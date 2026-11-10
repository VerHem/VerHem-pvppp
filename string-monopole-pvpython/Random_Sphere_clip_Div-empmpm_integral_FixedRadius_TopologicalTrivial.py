# This script calculates topological charge of string-monopole with randomly sitributed
# center of sphere clips of VerHem simulation grid. The integrals are done throguh strokes theram.
# The integral results of different sphere clips is saved as csv file.
from paraview.simple import *
from paraview import servermanager
from paraview.vtk.numpy_interface import dataset_adapter as dsa
import numpy as np

# ---------------- script control settings ----------------
data_loading_path = '/home/heidi/Documents/string-monopole/test-dealii-9.5-Trilinos-14.4-VI/refine-cycle_3/Divergence_empmpm_of_StringMonople_Curvature-solutioin-13-8-MPI.pvtu'
save_file = '/home/heidi/Documents/VerHem-project/VerHem-Visualization-Images/Div_empmpm_integrals-TopologicalTrivial-Solution-13-8-MPI.csv'

array_name = 'div_empmpm'      # name of the scalar array to integrate
radius = 80.0             # sphere clip radius
n_samples = 100          # number of random spheres volume integral

x_min, x_max = -70.0, -30.0
y_min, y_max = -70.0, -30.0
z_min, z_max = 60.0, 70.0 # (-60.0, -50.0)

seed = 7886
# -----------------------------------------------

# Load the dataset (stays on the server, works with a multi-rank remote server)
empmpmDataSet = XMLPartitionedUnstructuredGridReader(registrationName='Divergence_empmpm_of_StringMonople_Curvature-solutioin-13-8-MPI.pvtu', FileName=[data_loading_path])
empmpmDataSet.UpdatePipelineInformation()

# Sphere clip filter: 
sphereClip = Clip(registrationName='sphereClip', Input=empmpmDataSet)
sphereClip.ClipType = 'Sphere'
sphereClip.ClipType.Radius = radius
sphereClip.Invert = 1
sphereClip.Crinkleclip = 0

# IngegrateVaribles filter:
integrateVolume = IntegrateVariables(registrationName='IntegrateVariablesVolume', Input=sphereClip)
integrateVolume.DivideCellDataByVolume = 0

# Make random distributed sphere clip centerss
rng = np.random.default_rng(seed)
centers_x = rng.uniform(x_min, x_max, n_samples)
centers_y = rng.uniform(y_min, y_max, n_samples)
centers_z = rng.uniform(z_min, z_max, n_samples)

# intgrals saviing array
integrals = np.zeros(n_samples)

for i in range(n_samples):
    # Move the sphere
    sphereClip.ClipType.Center = [centers_x[i], centers_y[i], centers_z[i]]

    # Update the pipeline and bring the (single-point) result to the client
    integrateVolume.UpdatePipeline()
    integral_result = servermanager.Fetch(integrateVolume)

    # Empty sphereClip (sphere entirely outside the data): integral is zero
    if integral_result.GetNumberOfPoints() == 0:
        integrals[i] = 0.0
        continue

    integral_result_wrapped = dsa.WrapDataObject(integral_result)
    integrals[i] = integral_result_wrapped.PointData[array_name][0]

# Save integral results as csv: one row per sphere -> center x, y, z and the integral
table = np.column_stack((centers_x, centers_y, centers_z, integrals))

column_name = 'integral_' + array_name.replace(' ', '_')
Header = "'center_x','center_y','center_z','" + column_name + "'"

np.savetxt(save_file,
           table,
           delimiter=',',
           header=Header,
           comments='')

print('Saved', n_samples, 'integrals to', save_file)
