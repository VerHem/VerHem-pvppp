from paraview.vtk.numpy_interface import dataset_adapter as dsa
from paraview.vtk.numpy_interface import algorithms as algs
import numpy as np

data = inputs[0]
#print(data.PointData.keys())
print(data.PointData['u_12'])
print("u_12.shape is")

# this ouput u_12's shape is (32768,), which menans it is a 1D vector
print(data.PointData['u_12'].shape)

u12=data.PointData['u_12']
v12=data.PointData['v_12']
print(type(u12))

# this gonna to say u12, which is VTKarray, is also np array
print(isinstance(u12, np.ndarray))

output.PointData.append(v12 + 1, 'v12p1')
print(algs.max(u12))
print(algs.max(data.PointData['v12p1']))
#print(data.VTKObject)


# take derivative directly on unstructed array
print("algs.gradient() call:")
print(algs.gradient(data.PointData['u_11']))
gu11=algs.gradient(data.PointData['u_11'])

# gradient os u_11 is (32768,3), so u11 is structed as vector, is this so-called VTKArray
print(gu11.shape)

output.PointData.append(gu11, 'gu11')

print(data.GetNumberOfCells())

help(algs)