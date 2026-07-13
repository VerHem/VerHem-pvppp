# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
pythonCalculator19 = FindSource('PythonCalculator19')

# set active source
# SetActiveSource(pythonCalculator19)

# find source
pythonCalculator20 = FindSource('PythonCalculator20')

# set active source
# SetActiveSource(pythonCalculator20)

# find source
pythonCalculator21 = FindSource('PythonCalculator21')

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pythonCalculator19, pythonCalculator20, pythonCalculator21])

# find source
pythonCalculator4 = FindSource('PythonCalculator4')

# find source
pythonCalculator5 = FindSource('PythonCalculator5')

# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# find source
pythonCalculator6 = FindSource('PythonCalculator6')

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

# find source
pythonCalculator8 = FindSource('PythonCalculator8')

# find source
pythonCalculator9 = FindSource('PythonCalculator9')

# get active view
renderView2 = GetActiveViewOrCreate('RenderView')

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Surface'
appendAttributes1Display.ColorArrayName = [None, '']
appendAttributes1Display.SelectTCoordArray = 'None'
appendAttributes1Display.SelectNormalArray = 'None'
appendAttributes1Display.SelectTangentArray = 'None'
appendAttributes1Display.OSPRayScaleArray = 'SycurrK1'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'None'
appendAttributes1Display.ScaleFactor = 12.0
appendAttributes1Display.SelectScaleArray = 'None'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'None'
appendAttributes1Display.GaussianRadius = 0.6
appendAttributes1Display.SetScaleArray = ['POINTS', 'SycurrK1']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'SycurrK1']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityUnitDistance = 2.5028001676159013
appendAttributes1Display.OpacityArrayName = ['POINTS', 'SycurrK1']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
appendAttributes1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
appendAttributes1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
appendAttributes1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
appendAttributes1Display.DataAxesGrid.XTitleBold = 1
appendAttributes1Display.DataAxesGrid.XTitleFontSize = 24
appendAttributes1Display.DataAxesGrid.YTitleBold = 1
appendAttributes1Display.DataAxesGrid.YTitleFontSize = 24
appendAttributes1Display.DataAxesGrid.ZTitleBold = 1
appendAttributes1Display.DataAxesGrid.ZTitleFontSize = 23
appendAttributes1Display.DataAxesGrid.XLabelBold = 1
appendAttributes1Display.DataAxesGrid.XLabelFontSize = 17
appendAttributes1Display.DataAxesGrid.YLabelBold = 1
appendAttributes1Display.DataAxesGrid.YLabelFontSize = 17
appendAttributes1Display.DataAxesGrid.ZLabelBold = 1
appendAttributes1Display.DataAxesGrid.ZLabelFontSize = 17

# find source
pythonCalculator10 = FindSource('PythonCalculator10')

# find source
pythonCalculator17 = FindSource('PythonCalculator17')

# find source
pythonCalculator16 = FindSource('PythonCalculator16')

# find source
pythonCalculator19 = FindSource('PythonCalculator19')

# find source
pythonCalculator1 = FindSource('PythonCalculator1')

# find source
pythonCalculator7 = FindSource('PythonCalculator7')

# find source
pythonCalculator11 = FindSource('PythonCalculator11')

# find source
pythonCalculator12 = FindSource('PythonCalculator12')

# find source
pythonCalculator13 = FindSource('PythonCalculator13')

# find source
pythonCalculator14 = FindSource('PythonCalculator14')

# find source
pythonCalculator15 = FindSource('PythonCalculator15')

# find source
pythonCalculator18 = FindSource('PythonCalculator18')

# find source
output_conf_00pvtu = FindSource('output_conf_00.pvtu')

# update the view to ensure updated data information
renderView2.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=appendAttributes1)
mergeVectorComponents1.XArray = 'SycurrK1X'
#mergeVectorComponents1.YArray = 'SycurrK1X'
#mergeVectorComponents1.ZArray = 'SycurrK1X'

# Properties modified on mergeVectorComponents1
mergeVectorComponents1.YArray = 'SycurrK1Y'
mergeVectorComponents1.ZArray = 'SycurrK1Z'
mergeVectorComponents1.OutputVectorName = 'SycurrK1'

# show data in view
mergeVectorComponents1Display = Show(mergeVectorComponents1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents1Display.Representation = 'Surface'
mergeVectorComponents1Display.ColorArrayName = [None, '']
mergeVectorComponents1Display.SelectTCoordArray = 'None'
mergeVectorComponents1Display.SelectNormalArray = 'None'
mergeVectorComponents1Display.SelectTangentArray = 'None'
mergeVectorComponents1Display.OSPRayScaleArray = 'SycurrK1'
mergeVectorComponents1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.SelectOrientationVectors = 'None'
mergeVectorComponents1Display.ScaleFactor = 12.0
mergeVectorComponents1Display.SelectScaleArray = 'None'
mergeVectorComponents1Display.GlyphType = 'Arrow'
mergeVectorComponents1Display.GlyphTableIndexArray = 'None'
mergeVectorComponents1Display.GaussianRadius = 0.6
mergeVectorComponents1Display.SetScaleArray = ['POINTS', 'SycurrK1']
mergeVectorComponents1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.OpacityArray = ['POINTS', 'SycurrK1']
mergeVectorComponents1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents1Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents1Display.ScalarOpacityUnitDistance = 2.5028001676159013
mergeVectorComponents1Display.OpacityArrayName = ['POINTS', 'SycurrK1']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents1Display.ScaleTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents1Display.OpacityTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mergeVectorComponents1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
mergeVectorComponents1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
mergeVectorComponents1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
mergeVectorComponents1Display.DataAxesGrid.XTitleBold = 1
mergeVectorComponents1Display.DataAxesGrid.XTitleFontSize = 24
mergeVectorComponents1Display.DataAxesGrid.YTitleBold = 1
mergeVectorComponents1Display.DataAxesGrid.YTitleFontSize = 24
mergeVectorComponents1Display.DataAxesGrid.ZTitleBold = 1
mergeVectorComponents1Display.DataAxesGrid.ZTitleFontSize = 23
mergeVectorComponents1Display.DataAxesGrid.XLabelBold = 1
mergeVectorComponents1Display.DataAxesGrid.XLabelFontSize = 17
mergeVectorComponents1Display.DataAxesGrid.YLabelBold = 1
mergeVectorComponents1Display.DataAxesGrid.YLabelFontSize = 17
mergeVectorComponents1Display.DataAxesGrid.ZLabelBold = 1
mergeVectorComponents1Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
# Hide(appendAttributes1, renderView2)

# update the view to ensure updated data information
# renderView2.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2070, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView2
# renderView2.CameraPosition = [-4.914883380006738, -1.7358159363190553, 309.39856969822534]
# renderView2.CameraViewUp = [-5.242531761370049e-05, 0.999984265987824, 0.0056093696953431705]
# renderView2.CameraParallelScale = 80.08960536370884

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
