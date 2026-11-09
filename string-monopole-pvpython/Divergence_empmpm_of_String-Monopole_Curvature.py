# For pvpython - ParaView python shell
# Calclate the Divergence of surface charge density of string-monopole
# for calculating topological invarient integral.
# 
# div e^ijk m.\partial_i m x \partial_j m = 6 det M,  M_ji = d_j m_i
from paraview.simple import *



# ---- load gradient of m-vector ----------------------------------------
reader = XMLPartitionedUnstructuredGridReader(registrationName='gradient-m',
                                              FileName=['/home/heidi/Documents/string-monopole/test-dealii-9.5-Trilinos-14.4-VI/refine-cycle_3/gradient-m-vector-solution-13-8-MPI.pvtu'])
reader.UpdatePipeline()
print('Point arrays found:', list(reader.PointData.keys()))

# 'm_i1', 'm_i2', 'm_i3' hold grad(m_x), grad(m_y), grad(m_z).
# Column 0, 1, 2 ([:,i]) of each is the derivative along x, y, z.
# Row j of the matrix M = d_j m_i is the vector (d_j m_x, d_j m_y, d_j m_z).

# ---- row 0 of M: (d_x m_x, d_x m_y, d_x m_z) ---------------------------
M_p0Row = PythonCalculator(registrationName='M_p0Row', Input=reader)
# M_p0Row.ArrayAssociation = 'Point Data'
M_p0Row.ArrayName = 'M_p0Row'
M_p0Row.CopyArrays = 0
M_p0Row.Expression = ("make_vector(inputs[0].PointData['m_i1'][:, 0], "
                     "inputs[0].PointData['m_i2'][:, 0], "
                     "inputs[0].PointData['m_i3'][:, 0])")

# ---- row 1 of M: (d_y m_x, d_y m_y, d_y m_z) ---------------------------
M_p1Row = PythonCalculator(registrationName='M_p1Row', Input=reader)
# M_p1Row.ArrayAssociation = 'Point Data'
M_p1Row.ArrayName = 'M_p1Row'
M_p1Row.CopyArrays = 0
M_p1Row.Expression = ("make_vector(inputs[0].PointData['m_i1'][:, 1], "
                     "inputs[0].PointData['m_i2'][:, 1], "
                     "inputs[0].PointData['m_i3'][:, 1])")

# ---- row 2 of M: (d_z m_x, d_z m_y, d_z m_z) ---------------------------
M_p2Row = PythonCalculator(registrationName='M_p2Row', Input=reader)
# M_p2Row.ArrayAssociation = 'Point Data'
M_p2Row.ArrayName = 'M_p2Row'
M_p2Row.CopyArrays = 0
M_p2Row.Expression = ("make_vector(inputs[0].PointData['m_i1'][:, 2], "
                     "inputs[0].PointData['m_i2'][:, 2], "
                     "inputs[0].PointData['m_i3'][:, 2])")

# ---- cross product of rows 1 and 2: row1 x row2 ------------------------
# Stored as its own array so that dot() below receives two ParaView arrays.
cross_M_p1Row_M_p2Row = PythonCalculator(registrationName='cross_M_p1Row_M_p2Row', Input=[M_p1Row, M_p2Row])
# cross_M_p1Row_M_p2Row.ArrayAssociation = 'Point Data'
cross_M_p1Row_M_p2Row.ArrayName = 'cross_M_p1Row_M_p2Row'
cross_M_p1Row_M_p2Row.CopyArrays = 0
cross_M_p1Row_M_p2Row.Expression = ("cross(inputs[0].PointData['M_p1Row'], "
                      "inputs[1].PointData['M_p2Row'])")
 
# ---- divergence: 3 det M = 3 * row0 . (row1 x row2) --------------------
div_empmpm = PythonCalculator(registrationName='div_empmpm', Input=[M_p0Row, cross_M_p1Row_M_p2Row])
# div_empmpm.ArrayAssociation = 'Point Data'
div_empmpm.ArrayName = 'div_empmpm'
div_empmpm.CopyArrays = 0
div_empmpm.Expression = ("6 * dot(inputs[0].PointData['M_p0Row'], "
                    "inputs[1].PointData['cross_M_p1Row_M_p2Row'])")
div_empmpm.UpdatePipeline()
print('range of div empmpm = 6 det M:', div_empmpm.PointData['div_empmpm'].GetRange())

# Show(div_empmpm)
# Render()

# ---- parallel save: divergence-j.pvtu + one piece per rank in a folder --
# SaveData('/path/to/pvtu/divergence-j.pvtu', proxy=div_empmpm,
#          PointDataArrays=['div_empmpm'],
#          UseSubdirectory=1)
# print('saved /path/to/pvtu/divergence-j.pvtu')
