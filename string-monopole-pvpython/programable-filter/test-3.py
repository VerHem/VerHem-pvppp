# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
setup_conf_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='setup_conf_00.pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/lumi/string-monople/runs-32bar-0Hfield/t-0.50/refine-cycle_0/setup_conf_00.pvtu'])
setup_conf_00pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# Properties modified on setup_conf_00pvtu
setup_conf_00pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
setup_conf_00pvtuDisplay = Show(setup_conf_00pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
setup_conf_00pvtuDisplay.Representation = 'Surface'
setup_conf_00pvtuDisplay.ColorArrayName = [None, '']
setup_conf_00pvtuDisplay.SelectTCoordArray = 'None'
setup_conf_00pvtuDisplay.SelectNormalArray = 'None'
setup_conf_00pvtuDisplay.SelectTangentArray = 'None'
setup_conf_00pvtuDisplay.OSPRayScaleArray = 'du_11'
setup_conf_00pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
setup_conf_00pvtuDisplay.SelectOrientationVectors = 'None'
setup_conf_00pvtuDisplay.ScaleFactor = 3.0
setup_conf_00pvtuDisplay.SelectScaleArray = 'None'
setup_conf_00pvtuDisplay.GlyphType = 'Arrow'
setup_conf_00pvtuDisplay.GlyphTableIndexArray = 'None'
setup_conf_00pvtuDisplay.GaussianRadius = 0.15
setup_conf_00pvtuDisplay.SetScaleArray = ['POINTS', 'du_11']
setup_conf_00pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
setup_conf_00pvtuDisplay.OpacityArray = ['POINTS', 'du_11']
setup_conf_00pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
setup_conf_00pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
setup_conf_00pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
setup_conf_00pvtuDisplay.ScalarOpacityUnitDistance = 3.247595264191645
setup_conf_00pvtuDisplay.OpacityArrayName = ['POINTS', 'du_11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
setup_conf_00pvtuDisplay.ScaleTransferFunction.Points = [-6.092341209296137e-06, 0.0, 0.5, 0.0, 1.2894259953100118e-06, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
setup_conf_00pvtuDisplay.OpacityTransferFunction.Points = [-6.092341209296137e-06, 0.0, 0.5, 0.0, 1.2894259953100118e-06, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=setup_conf_00pvtu)
programmableFilter1.Script = ''
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# Properties modified on programmableFilter1
programmableFilter1.Script ="""
from paraview.vtk.numpy_interface import dataset_adapter as dsa
from paraview.vtk.numpy_interface import algorithms as algs
import numpy as np

data = inputs[0]
#print(data.PointData.keys())
print(data.PointData[\'u_12\'])
print("u_12.shape is")

# this ouput u_12\'s shape is (32768,), which menans it is a 1D vector
print(data.PointData[\'u_12\'].shape)

u12=data.PointData[\'u_12\']
v12=data.PointData[\'v_12\']
print(type(u12))

# this gonna to say u12, which is VTKarray, is also np array
print(isinstance(u12, np.ndarray))

output.PointData.append(v12 + 1, \'v12p1\')
print(algs.max(u12))
print(algs.max(data.PointData[\'v12p1\']))
#print(data.VTKObject)


# take derivative directly on unstructed array
print("algs.gradient() call:")
print(algs.gradient(data.PointData[\'u_11\']))
gu11=algs.gradient(data.PointData[\'u_11\'])

# gradient os u_11 is (32768,3), so u11 is structed as vector, is this so-called VTKArray
print(gu11.shape)

output.PointData.append(gu11, \'gu11\')

print(data.GetNumberOfCells())
"""
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# show data in view
programmableFilter1Display = Show(programmableFilter1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
programmableFilter1Display.Representation = 'Surface'
programmableFilter1Display.ColorArrayName = [None, '']
programmableFilter1Display.SelectTCoordArray = 'None'
programmableFilter1Display.SelectNormalArray = 'None'
programmableFilter1Display.SelectTangentArray = 'None'
programmableFilter1Display.OSPRayScaleArray = 'gu11'
programmableFilter1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableFilter1Display.SelectOrientationVectors = 'None'
programmableFilter1Display.ScaleFactor = 3.0
programmableFilter1Display.SelectScaleArray = 'None'
programmableFilter1Display.GlyphType = 'Arrow'
programmableFilter1Display.GlyphTableIndexArray = 'None'
programmableFilter1Display.GaussianRadius = 0.15
programmableFilter1Display.SetScaleArray = ['POINTS', 'gu11']
programmableFilter1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.OpacityArray = ['POINTS', 'gu11']
programmableFilter1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableFilter1Display.PolarAxes = 'PolarAxesRepresentation'
programmableFilter1Display.ScalarOpacityUnitDistance = 3.247595264191645
programmableFilter1Display.OpacityArrayName = ['POINTS', 'gu11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
programmableFilter1Display.ScaleTransferFunction.Points = [-1.1107818126678466, 0.0, 0.5, 0.0, 1.1107818603515622, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
programmableFilter1Display.OpacityTransferFunction.Points = [-1.1107818126678466, 0.0, 0.5, 0.0, 1.1107818603515622, 1.0, 0.5, 0.0]

# hide data in view
Hide(setup_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(programmableFilter1Display, ('POINTS', 'v12p1'))

# rescale color and/or opacity maps used to include current data range
programmableFilter1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
programmableFilter1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'v12p1'
v12p1LUT = GetColorTransferFunction('v12p1')
v12p1LUT.RGBPoints = [-1.1222343444824219, 0.231373, 0.298039, 0.752941, 1.448106288909912, 0.865003, 0.865003, 0.865003, 4.018446922302246, 0.705882, 0.0156863, 0.14902]
v12p1LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'v12p1'
v12p1PWF = GetOpacityTransferFunction('v12p1')
v12p1PWF.Points = [-1.1222343444824219, 0.0, 0.5, 0.0, 4.018446922302246, 1.0, 0.5, 0.0]
v12p1PWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(programmableFilter1Display, ('POINTS', 'gu11', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(v12p1LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
programmableFilter1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
programmableFilter1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'gu11'
gu11LUT = GetColorTransferFunction('gu11')
gu11LUT.RGBPoints = [0.0008038457371477765, 0.231373, 0.298039, 0.752941, 0.557384996255063, 0.865003, 0.865003, 0.865003, 1.1139661467729782, 0.705882, 0.0156863, 0.14902]
gu11LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'gu11'
gu11PWF = GetOpacityTransferFunction('gu11')
gu11PWF.Points = [0.0008038457371477765, 0.0, 0.5, 0.0, 1.1139661467729782, 1.0, 0.5, 0.0]
gu11PWF.ScalarRangeInitialized = 1

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1820, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.6930862197996582, -1.0067439041118153e-05, 100.37956371656429]
renderView1.CameraViewUp = [-1.9367215516210614e-05, 0.999999999812455, -3.343022251442501e-08]
renderView1.CameraParallelScale = 25.98076211353316

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
