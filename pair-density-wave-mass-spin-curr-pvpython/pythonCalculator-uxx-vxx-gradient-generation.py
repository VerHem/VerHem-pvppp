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
#output_conf_00pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

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
pythonCalculator1.Expression = "gradient(inputs[0].PointData['u_11'])"
pythonCalculator1.ArrayName = 'u_i11'
pythonCalculator1.CopyArrays = 0

# show data in view
pythonCalculator1Display = Show(pythonCalculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator1Display.Representation = 'Surface'
pythonCalculator1Display.ColorArrayName = [None, '']
pythonCalculator1Display.SelectTCoordArray = 'None'
pythonCalculator1Display.SelectNormalArray = 'None'
pythonCalculator1Display.SelectTangentArray = 'None'
pythonCalculator1Display.OSPRayScaleArray = 'u_i11'
pythonCalculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator1Display.SelectOrientationVectors = 'None'
pythonCalculator1Display.ScaleFactor = 12.0
pythonCalculator1Display.SelectScaleArray = 'None'
pythonCalculator1Display.GlyphType = 'Arrow'
pythonCalculator1Display.GlyphTableIndexArray = 'None'
pythonCalculator1Display.GaussianRadius = 0.6
pythonCalculator1Display.SetScaleArray = ['POINTS', 'u_i11']
pythonCalculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.OpacityArray = ['POINTS', 'u_i11']
pythonCalculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator1Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator1Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator1Display.OpacityArrayName = ['POINTS', 'u_i11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator1Display.ScaleTransferFunction.Points = [-0.04944011370340984, 0.0, 0.5, 0.0, 0.049654599598475874, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator1Display.OpacityTransferFunction.Points = [-0.04944011370340984, 0.0, 0.5, 0.0, 0.049654599598475874, 1.0, 0.5, 0.0]

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

# hide data in view
Hide(pythonCalculator1, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator2 = PythonCalculator(registrationName='PythonCalculator2', Input=output_conf_00pvtu)
pythonCalculator2.Expression = ''

# Properties modified on pythonCalculator2
pythonCalculator2.Expression = "gradient(inputs[0].PointData['u_12'])"
pythonCalculator2.ArrayName = 'u_i12'
pythonCalculator2.CopyArrays = 0

# show data in view
pythonCalculator2Display = Show(pythonCalculator2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator2Display.Representation = 'Surface'
pythonCalculator2Display.ColorArrayName = [None, '']
pythonCalculator2Display.SelectTCoordArray = 'None'
pythonCalculator2Display.SelectNormalArray = 'None'
pythonCalculator2Display.SelectTangentArray = 'None'
pythonCalculator2Display.OSPRayScaleArray = 'u_i12'
pythonCalculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator2Display.SelectOrientationVectors = 'None'
pythonCalculator2Display.ScaleFactor = 12.0
pythonCalculator2Display.SelectScaleArray = 'None'
pythonCalculator2Display.GlyphType = 'Arrow'
pythonCalculator2Display.GlyphTableIndexArray = 'None'
pythonCalculator2Display.GaussianRadius = 0.6
pythonCalculator2Display.SetScaleArray = ['POINTS', 'u_i12']
pythonCalculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator2Display.OpacityArray = ['POINTS', 'u_i12']
pythonCalculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator2Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator2Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator2Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator2Display.OpacityArrayName = ['POINTS', 'u_i12']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator2Display.ScaleTransferFunction.Points = [-0.03856517246791295, 0.0, 0.5, 0.0, 0.03781185150146485, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator2Display.OpacityTransferFunction.Points = [-0.03856517246791295, 0.0, 0.5, 0.0, 0.03781185150146485, 1.0, 0.5, 0.0]

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

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator3 = PythonCalculator(registrationName='PythonCalculator3', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator3
pythonCalculator3.Expression = "gradient(inputs[0].PointData['u_13'])"
pythonCalculator3.ArrayName = 'u_i13'
pythonCalculator3.CopyArrays = 0

# show data in view
pythonCalculator3Display = Show(pythonCalculator3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator3Display.Representation = 'Surface'
pythonCalculator3Display.ColorArrayName = [None, '']
pythonCalculator3Display.SelectTCoordArray = 'None'
pythonCalculator3Display.SelectNormalArray = 'None'
pythonCalculator3Display.SelectTangentArray = 'None'
pythonCalculator3Display.OSPRayScaleArray = 'u_i13'
pythonCalculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator3Display.SelectOrientationVectors = 'None'
pythonCalculator3Display.ScaleFactor = 12.0
pythonCalculator3Display.SelectScaleArray = 'None'
pythonCalculator3Display.GlyphType = 'Arrow'
pythonCalculator3Display.GlyphTableIndexArray = 'None'
pythonCalculator3Display.GaussianRadius = 0.6
pythonCalculator3Display.SetScaleArray = ['POINTS', 'u_i13']
pythonCalculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator3Display.OpacityArray = ['POINTS', 'u_i13']
pythonCalculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator3Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator3Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator3Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator3Display.OpacityArrayName = ['POINTS', 'u_i13']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator3Display.ScaleTransferFunction.Points = [-0.207784941082909, 0.0, 0.5, 0.0, 0.20914519173758372, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator3Display.OpacityTransferFunction.Points = [-0.207784941082909, 0.0, 0.5, 0.0, 0.20914519173758372, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator3Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator3Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator3Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator3Display.DataAxesGrid.XTitleBold = 1
pythonCalculator3Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator3Display.DataAxesGrid.YTitleBold = 1
pythonCalculator3Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator3Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator3Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator3Display.DataAxesGrid.XLabelBold = 1
pythonCalculator3Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator3Display.DataAxesGrid.YLabelBold = 1
pythonCalculator3Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator3Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator3Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator2, renderView1)

# hide data in view
Hide(pythonCalculator3, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator4 = PythonCalculator(registrationName='PythonCalculator4', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator4
pythonCalculator4.Expression = "gradient(inputs[0].PointData['u_21'])"
pythonCalculator4.ArrayName = 'u_i21'
pythonCalculator4.CopyArrays = 0

# show data in view
pythonCalculator4Display = Show(pythonCalculator4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator4Display.Representation = 'Surface'
pythonCalculator4Display.ColorArrayName = [None, '']
pythonCalculator4Display.SelectTCoordArray = 'None'
pythonCalculator4Display.SelectNormalArray = 'None'
pythonCalculator4Display.SelectTangentArray = 'None'
pythonCalculator4Display.OSPRayScaleArray = 'u_i21'
pythonCalculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator4Display.SelectOrientationVectors = 'None'
pythonCalculator4Display.ScaleFactor = 12.0
pythonCalculator4Display.SelectScaleArray = 'None'
pythonCalculator4Display.GlyphType = 'Arrow'
pythonCalculator4Display.GlyphTableIndexArray = 'None'
pythonCalculator4Display.GaussianRadius = 0.6
pythonCalculator4Display.SetScaleArray = ['POINTS', 'u_i21']
pythonCalculator4Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator4Display.OpacityArray = ['POINTS', 'u_i21']
pythonCalculator4Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator4Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator4Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator4Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator4Display.OpacityArrayName = ['POINTS', 'u_i21']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator4Display.ScaleTransferFunction.Points = [-0.03371106102353051, 0.0, 0.5, 0.0, 0.03440081278483073, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator4Display.OpacityTransferFunction.Points = [-0.03371106102353051, 0.0, 0.5, 0.0, 0.03440081278483073, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator4Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator4Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator4Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator4Display.DataAxesGrid.XTitleBold = 1
pythonCalculator4Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator4Display.DataAxesGrid.YTitleBold = 1
pythonCalculator4Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator4Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator4Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator4Display.DataAxesGrid.XLabelBold = 1
pythonCalculator4Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator4Display.DataAxesGrid.YLabelBold = 1
pythonCalculator4Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator4Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator4Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator4, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator5 = PythonCalculator(registrationName='PythonCalculator5', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator5
pythonCalculator5.Expression = "gradient(inputs[0].PointData['u_22'])"
pythonCalculator5.ArrayName = 'u_i22'
pythonCalculator5.CopyArrays = 0

# show data in view
pythonCalculator5Display = Show(pythonCalculator5, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator5Display.Representation = 'Surface'
pythonCalculator5Display.ColorArrayName = [None, '']
pythonCalculator5Display.SelectTCoordArray = 'None'
pythonCalculator5Display.SelectNormalArray = 'None'
pythonCalculator5Display.SelectTangentArray = 'None'
pythonCalculator5Display.OSPRayScaleArray = 'u_i22'
pythonCalculator5Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator5Display.SelectOrientationVectors = 'None'
pythonCalculator5Display.ScaleFactor = 12.0
pythonCalculator5Display.SelectScaleArray = 'None'
pythonCalculator5Display.GlyphType = 'Arrow'
pythonCalculator5Display.GlyphTableIndexArray = 'None'
pythonCalculator5Display.GaussianRadius = 0.6
pythonCalculator5Display.SetScaleArray = ['POINTS', 'u_i22']
pythonCalculator5Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator5Display.OpacityArray = ['POINTS', 'u_i22']
pythonCalculator5Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator5Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator5Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator5Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator5Display.OpacityArrayName = ['POINTS', 'u_i22']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator5Display.ScaleTransferFunction.Points = [-0.016930987721397766, 0.0, 0.5, 0.0, 0.016927037920270647, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator5Display.OpacityTransferFunction.Points = [-0.016930987721397766, 0.0, 0.5, 0.0, 0.016927037920270647, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator5Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator5Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator5Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator5Display.DataAxesGrid.XTitleBold = 1
pythonCalculator5Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator5Display.DataAxesGrid.YTitleBold = 1
pythonCalculator5Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator5Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator5Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator5Display.DataAxesGrid.XLabelBold = 1
pythonCalculator5Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator5Display.DataAxesGrid.YLabelBold = 1
pythonCalculator5Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator5Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator5Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator6 = PythonCalculator(registrationName='PythonCalculator6', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator6
pythonCalculator6.Expression = "gradient(inputs[0].PointData['u_23'])"
pythonCalculator6.ArrayName = 'u_i23'
pythonCalculator6.CopyArrays = 0

# show data in view
pythonCalculator6Display = Show(pythonCalculator6, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator6Display.Representation = 'Surface'
pythonCalculator6Display.ColorArrayName = [None, '']
pythonCalculator6Display.SelectTCoordArray = 'None'
pythonCalculator6Display.SelectNormalArray = 'None'
pythonCalculator6Display.SelectTangentArray = 'None'
pythonCalculator6Display.OSPRayScaleArray = 'u_i23'
pythonCalculator6Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator6Display.SelectOrientationVectors = 'None'
pythonCalculator6Display.ScaleFactor = 12.0
pythonCalculator6Display.SelectScaleArray = 'None'
pythonCalculator6Display.GlyphType = 'Arrow'
pythonCalculator6Display.GlyphTableIndexArray = 'None'
pythonCalculator6Display.GaussianRadius = 0.6
pythonCalculator6Display.SetScaleArray = ['POINTS', 'u_i23']
pythonCalculator6Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator6Display.OpacityArray = ['POINTS', 'u_i23']
pythonCalculator6Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator6Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator6Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator6Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator6Display.OpacityArrayName = ['POINTS', 'u_i23']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator6Display.ScaleTransferFunction.Points = [-0.06503745544524421, 0.0, 0.5, 0.0, 0.06630675139881316, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator6Display.OpacityTransferFunction.Points = [-0.06503745544524421, 0.0, 0.5, 0.0, 0.06630675139881316, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator6Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator6Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator6Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator6Display.DataAxesGrid.XTitleBold = 1
pythonCalculator6Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator6Display.DataAxesGrid.YTitleBold = 1
pythonCalculator6Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator6Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator6Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator6Display.DataAxesGrid.XLabelBold = 1
pythonCalculator6Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator6Display.DataAxesGrid.YLabelBold = 1
pythonCalculator6Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator6Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator6Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator5, renderView1)

# hide data in view
Hide(pythonCalculator6, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator7 = PythonCalculator(registrationName='PythonCalculator7', Input=output_conf_00pvtu)
pythonCalculator7.Expression = ''

# Properties modified on pythonCalculator7
pythonCalculator7.Expression = "gradient(inputs[0].PointData['u_31'])"
pythonCalculator7.ArrayName = 'u_i31'
pythonCalculator7.CopyArrays = 0

# show data in view
pythonCalculator7Display = Show(pythonCalculator7, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator7Display.Representation = 'Surface'
pythonCalculator7Display.ColorArrayName = [None, '']
pythonCalculator7Display.SelectTCoordArray = 'None'
pythonCalculator7Display.SelectNormalArray = 'None'
pythonCalculator7Display.SelectTangentArray = 'None'
pythonCalculator7Display.OSPRayScaleArray = 'u_i31'
pythonCalculator7Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator7Display.SelectOrientationVectors = 'None'
pythonCalculator7Display.ScaleFactor = 12.0
pythonCalculator7Display.SelectScaleArray = 'None'
pythonCalculator7Display.GlyphType = 'Arrow'
pythonCalculator7Display.GlyphTableIndexArray = 'None'
pythonCalculator7Display.GaussianRadius = 0.6
pythonCalculator7Display.SetScaleArray = ['POINTS', 'u_i31']
pythonCalculator7Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator7Display.OpacityArray = ['POINTS', 'u_i31']
pythonCalculator7Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator7Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator7Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator7Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator7Display.OpacityArrayName = ['POINTS', 'u_i31']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator7Display.ScaleTransferFunction.Points = [-0.06232633363632929, 0.0, 0.5, 0.0, 0.06139125142778669, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator7Display.OpacityTransferFunction.Points = [-0.06232633363632929, 0.0, 0.5, 0.0, 0.06139125142778669, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator7Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator7Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator7Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator7Display.DataAxesGrid.XTitleBold = 1
pythonCalculator7Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator7Display.DataAxesGrid.YTitleBold = 1
pythonCalculator7Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator7Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator7Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator7Display.DataAxesGrid.XLabelBold = 1
pythonCalculator7Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator7Display.DataAxesGrid.YLabelBold = 1
pythonCalculator7Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator7Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator7Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator7, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator8 = PythonCalculator(registrationName='PythonCalculator8', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator8
pythonCalculator8.Expression = "gradient(inputs[0].PointData['u_32'])"
pythonCalculator8.ArrayName = 'u_i32'
pythonCalculator8.CopyArrays = 0

# show data in view
pythonCalculator8Display = Show(pythonCalculator8, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator8Display.Representation = 'Surface'
pythonCalculator8Display.ColorArrayName = [None, '']
pythonCalculator8Display.SelectTCoordArray = 'None'
pythonCalculator8Display.SelectNormalArray = 'None'
pythonCalculator8Display.SelectTangentArray = 'None'
pythonCalculator8Display.OSPRayScaleArray = 'u_i32'
pythonCalculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator8Display.SelectOrientationVectors = 'None'
pythonCalculator8Display.ScaleFactor = 12.0
pythonCalculator8Display.SelectScaleArray = 'None'
pythonCalculator8Display.GlyphType = 'Arrow'
pythonCalculator8Display.GlyphTableIndexArray = 'None'
pythonCalculator8Display.GaussianRadius = 0.6
pythonCalculator8Display.SetScaleArray = ['POINTS', 'u_i32']
pythonCalculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator8Display.OpacityArray = ['POINTS', 'u_i32']
pythonCalculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator8Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator8Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator8Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator8Display.OpacityArrayName = ['POINTS', 'u_i32']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator8Display.ScaleTransferFunction.Points = [-0.043398284912109376, 0.0, 0.5, 0.0, 0.043039149329775865, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator8Display.OpacityTransferFunction.Points = [-0.043398284912109376, 0.0, 0.5, 0.0, 0.043039149329775865, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator8Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator8Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator8Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator8Display.DataAxesGrid.XTitleBold = 1
pythonCalculator8Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator8Display.DataAxesGrid.YTitleBold = 1
pythonCalculator8Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator8Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator8Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator8Display.DataAxesGrid.XLabelBold = 1
pythonCalculator8Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator8Display.DataAxesGrid.YLabelBold = 1
pythonCalculator8Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator8Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator8Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator8, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator9 = PythonCalculator(registrationName='PythonCalculator9', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator9
pythonCalculator9.Expression = "gradient(inputs[0].PointData['u_33'])"
pythonCalculator9.ArrayName = 'u_i33'
pythonCalculator9.CopyArrays = 0

# show data in view
pythonCalculator9Display = Show(pythonCalculator9, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator9Display.Representation = 'Surface'
pythonCalculator9Display.ColorArrayName = [None, '']
pythonCalculator9Display.SelectTCoordArray = 'None'
pythonCalculator9Display.SelectNormalArray = 'None'
pythonCalculator9Display.SelectTangentArray = 'None'
pythonCalculator9Display.OSPRayScaleArray = 'u_i33'
pythonCalculator9Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator9Display.SelectOrientationVectors = 'None'
pythonCalculator9Display.ScaleFactor = 12.0
pythonCalculator9Display.SelectScaleArray = 'None'
pythonCalculator9Display.GlyphType = 'Arrow'
pythonCalculator9Display.GlyphTableIndexArray = 'None'
pythonCalculator9Display.GaussianRadius = 0.6
pythonCalculator9Display.SetScaleArray = ['POINTS', 'u_i33']
pythonCalculator9Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator9Display.OpacityArray = ['POINTS', 'u_i33']
pythonCalculator9Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator9Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator9Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator9Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator9Display.OpacityArrayName = ['POINTS', 'u_i33']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator9Display.ScaleTransferFunction.Points = [-0.26257869175502235, 0.0, 0.5, 0.0, 0.2615699018750872, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator9Display.OpacityTransferFunction.Points = [-0.26257869175502235, 0.0, 0.5, 0.0, 0.2615699018750872, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator9Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator9Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator9Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator9Display.DataAxesGrid.XTitleBold = 1
pythonCalculator9Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator9Display.DataAxesGrid.YTitleBold = 1
pythonCalculator9Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator9Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator9Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator9Display.DataAxesGrid.XLabelBold = 1
pythonCalculator9Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator9Display.DataAxesGrid.YLabelBold = 1
pythonCalculator9Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator9Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator9Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator10 = PythonCalculator(registrationName='PythonCalculator10', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator10
pythonCalculator10.Expression = "gradient(inputs[0].PointData['v_11'])"
pythonCalculator10.ArrayName = 'v_i11'
pythonCalculator10.CopyArrays = 0

# show data in view
pythonCalculator10Display = Show(pythonCalculator10, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator10Display.Representation = 'Surface'
pythonCalculator10Display.ColorArrayName = [None, '']
pythonCalculator10Display.SelectTCoordArray = 'None'
pythonCalculator10Display.SelectNormalArray = 'None'
pythonCalculator10Display.SelectTangentArray = 'None'
pythonCalculator10Display.OSPRayScaleArray = 'v_i11'
pythonCalculator10Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator10Display.SelectOrientationVectors = 'None'
pythonCalculator10Display.ScaleFactor = 12.0
pythonCalculator10Display.SelectScaleArray = 'None'
pythonCalculator10Display.GlyphType = 'Arrow'
pythonCalculator10Display.GlyphTableIndexArray = 'None'
pythonCalculator10Display.GaussianRadius = 0.6
pythonCalculator10Display.SetScaleArray = ['POINTS', 'v_i11']
pythonCalculator10Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator10Display.OpacityArray = ['POINTS', 'v_i11']
pythonCalculator10Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator10Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator10Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator10Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator10Display.OpacityArrayName = ['POINTS', 'v_i11']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator10Display.ScaleTransferFunction.Points = [-0.038501094636462986, 0.0, 0.5, 0.0, 0.03864783105396089, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator10Display.OpacityTransferFunction.Points = [-0.038501094636462986, 0.0, 0.5, 0.0, 0.03864783105396089, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator10Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator10Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator10Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator10Display.DataAxesGrid.XTitleBold = 1
pythonCalculator10Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator10Display.DataAxesGrid.YTitleBold = 1
pythonCalculator10Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator10Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator10Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator10Display.DataAxesGrid.XLabelBold = 1
pythonCalculator10Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator10Display.DataAxesGrid.YLabelBold = 1
pythonCalculator10Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator10Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator10Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator9, renderView1)

# hide data in view
Hide(pythonCalculator10, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator11 = PythonCalculator(registrationName='PythonCalculator11', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator11
pythonCalculator11.Expression = "gradient(inputs[0].PointData['v_12'])"
pythonCalculator11.ArrayName = 'v_i12'
pythonCalculator11.CopyArrays = 0

# show data in view
pythonCalculator11Display = Show(pythonCalculator11, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator11Display.Representation = 'Surface'
pythonCalculator11Display.ColorArrayName = [None, '']
pythonCalculator11Display.SelectTCoordArray = 'None'
pythonCalculator11Display.SelectNormalArray = 'None'
pythonCalculator11Display.SelectTangentArray = 'None'
pythonCalculator11Display.OSPRayScaleArray = 'v_i12'
pythonCalculator11Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator11Display.SelectOrientationVectors = 'None'
pythonCalculator11Display.ScaleFactor = 12.0
pythonCalculator11Display.SelectScaleArray = 'None'
pythonCalculator11Display.GlyphType = 'Arrow'
pythonCalculator11Display.GlyphTableIndexArray = 'None'
pythonCalculator11Display.GaussianRadius = 0.6
pythonCalculator11Display.SetScaleArray = ['POINTS', 'v_i12']
pythonCalculator11Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator11Display.OpacityArray = ['POINTS', 'v_i12']
pythonCalculator11Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator11Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator11Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator11Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator11Display.OpacityArrayName = ['POINTS', 'v_i12']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator11Display.ScaleTransferFunction.Points = [-0.030060214088076638, 0.0, 0.5, 0.0, 0.029440116882324223, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator11Display.OpacityTransferFunction.Points = [-0.030060214088076638, 0.0, 0.5, 0.0, 0.029440116882324223, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator11Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator11Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator11Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator11Display.DataAxesGrid.XTitleBold = 1
pythonCalculator11Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator11Display.DataAxesGrid.YTitleBold = 1
pythonCalculator11Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator11Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator11Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator11Display.DataAxesGrid.XLabelBold = 1
pythonCalculator11Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator11Display.DataAxesGrid.YLabelBold = 1
pythonCalculator11Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator11Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator11Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator11, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator12 = PythonCalculator(registrationName='PythonCalculator12', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator12
pythonCalculator12.Expression = "gradient(inputs[0].PointData['v_13'])"
pythonCalculator12.ArrayName = 'v_i13'
pythonCalculator12.CopyArrays = 0

# show data in view
pythonCalculator12Display = Show(pythonCalculator12, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator12Display.Representation = 'Surface'
pythonCalculator12Display.ColorArrayName = [None, '']
pythonCalculator12Display.SelectTCoordArray = 'None'
pythonCalculator12Display.SelectNormalArray = 'None'
pythonCalculator12Display.SelectTangentArray = 'None'
pythonCalculator12Display.OSPRayScaleArray = 'v_i13'
pythonCalculator12Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator12Display.SelectOrientationVectors = 'None'
pythonCalculator12Display.ScaleFactor = 12.0
pythonCalculator12Display.SelectScaleArray = 'None'
pythonCalculator12Display.GlyphType = 'Arrow'
pythonCalculator12Display.GlyphTableIndexArray = 'None'
pythonCalculator12Display.GaussianRadius = 0.6
pythonCalculator12Display.SetScaleArray = ['POINTS', 'v_i13']
pythonCalculator12Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator12Display.OpacityArray = ['POINTS', 'v_i13']
pythonCalculator12Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator12Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator12Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator12Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator12Display.OpacityArrayName = ['POINTS', 'v_i13']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator12Display.ScaleTransferFunction.Points = [-0.16150279612768265, 0.0, 0.5, 0.0, 0.16298940749395463, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator12Display.OpacityTransferFunction.Points = [-0.16150279612768265, 0.0, 0.5, 0.0, 0.16298940749395463, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator12Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator12Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator12Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator12Display.DataAxesGrid.XTitleBold = 1
pythonCalculator12Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator12Display.DataAxesGrid.YTitleBold = 1
pythonCalculator12Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator12Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator12Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator12Display.DataAxesGrid.XLabelBold = 1
pythonCalculator12Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator12Display.DataAxesGrid.YLabelBold = 1
pythonCalculator12Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator12Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator12Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator12, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator13 = PythonCalculator(registrationName='PythonCalculator13', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator13
pythonCalculator13.Expression = "gradient(inputs[0].PointData['v_21'])"
pythonCalculator13.ArrayName = 'v_i21'
pythonCalculator13.CopyArrays = 0

# show data in view
pythonCalculator13Display = Show(pythonCalculator13, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator13Display.Representation = 'Surface'
pythonCalculator13Display.ColorArrayName = [None, '']
pythonCalculator13Display.SelectTCoordArray = 'None'
pythonCalculator13Display.SelectNormalArray = 'None'
pythonCalculator13Display.SelectTangentArray = 'None'
pythonCalculator13Display.OSPRayScaleArray = 'v_i21'
pythonCalculator13Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator13Display.SelectOrientationVectors = 'None'
pythonCalculator13Display.ScaleFactor = 12.0
pythonCalculator13Display.SelectScaleArray = 'None'
pythonCalculator13Display.GlyphType = 'Arrow'
pythonCalculator13Display.GlyphTableIndexArray = 'None'
pythonCalculator13Display.GaussianRadius = 0.6
pythonCalculator13Display.SetScaleArray = ['POINTS', 'v_i21']
pythonCalculator13Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator13Display.OpacityArray = ['POINTS', 'v_i21']
pythonCalculator13Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator13Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator13Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator13Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator13Display.OpacityArrayName = ['POINTS', 'v_i21']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator13Display.ScaleTransferFunction.Points = [-0.02621444520496187, 0.0, 0.5, 0.0, 0.02675582340785436, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator13Display.OpacityTransferFunction.Points = [-0.02621444520496187, 0.0, 0.5, 0.0, 0.02675582340785436, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator13Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator13Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator13Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator13Display.DataAxesGrid.XTitleBold = 1
pythonCalculator13Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator13Display.DataAxesGrid.YTitleBold = 1
pythonCalculator13Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator13Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator13Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator13Display.DataAxesGrid.XLabelBold = 1
pythonCalculator13Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator13Display.DataAxesGrid.YLabelBold = 1
pythonCalculator13Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator13Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator13Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator13, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator14 = PythonCalculator(registrationName='PythonCalculator14', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator14
pythonCalculator14.Expression = "gradient(inputs[0].PointData['v_22'])"
pythonCalculator14.ArrayName = 'v_i22'
pythonCalculator14.CopyArrays = 0

# show data in view
pythonCalculator14Display = Show(pythonCalculator14, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator14Display.Representation = 'Surface'
pythonCalculator14Display.ColorArrayName = [None, '']
pythonCalculator14Display.SelectTCoordArray = 'None'
pythonCalculator14Display.SelectNormalArray = 'None'
pythonCalculator14Display.SelectTangentArray = 'None'
pythonCalculator14Display.OSPRayScaleArray = 'v_i22'
pythonCalculator14Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator14Display.SelectOrientationVectors = 'None'
pythonCalculator14Display.ScaleFactor = 12.0
pythonCalculator14Display.SelectScaleArray = 'None'
pythonCalculator14Display.GlyphType = 'Arrow'
pythonCalculator14Display.GlyphTableIndexArray = 'None'
pythonCalculator14Display.GaussianRadius = 0.6
pythonCalculator14Display.SetScaleArray = ['POINTS', 'v_i22']
pythonCalculator14Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator14Display.OpacityArray = ['POINTS', 'v_i22']
pythonCalculator14Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator14Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator14Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator14Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator14Display.OpacityArrayName = ['POINTS', 'v_i22']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator14Display.ScaleTransferFunction.Points = [-0.013164440790812176, 0.0, 0.5, 0.0, 0.013173036348252069, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator14Display.OpacityTransferFunction.Points = [-0.013164440790812176, 0.0, 0.5, 0.0, 0.013173036348252069, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator14Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator14Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator14Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator14Display.DataAxesGrid.XTitleBold = 1
pythonCalculator14Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator14Display.DataAxesGrid.YTitleBold = 1
pythonCalculator14Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator14Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator14Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator14Display.DataAxesGrid.XLabelBold = 1
pythonCalculator14Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator14Display.DataAxesGrid.YLabelBold = 1
pythonCalculator14Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator14Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator14Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator15 = PythonCalculator(registrationName='PythonCalculator15', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator15
pythonCalculator15.Expression = "gradient(inputs[0].PointData['v_23'])"
pythonCalculator15.ArrayName = 'v_i23'
pythonCalculator15.CopyArrays = 0

# show data in view
pythonCalculator15Display = Show(pythonCalculator15, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator15Display.Representation = 'Surface'
pythonCalculator15Display.ColorArrayName = [None, '']
pythonCalculator15Display.SelectTCoordArray = 'None'
pythonCalculator15Display.SelectNormalArray = 'None'
pythonCalculator15Display.SelectTangentArray = 'None'
pythonCalculator15Display.OSPRayScaleArray = 'v_i23'
pythonCalculator15Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator15Display.SelectOrientationVectors = 'None'
pythonCalculator15Display.ScaleFactor = 12.0
pythonCalculator15Display.SelectScaleArray = 'None'
pythonCalculator15Display.GlyphType = 'Arrow'
pythonCalculator15Display.GlyphTableIndexArray = 'None'
pythonCalculator15Display.GaussianRadius = 0.6
pythonCalculator15Display.SetScaleArray = ['POINTS', 'v_i23']
pythonCalculator15Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator15Display.OpacityArray = ['POINTS', 'v_i23']
pythonCalculator15Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator15Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator15Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator15Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator15Display.OpacityArrayName = ['POINTS', 'v_i23']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator15Display.ScaleTransferFunction.Points = [-0.2046630041939872, 0.0, 0.5, 0.0, 0.20455077943347755, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator15Display.OpacityTransferFunction.Points = [-0.2046630041939872, 0.0, 0.5, 0.0, 0.20455077943347755, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator15Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator15Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator15Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator15Display.DataAxesGrid.XTitleBold = 1
pythonCalculator15Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator15Display.DataAxesGrid.YTitleBold = 1
pythonCalculator15Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator15Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator15Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator15Display.DataAxesGrid.XLabelBold = 1
pythonCalculator15Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator15Display.DataAxesGrid.YLabelBold = 1
pythonCalculator15Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator15Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator15Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator16 = PythonCalculator(registrationName='PythonCalculator16', Input=output_conf_00pvtu)


# hide data in view
Hide(pythonCalculator15, renderView1)

# hide data in view
Hide(pythonCalculator14, renderView1)

# Properties modified on pythonCalculator16
pythonCalculator16.Expression = "gradient(inputs[0].PointData['v_31'])"
pythonCalculator16.ArrayName = 'v_i31'
pythonCalculator16.CopyArrays = 0

# show data in view
pythonCalculator16Display = Show(pythonCalculator16, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator16Display.Representation = 'Surface'
pythonCalculator16Display.ColorArrayName = [None, '']
pythonCalculator16Display.SelectTCoordArray = 'None'
pythonCalculator16Display.SelectNormalArray = 'None'
pythonCalculator16Display.SelectTangentArray = 'None'
pythonCalculator16Display.OSPRayScaleArray = 'v_i31'
pythonCalculator16Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator16Display.SelectOrientationVectors = 'None'
pythonCalculator16Display.ScaleFactor = 12.0
pythonCalculator16Display.SelectScaleArray = 'None'
pythonCalculator16Display.GlyphType = 'Arrow'
pythonCalculator16Display.GlyphTableIndexArray = 'None'
pythonCalculator16Display.GaussianRadius = 0.6
pythonCalculator16Display.SetScaleArray = ['POINTS', 'v_i31']
pythonCalculator16Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator16Display.OpacityArray = ['POINTS', 'v_i31']
pythonCalculator16Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator16Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator16Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator16Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator16Display.OpacityArrayName = ['POINTS', 'v_i31']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator16Display.ScaleTransferFunction.Points = [-0.04853589194161552, 0.0, 0.5, 0.0, 0.04779706228347051, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator16Display.OpacityTransferFunction.Points = [-0.04853589194161552, 0.0, 0.5, 0.0, 0.04779706228347051, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator16Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator16Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator16Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator16Display.DataAxesGrid.XTitleBold = 1
pythonCalculator16Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator16Display.DataAxesGrid.YTitleBold = 1
pythonCalculator16Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator16Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator16Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator16Display.DataAxesGrid.XLabelBold = 1
pythonCalculator16Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator16Display.DataAxesGrid.YLabelBold = 1
pythonCalculator16Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator16Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator16Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator16, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator17 = PythonCalculator(registrationName='PythonCalculator17', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator17
pythonCalculator17.Expression = "gradient(inputs[0].PointData['v_32'])"
pythonCalculator17.ArrayName = 'v_i32'
pythonCalculator17.CopyArrays = 0

# show data in view
pythonCalculator17Display = Show(pythonCalculator17, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator17Display.Representation = 'Surface'
pythonCalculator17Display.ColorArrayName = [None, '']
pythonCalculator17Display.SelectTCoordArray = 'None'
pythonCalculator17Display.SelectNormalArray = 'None'
pythonCalculator17Display.SelectTangentArray = 'None'
pythonCalculator17Display.OSPRayScaleArray = 'u_i32'
pythonCalculator17Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator17Display.SelectOrientationVectors = 'None'
pythonCalculator17Display.ScaleFactor = 12.0
pythonCalculator17Display.SelectScaleArray = 'None'
pythonCalculator17Display.GlyphType = 'Arrow'
pythonCalculator17Display.GlyphTableIndexArray = 'None'
pythonCalculator17Display.GaussianRadius = 0.6
pythonCalculator17Display.SetScaleArray = ['POINTS', 'v_i32']
pythonCalculator17Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator17Display.OpacityArray = ['POINTS', 'v_i32']
pythonCalculator17Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator17Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator17Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator17Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator17Display.OpacityArrayName = ['POINTS', 'v_i32']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator17Display.ScaleTransferFunction.Points = [-0.03372589292980376, 0.0, 0.5, 0.0, 0.033475853147960845, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator17Display.OpacityTransferFunction.Points = [-0.03372589292980376, 0.0, 0.5, 0.0, 0.033475853147960845, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator17Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator17Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator17Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator17Display.DataAxesGrid.XTitleBold = 1
pythonCalculator17Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator17Display.DataAxesGrid.YTitleBold = 1
pythonCalculator17Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator17Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator17Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator17Display.DataAxesGrid.XLabelBold = 1
pythonCalculator17Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator17Display.DataAxesGrid.YLabelBold = 1
pythonCalculator17Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator17Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator17Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator17, renderView1)

# set active source
SetActiveSource(output_conf_00pvtu)

# create a new 'Python Calculator'
pythonCalculator18 = PythonCalculator(registrationName='PythonCalculator18', Input=output_conf_00pvtu)

# Properties modified on pythonCalculator18
pythonCalculator18.Expression = "gradient(inputs[0].PointData['v_33'])"
pythonCalculator18.ArrayName = 'v_i33'
pythonCalculator18.CopyArrays = 0

# show data in view
pythonCalculator18Display = Show(pythonCalculator18, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator18Display.Representation = 'Surface'
pythonCalculator18Display.ColorArrayName = [None, '']
pythonCalculator18Display.SelectTCoordArray = 'None'
pythonCalculator18Display.SelectNormalArray = 'None'
pythonCalculator18Display.SelectTangentArray = 'None'
pythonCalculator18Display.OSPRayScaleArray = 'u_i33'
pythonCalculator18Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator18Display.SelectOrientationVectors = 'None'
pythonCalculator18Display.ScaleFactor = 12.0
pythonCalculator18Display.SelectScaleArray = 'None'
pythonCalculator18Display.GlyphType = 'Arrow'
pythonCalculator18Display.GlyphTableIndexArray = 'None'
pythonCalculator18Display.GaussianRadius = 0.6
pythonCalculator18Display.SetScaleArray = ['POINTS', 'u_i33']
pythonCalculator18Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator18Display.OpacityArray = ['POINTS', 'u_i33']
pythonCalculator18Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator18Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator18Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator18Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator18Display.OpacityArrayName = ['POINTS', 'u_i33']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator18Display.ScaleTransferFunction.Points = [-0.26257869175502235, 0.0, 0.5, 0.0, 0.2615699018750872, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator18Display.OpacityTransferFunction.Points = [-0.26257869175502235, 0.0, 0.5, 0.0, 0.2615699018750872, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator18Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator18Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator18Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator18Display.DataAxesGrid.XTitleBold = 1
pythonCalculator18Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator18Display.DataAxesGrid.YTitleBold = 1
pythonCalculator18Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator18Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator18Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator18Display.DataAxesGrid.XLabelBold = 1
pythonCalculator18Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator18Display.DataAxesGrid.YLabelBold = 1
pythonCalculator18Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator18Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator18Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(pythonCalculator18, renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2079, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 309.4424729524235]
renderView1.CameraParallelScale = 80.08960536370884

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
