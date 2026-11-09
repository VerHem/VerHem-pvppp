# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
mVectorPointDataSet = FindSource('m-n-vector-solution-13-8-MPI.pvtu')

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=mVectorPointDataSet)

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = "gradient(inputs[0].PointData['m'][:,0])"
pythonCalculator1.ArrayName = 'm_i1'
pythonCalculator1.CopyArrays = 0

# create a new 'Python Calculator'
pythonCalculator2 = PythonCalculator(registrationName='PythonCalculator2', Input=mVectorPointDataSet)

# Properties modified on pythonCalculator2
pythonCalculator2.Expression = "gradient(inputs[0].PointData['m'][:,1])"
pythonCalculator2.ArrayName = 'm_i2'
pythonCalculator2.CopyArrays = 0

# create a new 'Python Calculator'
pythonCalculator3 = PythonCalculator(registrationName='PythonCalculator3', Input=mVectorPointDataSet)

# Properties modified on pythonCalculator3
pythonCalculator3.Expression = "gradient(inputs[0].PointData['m'][:,2])"
pythonCalculator3.ArrayName = 'm_i3'
pythonCalculator3.CopyArrays = 0

