# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
output_conf_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='output_conf_00.pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/lumi/2dPDW/z-axis-300nm-xy-perodic-2dPDW-test-X-random-iniconf-IV-120x105x15.24-breakgoodrun/refine-cycle_0/output_conf_00.pvtu'])
output_conf_00pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# Properties modified on output_conf_00pvtu
output_conf_00pvtu.PointArrayStatus = ['subdomain', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33']
output_conf_00pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
output_conf_00pvtuDisplay = Show(output_conf_00pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
output_conf_00pvtuDisplay.Representation = 'Surface'
output_conf_00pvtuDisplay.ColorArrayName = [None, '']
output_conf_00pvtuDisplay.SelectTCoordArray = 'None'
output_conf_00pvtuDisplay.SelectNormalArray = 'None'
output_conf_00pvtuDisplay.SelectTangentArray = 'None'
output_conf_00pvtuDisplay.OSPRayScaleArray = 'subdomain'
output_conf_00pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
output_conf_00pvtuDisplay.SelectOrientationVectors = 'None'
output_conf_00pvtuDisplay.ScaleFactor = 12.0
output_conf_00pvtuDisplay.SelectScaleArray = 'None'
output_conf_00pvtuDisplay.GlyphType = 'Arrow'
output_conf_00pvtuDisplay.GlyphTableIndexArray = 'None'
output_conf_00pvtuDisplay.GaussianRadius = 0.6
output_conf_00pvtuDisplay.SetScaleArray = ['POINTS', 'subdomain']
output_conf_00pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
output_conf_00pvtuDisplay.OpacityArray = ['POINTS', 'subdomain']
output_conf_00pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
output_conf_00pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
output_conf_00pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
output_conf_00pvtuDisplay.ScalarOpacityUnitDistance = 2.5028001676159013
output_conf_00pvtuDisplay.OpacityArrayName = ['POINTS', 'subdomain']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
output_conf_00pvtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 8191.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
output_conf_00pvtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 8191.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
output_conf_00pvtuDisplay.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
output_conf_00pvtuDisplay.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
output_conf_00pvtuDisplay.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
output_conf_00pvtuDisplay.DataAxesGrid.XTitleBold = 1
output_conf_00pvtuDisplay.DataAxesGrid.XTitleFontSize = 24
output_conf_00pvtuDisplay.DataAxesGrid.YTitleBold = 1
output_conf_00pvtuDisplay.DataAxesGrid.YTitleFontSize = 24
output_conf_00pvtuDisplay.DataAxesGrid.ZTitleBold = 1
output_conf_00pvtuDisplay.DataAxesGrid.ZTitleFontSize = 23
output_conf_00pvtuDisplay.DataAxesGrid.XLabelBold = 1
output_conf_00pvtuDisplay.DataAxesGrid.XLabelFontSize = 17
output_conf_00pvtuDisplay.DataAxesGrid.YLabelBold = 1
output_conf_00pvtuDisplay.DataAxesGrid.YLabelFontSize = 17
output_conf_00pvtuDisplay.DataAxesGrid.ZLabelBold = 1
output_conf_00pvtuDisplay.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=output_conf_00pvtu)
pythonCalculator1.Expression = ''

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = "gradient(inputs[0].PointData['u_12'])"
pythonCalculator1.ArrayName = 'u_i12'
pythonCalculator1.CopyArrays = 0

# show data in view
pythonCalculator1Display = Show(pythonCalculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator1Display.Representation = 'Surface'
pythonCalculator1Display.ColorArrayName = [None, '']
pythonCalculator1Display.SelectTCoordArray = 'None'
pythonCalculator1Display.SelectNormalArray = 'None'
pythonCalculator1Display.SelectTangentArray = 'None'
pythonCalculator1Display.OSPRayScaleArray = 'u_i12'
pythonCalculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator1Display.SelectOrientationVectors = 'None'
pythonCalculator1Display.ScaleFactor = 12.0
pythonCalculator1Display.SelectScaleArray = 'None'
pythonCalculator1Display.GlyphType = 'Arrow'
pythonCalculator1Display.GlyphTableIndexArray = 'None'
pythonCalculator1Display.GaussianRadius = 0.6
pythonCalculator1Display.SetScaleArray = ['POINTS', 'u_i12']
pythonCalculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.OpacityArray = ['POINTS', 'u_i12']
pythonCalculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator1Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator1Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator1Display.OpacityArrayName = ['POINTS', 'u_i12']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator1Display.ScaleTransferFunction.Points = [-0.03856517246791295, 0.0, 0.5, 0.0, 0.03781185150146485, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator1Display.OpacityTransferFunction.Points = [-0.03856517246791295, 0.0, 0.5, 0.0, 0.03781185150146485, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator1Display.DataAxesGrid.XTitleBold = 1
pythonCalculator1Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator1Display.DataAxesGrid.YTitleBold = 1
pythonCalculator1Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator1Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator1Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator1Display.DataAxesGrid.XLabelBold = 1
pythonCalculator1Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator1Display.DataAxesGrid.YLabelBold = 1
pythonCalculator1Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator1Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator1Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(output_conf_00pvtu)

# set active source
SetActiveSource(pythonCalculator1)

# set active source
SetActiveSource(output_conf_00pvtu)

# set active source
SetActiveSource(pythonCalculator1)

# set active source
SetActiveSource(output_conf_00pvtu)

# set active source
SetActiveSource(pythonCalculator1)

# create a new 'Python Calculator'
pythonCalculator2 = PythonCalculator(registrationName='PythonCalculator2', Input=[output_conf_00pvtu, pythonCalculator1])
pythonCalculator2.Expression = ''

# Properties modified on pythonCalculator2
pythonCalculator2.Expression = "-inputs[1].PointData['u_i12']*inputs[0].PointData['v_12']"
pythonCalculator2.CopyArrays = 0

# show data in view
pythonCalculator2Display = Show(pythonCalculator2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator2Display.Representation = 'Surface'
pythonCalculator2Display.ColorArrayName = [None, '']
pythonCalculator2Display.SelectTCoordArray = 'None'
pythonCalculator2Display.SelectNormalArray = 'None'
pythonCalculator2Display.SelectTangentArray = 'None'
pythonCalculator2Display.OSPRayScaleArray = 'result'
pythonCalculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator2Display.SelectOrientationVectors = 'None'
pythonCalculator2Display.ScaleFactor = 12.0
pythonCalculator2Display.SelectScaleArray = 'None'
pythonCalculator2Display.GlyphType = 'Arrow'
pythonCalculator2Display.GlyphTableIndexArray = 'None'
pythonCalculator2Display.GaussianRadius = 0.6
pythonCalculator2Display.SetScaleArray = ['POINTS', 'result']
pythonCalculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator2Display.OpacityArray = ['POINTS', 'result']
pythonCalculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator2Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator2Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator2Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator2Display.OpacityArrayName = ['POINTS', 'result']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator2Display.ScaleTransferFunction.Points = [-0.022672902878789935, 0.0, 0.5, 0.0, 0.02323537931963204, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator2Display.OpacityTransferFunction.Points = [-0.022672902878789935, 0.0, 0.5, 0.0, 0.02323537931963204, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator2Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator2Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator2Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator2Display.DataAxesGrid.XTitleBold = 1
pythonCalculator2Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator2Display.DataAxesGrid.YTitleBold = 1
pythonCalculator2Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator2Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator2Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator2Display.DataAxesGrid.XLabelBold = 1
pythonCalculator2Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator2Display.DataAxesGrid.YLabelBold = 1
pythonCalculator2Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator2Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator2Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# hide data in view
Hide(pythonCalculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1922, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 309.4424729524235]
renderView1.CameraParallelScale = 80.08960536370884

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).