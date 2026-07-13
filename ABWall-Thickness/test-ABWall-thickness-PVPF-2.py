from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

import sys
sys.path.append("/home/heidi/Documents/VerHem-project/paraview-pvpython-py-scripts/ABWall-Thickness")
import Module_GLSCC_calculator as sc

import numpy as np

np.set_printoptions(precision=10)

####################################
data=inputs[0]

print("*-------------------*")
print(data)

print("*--dir(data)--*")
print(dir(data))

print("*--data.PointData--*")
print(data.PointData)

print("*-- data.PointData['gap'] --*")
print(data.PointData['gap'])

print("*-------------------*")
gap=data.PointData['gap']

print("*--gap--*")
print(gap)
print(gap.shape)

print(isinstance(gap, np.ndarray))

####################################
# gapA=3.771407909977933
# gapB=3.971606522061835
gapA=sc.gapA(22, 0.6)
gapB=sc.gapB(22, 0.6)

tol_gap=7*(10.0**-3)

####################################
print("*-------------------*")

print("*--dir(data.PointData)--*")
print(dir(data.PointData))

print("*-------------------*")
print("*--data.PointData.keys()--*")
print(data.PointData.keys())

print("*-------------------*")

print("*--data.Points.DataSet()--*")
print(data.Points.DataSet)

print("*-------------------*")
print("*--isinstance data.GetPoints()--*")
PointsArray=data.GetPoints()

print(isinstance(PointsArray, np.ndarray))

print("*--PointsArray.shape--*")
print(PointsArray.shape)

#print(dir(data.PointData.keys.__dir__))


####################################
print("*-------------------*")
#print("*--x0y0PointsArray--*")
print("*--PointsArray--*")
print(PointsArray[0:10,:])

x0y0PointsArray=PointsArray[:,2]

print(x0y0PointsArray.shape)

print(x0y0PointsArray[5]-x0y0PointsArray[6])
print(x0y0PointsArray[6])
print(x0y0PointsArray[7]-x0y0PointsArray[8])
print(x0y0PointsArray[8])

####################################
print("*--------------------*")
zArrayAphase=x0y0PointsArray[np.abs(gap - gapA) <= tol_gap]
zArrayBphase=x0y0PointsArray[np.abs(gap - gapB) <= tol_gap]

print("*--zArrayAphase--*")
print(zArrayAphase)
print("*--zArrayBphase--*")
print(zArrayBphase)

print("*--dzArrayAphase--*")
dzArrayAphase=np.diff(zArrayAphase)
print(dzArrayAphase)

print("*--np.max(dzArrayAphase)--*")
print(np.max(dzArrayAphase))
i, = np.where(dzArrayAphase==np.max(dzArrayAphase))
print(i[0])

print("*--zArrayAphase[0:i[0]]--*")
zArrayAphase=zArrayAphase[0:(i[0]+1)]
print(zArrayAphase)

##########################################

print("AB Wall thickness in this dataset")
ABthick=zArrayBphase[0]-zArrayAphase[len(zArrayAphase)-1]
print(ABthick)
print(zArrayBphase[0])
print(zArrayAphase[len(zArrayAphase)-1])
