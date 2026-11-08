# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Sphere'
sphere1 = Sphere(registrationName='Sphere1')

# Properties modified on sphere1
sphere1.Center = [-70.0, -70.0, -122.0]
sphere1.Radius = 162.0
sphere1.ThetaResolution = 1000
sphere1.EndTheta = 90.0
sphere1.PhiResolution = 1000
sphere1.EndPhi = 59.5

# find source
empmpmVectorDataSet = FindSource('empmpm-Components-solution-13-8-MPI.pvtu')

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(registrationName='ResampleWithDataset1', SourceDataArrays=empmpmVectorDataSet, DestinationMesh=sphere1)
resampleWithDataset1.CellLocator = 'Static Cell Locator'

# Properties modified on resampleWithDataset1
resampleWithDataset1.PassPointArrays = 1

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=resampleWithDataset1)

calculator1.ResultArrayName = 'empmpm.n'
calculator1.Function = 'dot(empmpm,Normals)'

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=calculator1)
