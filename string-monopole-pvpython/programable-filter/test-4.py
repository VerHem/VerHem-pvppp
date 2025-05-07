from paraview.vtk.numpy_interface import dataset_adapter as dsa
from paraview.vtk.numpy_interface import algorithms as algs
import numpy as np

from scipy.optimize import fsolve

def equations(svec, *paras):
    m1, m2, m3, n1, n2, n3, cosphi, sinphi = svec
    u11, v11, u12, v12, u13, v13, DeltaA = paras
    return [-u11 + ((cosphi*m1 - n1*sinphi)*DeltaA)/1.414213562,
            -v11 + ((cosphi*n1 + m1*sinphi)*DeltaA)/1.414213562,
            -u12 + ((cosphi*m2 - n2*sinphi)*DeltaA)/1.414213562,
            -v12 + ((cosphi*n2 + m2*sinphi)*DeltaA)/1.414213562,
            -u13 + ((cosphi*m3 - n3*sinphi)*DeltaA)/1.414213562,
            -v13 + ((cosphi*n3 + m3*sinphi)*DeltaA)/1.414213562,
            -1 + cosphi*cosphi + sinphi*sinphi,
            m1*n1 + m2*n2 + m3*n3]

data = inputs[0]
#print(data.PointData.keys())
#print(data.PointData['u_12'])
#print("u_12.shape is")

# this ouput u_12's shape is (32768,), which menans it is a 1D vector
# print(data.PointData['u_12'].shape)

u11=data.PointData['u_11']
u12=data.PointData['u_12']
u13=data.PointData['u_13']
v11=data.PointData['v_11']
v12=data.PointData['v_12']
v13=data.PointData['v_13']
#print(type(u12))

NumRow=32768
#NumRow=10
gap2=np.zeros(shape=(NumRow,))
Vm=np.zeros(shape=(NumRow, 3))
Vn=np.zeros(shape=(NumRow, 3))
cosPhi=np.zeros(shape=(NumRow,))
sinPhi=np.zeros(shape=(NumRow,))

inivec2=(1.0, 0., 0., 0., 1.0, 0., 1., 0.)

# this gonna to say u12, which is VTKarray, is also np array
# print(isinstance(u12, np.ndarray))

# output.PointData.append(v12 + 1, 'v12p1')
# print(algs.max(u12))
# print(algs.max(data.PointData['v12p1']))
#print(data.VTKObject)


# take derivative directly on unstructed array
# print("algs.gradient() call:")
# print(algs.gradient(data.PointData['u_11']))
# gu11=algs.gradient(data.PointData['u_11'])

# gradient os u_11 is (32768,3), so u11 is structed as vector, is this so-called VTKArray
# print(gu11.shape)

# output.PointData.append(gu11, 'gu11')

# print(data.GetNumberOfCells())
for i in range(NumRow):
    #print("gap^2 is")
    #gap2[i]=u11[i]*u11[i]+u12[i]*u12[i]+u13[i]*u13[i]+v11[i]*v11[i]+v12[i]*v12[i]+v13[i]*v13[i]
    print(u11[i]*u11[i]+u12[i]*u12[i]+u13[i]*u13[i]+v11[i]*v11[i]+v12[i]*v12[i]+v13[i]*v13[i])
    paras2=(u11[i], u12[i], u13[i], v11[i], v12[i], v13[i], 3.87091)
    s = fsolve(equations, inivec2, args=paras2, xtol=1.49012e-13)
    Vm[i]=[s[0],s[1],s[2]]
    Vn[i]=[s[3],s[4],s[5]]
    cosPhi[i]=s[6]
    sinPhi[i]=s[7]

#print("Vm looks like :")
#print(Vm)
#print("Vn looks like :")
#print(Vn)

output.PointData.append(Vm, 'm')
output.PointData.append(Vn, 'n')
output.PointData.append(cosPhi, 'cosPHI')
output.PointData.append(sinPhi, 'sinPHI')
#output.PointData.append(gap2, 'gap2')