from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

import numpy as np
np.set_printoptions(precision=10)

####################################
data=inputs[0]

print("*-------------------*")
print(data)

print(data.PointData)

print("*-- data.PointData['gap'] --*")
print(data.PointData['gap'])

print("*-------------------*")
gap=data.PointData['gap']

print(gap.shape)

print(isinstance(gap, np.ndarray))

####################################
gapA=3.495287723239516
gapB=3.623231838876226

tol_gap=10**-2

####################################
print("*-------------------*")
print("*--dir(data)--*")
print(dir(data))

print("*--dir(data.PointData)--*")
print(dir(data.PointData))

print("*-------------------*")
print("*--data.PointData.keys()--*")
print(data.PointData.keys())

#print(dir(data.__dict__.__getattribute__))

print("*-------------------*")
print("*--data.GetPoints()--*")
print(data.GetPoints())

print("*--data.Points.DataSet()--*")
print(data.Points.DataSet)

print("*-------------------*")
print("*--isinstance data.GetPoints()--*")
PointsArray=data.GetPoints()

print(isinstance(PointsArray, np.ndarray))

#print("*--print(PointsArray)--*")
#print(PointsArray)

print("*--PointsArray.shape--*")
print(PointsArray.shape)

#print(dir(data.PointData.keys.__dir__))


####################################
print("*-------------------*")
#print("*--x0y0PointsArray--*")
print("*--PointsArray--*")
print(PointsArray[0:10,:])


x0PointsArray=PointsArray[PointsArray[:,0]==0]
print("*--x0PointsArray--*")
print(x0PointsArray[0:20,:])
# x0y0PointsArray=x0y0PointsArray[x0y0PointsArray[:,1]==0]


#x0y0PointsArray=PointsArray[(PointsArray[:,0]==0) & (PointsArray[:,1]==0)]
#print(x0y0PointsArray)

# x0y0PointsArray=x0y0PointsArray[:,2]

# print(x0y0PointsArray.shape)

# print(x0y0PointsArray[5]-x0y0PointsArray[6])
# print(x0y0PointsArray[6])
# print(x0y0PointsArray[7]-x0y0PointsArray[8])
# print(x0y0PointsArray[8])

####################################
# print("*-------------------*")
# gapArray=gap[PointsArray[:,0]==0]
# gapArray=gapArray[PointsArray[PointsArray[:,0]==0][:,1]==0]

# print(gapArray.shape)

# print("*--print.gapArray--*")
# print(gapArray)

# ####################################
# print("*--------------------*")
# zArrayAphase=x0y0PointsArray[np.abs(gapArray - gapA) <= tol_gap]
# zArrayBphase=x0y0PointsArray[np.abs(gapArray - gapB) <= tol_gap]

# print("*--zArrayAphase--*")
# print(zArrayAphase)
# print("*--zArrayBphase--*")
# print(zArrayBphase)
