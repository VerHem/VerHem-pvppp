# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
mergeVectorComponents2 = FindSource('MergeVectorComponents2')

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=mergeVectorComponents2)
pythonCalculator1.Expression = ''

# find source
calculator4 = FindSource('Calculator4')

# find source
calculator3 = FindSource('Calculator3')

# find source
calculator6 = FindSource('Calculator6')

# find source
calculator5 = FindSource('Calculator5')

# find source
calculator2 = FindSource('Calculator2')

# find source
setup_conf_00pvtu = FindSource('setup_conf_00.pvtu')

# Properties modified on setup_conf_00pvtu
# setup_conf_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']


# find source
mergeVectorComponents1 = FindSource('MergeVectorComponents1')

# find source
calculator1 = FindSource('Calculator1')

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = "gradient(inputs[0].PointData['m1'])"
pythonCalculator1.ArrayName = 'm_i1'
pythonCalculator1.CopyArrays = 0

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
pythonCalculator1Display = Show(pythonCalculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
# pythonCalculator1Display.Representation = 'Surface'
# pythonCalculator1Display.ColorArrayName = [None, '']
# pythonCalculator1Display.SelectTCoordArray = 'None'
# pythonCalculator1Display.SelectNormalArray = 'None'
# pythonCalculator1Display.SelectTangentArray = 'None'
# pythonCalculator1Display.OSPRayScaleArray = 'm_i1'
# pythonCalculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# pythonCalculator1Display.SelectOrientationVectors = 'None'
# pythonCalculator1Display.ScaleFactor = 3.0
# pythonCalculator1Display.SelectScaleArray = 'None'
# pythonCalculator1Display.GlyphType = 'Arrow'
# pythonCalculator1Display.GlyphTableIndexArray = 'None'
# pythonCalculator1Display.GaussianRadius = 0.15
# pythonCalculator1Display.SetScaleArray = ['POINTS', 'm_i1']
# pythonCalculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
# pythonCalculator1Display.OpacityArray = ['POINTS', 'm_i1']
# pythonCalculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
# pythonCalculator1Display.DataAxesGrid = 'GridAxesRepresentation'
# pythonCalculator1Display.PolarAxes = 'PolarAxesRepresentation'
# pythonCalculator1Display.ScalarOpacityUnitDistance = 1.447513849627623
# pythonCalculator1Display.OpacityArrayName = ['POINTS', 'm_i1']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# pythonCalculator1Display.ScaleTransferFunction.Points = [-0.536063460914585, 0.0, 0.5, 0.0, 0.536061490676547, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# pythonCalculator1Display.OpacityTransferFunction.Points = [-0.536063460914585, 0.0, 0.5, 0.0, 0.536061490676547, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# pythonCalculator1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# pythonCalculator1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# pythonCalculator1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# pythonCalculator1Display.DataAxesGrid.XTitleBold = 1
# pythonCalculator1Display.DataAxesGrid.XTitleFontSize = 24
# pythonCalculator1Display.DataAxesGrid.YTitleBold = 1
# pythonCalculator1Display.DataAxesGrid.YTitleFontSize = 24
# pythonCalculator1Display.DataAxesGrid.ZTitleBold = 1
# pythonCalculator1Display.DataAxesGrid.ZTitleFontSize = 23
# pythonCalculator1Display.DataAxesGrid.XLabelBold = 1
# pythonCalculator1Display.DataAxesGrid.XLabelFontSize = 17
# pythonCalculator1Display.DataAxesGrid.YLabelBold = 1
# pythonCalculator1Display.DataAxesGrid.YLabelFontSize = 17
# pythonCalculator1Display.DataAxesGrid.ZLabelBold = 1
# pythonCalculator1Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(mergeVectorComponents2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
# ColorBy(pythonCalculator1Display, ('POINTS', 'm_i1', 'Magnitude'))

# # rescale color and/or opacity maps used to include current data range
# pythonCalculator1Display.RescaleTransferFunctionToDataRange(True, False)

# # show color bar/color legend
# pythonCalculator1Display.SetScalarBarVisibility(renderView1, True)

# # get color transfer function/color map for 'm_i1'
# m_i1LUT = GetColorTransferFunction('m_i1')
# m_i1LUT.RGBPoints = [0.0005542463744733191, 0.231373, 0.298039, 0.752941, 0.268322331235521, 0.865003, 0.865003, 0.865003, 0.5360904160965687, 0.705882, 0.0156863, 0.14902]
# m_i1LUT.ScalarRangeInitialized = 1.0

# # get opacity transfer function/opacity map for 'm_i1'
# m_i1PWF = GetOpacityTransferFunction('m_i1')
# m_i1PWF.Points = [0.0005542463744733191, 0.0, 0.5, 0.0, 0.5360904160965687, 1.0, 0.5, 0.0]
# m_i1PWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(mergeVectorComponents2)

# get color transfer function/color map for 'n3'
# n3LUT = GetColorTransferFunction('n3')
# n3LUT.RGBPoints = [-1.0839533278298874, 0.231373, 0.298039, 0.752941, -3.5201373327353735e-07, 0.865003, 0.865003, 0.865003, 1.0839526238024209, 0.705882, 0.0156863, 0.14902]
# n3LUT.ScalarRangeInitialized = 1.0

# # get opacity transfer function/opacity map for 'n3'
# n3PWF = GetOpacityTransferFunction('n3')
# n3PWF.Points = [-1.0839533278298874, 0.0, 0.5, 0.0, 1.0839526238024209, 1.0, 0.5, 0.0]
# n3PWF.ScalarRangeInitialized = 1

# get display properties
mergeVectorComponents2Display = GetDisplayProperties(mergeVectorComponents2, view=renderView1)

# create a new 'Python Calculator'
pythonCalculator2 = PythonCalculator(registrationName='PythonCalculator2', Input=mergeVectorComponents2)

# Properties modified on pythonCalculator2
pythonCalculator2.Expression = "gradient(inputs[0].PointData['m2'])"
pythonCalculator2.ArrayName = 'm_i2'
pythonCalculator2.CopyArrays = 0

# show data in view
pythonCalculator2Display = Show(pythonCalculator2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
# pythonCalculator2Display.Representation = 'Surface'
# pythonCalculator2Display.ColorArrayName = [None, '']
# pythonCalculator2Display.SelectTCoordArray = 'None'
# pythonCalculator2Display.SelectNormalArray = 'None'
# pythonCalculator2Display.SelectTangentArray = 'None'
# pythonCalculator2Display.OSPRayScaleArray = 'm_i2'
# pythonCalculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
# pythonCalculator2Display.SelectOrientationVectors = 'None'
# pythonCalculator2Display.ScaleFactor = 3.0
# pythonCalculator2Display.SelectScaleArray = 'None'
# pythonCalculator2Display.GlyphType = 'Arrow'
# pythonCalculator2Display.GlyphTableIndexArray = 'None'
# pythonCalculator2Display.GaussianRadius = 0.15
# pythonCalculator2Display.SetScaleArray = ['POINTS', 'm_i2']
# pythonCalculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
# pythonCalculator2Display.OpacityArray = ['POINTS', 'm_i2']
# pythonCalculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
# pythonCalculator2Display.DataAxesGrid = 'GridAxesRepresentation'
# pythonCalculator2Display.PolarAxes = 'PolarAxesRepresentation'
# pythonCalculator2Display.ScalarOpacityUnitDistance = 1.447513849627623
# pythonCalculator2Display.OpacityArrayName = ['POINTS', 'm_i2']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# pythonCalculator2Display.ScaleTransferFunction.Points = [-0.12129483215471479, 0.0, 0.5, 0.0, 0.12129475535151363, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# pythonCalculator2Display.OpacityTransferFunction.Points = [-0.12129483215471479, 0.0, 0.5, 0.0, 0.12129475535151363, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# pythonCalculator2Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# pythonCalculator2Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# pythonCalculator2Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# pythonCalculator2Display.DataAxesGrid.XTitleBold = 1
# pythonCalculator2Display.DataAxesGrid.XTitleFontSize = 24
# pythonCalculator2Display.DataAxesGrid.YTitleBold = 1
# pythonCalculator2Display.DataAxesGrid.YTitleFontSize = 24
# pythonCalculator2Display.DataAxesGrid.ZTitleBold = 1
# pythonCalculator2Display.DataAxesGrid.ZTitleFontSize = 23
# pythonCalculator2Display.DataAxesGrid.XLabelBold = 1
# pythonCalculator2Display.DataAxesGrid.XLabelFontSize = 17
# pythonCalculator2Display.DataAxesGrid.YLabelBold = 1
# pythonCalculator2Display.DataAxesGrid.YLabelFontSize = 17
# pythonCalculator2Display.DataAxesGrid.ZLabelBold = 1
# pythonCalculator2Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(mergeVectorComponents2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
# ColorBy(pythonCalculator2Display, ('POINTS', 'm_i2', 'Magnitude'))

# # rescale color and/or opacity maps used to include current data range
# pythonCalculator2Display.RescaleTransferFunctionToDataRange(True, False)

# # show color bar/color legend
# pythonCalculator2Display.SetScalarBarVisibility(renderView1, True)

# # get color transfer function/color map for 'm_i2'
# m_i2LUT = GetColorTransferFunction('m_i2')
# m_i2LUT.RGBPoints = [0.00039249406871408733, 0.231373, 0.298039, 0.752941, 0.2602009415895346, 0.865003, 0.865003, 0.865003, 0.5200093891103551, 0.705882, 0.0156863, 0.14902]
# m_i2LUT.ScalarRangeInitialized = 1.0

# # get opacity transfer function/opacity map for 'm_i2'
# m_i2PWF = GetOpacityTransferFunction('m_i2')
# m_i2PWF.Points = [0.00039249406871408733, 0.0, 0.5, 0.0, 0.5200093891103551, 1.0, 0.5, 0.0]
# m_i2PWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(mergeVectorComponents2)

# create a new 'Python Calculator'
pythonCalculator3 = PythonCalculator(registrationName='PythonCalculator3', Input=mergeVectorComponents2)
pythonCalculator3.Expression = ''

# Properties modified on pythonCalculator3
pythonCalculator3.Expression = "gradient(inputs[0].PointData['m3'])"
pythonCalculator3.ArrayName = 'm_i3'
pythonCalculator3.CopyArrays = 0

# show data in view
pythonCalculator3Display = Show(pythonCalculator3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
# pythonCalculator3Display.Representation = 'Surface'
# pythonCalculator3Display.ColorArrayName = [None, '']
# pythonCalculator3Display.SelectTCoordArray = 'None'
# pythonCalculator3Display.SelectNormalArray = 'None'
# pythonCalculator3Display.SelectTangentArray = 'None'
# pythonCalculator3Display.OSPRayScaleArray = 'm_i3'
# pythonCalculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
# pythonCalculator3Display.SelectOrientationVectors = 'None'
# pythonCalculator3Display.ScaleFactor = 3.0
# pythonCalculator3Display.SelectScaleArray = 'None'
# pythonCalculator3Display.GlyphType = 'Arrow'
# pythonCalculator3Display.GlyphTableIndexArray = 'None'
# pythonCalculator3Display.GaussianRadius = 0.15
# pythonCalculator3Display.SetScaleArray = ['POINTS', 'm_i3']
# pythonCalculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
# pythonCalculator3Display.OpacityArray = ['POINTS', 'm_i3']
# pythonCalculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
# pythonCalculator3Display.DataAxesGrid = 'GridAxesRepresentation'
# pythonCalculator3Display.PolarAxes = 'PolarAxesRepresentation'
# pythonCalculator3Display.ScalarOpacityUnitDistance = 1.447513849627623
# pythonCalculator3Display.OpacityArrayName = ['POINTS', 'm_i3']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# pythonCalculator3Display.ScaleTransferFunction.Points = [-0.09027627457392504, 0.0, 0.5, 0.0, 0.12470934392396624, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# pythonCalculator3Display.OpacityTransferFunction.Points = [-0.09027627457392504, 0.0, 0.5, 0.0, 0.12470934392396624, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# pythonCalculator3Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# pythonCalculator3Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# pythonCalculator3Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# pythonCalculator3Display.DataAxesGrid.XTitleBold = 1
# pythonCalculator3Display.DataAxesGrid.XTitleFontSize = 24
# pythonCalculator3Display.DataAxesGrid.YTitleBold = 1
# pythonCalculator3Display.DataAxesGrid.YTitleFontSize = 24
# pythonCalculator3Display.DataAxesGrid.ZTitleBold = 1
# pythonCalculator3Display.DataAxesGrid.ZTitleFontSize = 23
# pythonCalculator3Display.DataAxesGrid.XLabelBold = 1
# pythonCalculator3Display.DataAxesGrid.XLabelFontSize = 17
# pythonCalculator3Display.DataAxesGrid.YLabelBold = 1
# pythonCalculator3Display.DataAxesGrid.YLabelFontSize = 17
# pythonCalculator3Display.DataAxesGrid.ZLabelBold = 1
# pythonCalculator3Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(mergeVectorComponents2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
# ColorBy(pythonCalculator3Display, ('POINTS', 'm_i3', 'Magnitude'))

# # rescale color and/or opacity maps used to include current data range
# pythonCalculator3Display.RescaleTransferFunctionToDataRange(True, False)

# # show color bar/color legend
# pythonCalculator3Display.SetScalarBarVisibility(renderView1, True)

# # get color transfer function/color map for 'm_i3'
# m_i3LUT = GetColorTransferFunction('m_i3')
# m_i3LUT.RGBPoints = [0.0020869059995762347, 0.231373, 0.298039, 0.752941, 0.27061569434313576, 0.865003, 0.865003, 0.865003, 0.5391444826866953, 0.705882, 0.0156863, 0.14902]
# m_i3LUT.ScalarRangeInitialized = 1.0

# # get opacity transfer function/opacity map for 'm_i3'
# m_i3PWF = GetOpacityTransferFunction('m_i3')
# m_i3PWF.Points = [0.0020869059995762347, 0.0, 0.5, 0.0, 0.5391444826866953, 1.0, 0.5, 0.0]
# m_i3PWF.ScalarRangeInitialized = 1

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1939, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 100.38195644853695]
renderView1.CameraParallelScale = 25.98076211353316

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
