# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
pythonCalculator21 = FindSource('PythonCalculator21')

# set active source
SetActiveSource(pythonCalculator21)

# find source
pythonCalculator22 = FindSource('PythonCalculator22')

# set active source
SetActiveSource(pythonCalculator22)

# find source
pythonCalculator20 = FindSource('PythonCalculator20')

# create a new 'Append Attributes'
appendAttributes2 = AppendAttributes(registrationName='AppendAttributes2', Input=[pythonCalculator23, pythonCalculator24, pythonCalculator25])

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
appendAttributes2Display = Show(appendAttributes2, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
appendAttributes2Display.Representation = 'Surface'
appendAttributes2Display.ColorArrayName = [None, '']
appendAttributes2Display.SelectTCoordArray = 'None'
appendAttributes2Display.SelectNormalArray = 'None'
appendAttributes2Display.SelectTangentArray = 'None'
appendAttributes2Display.OSPRayScaleArray = 'currK2'
appendAttributes2Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes2Display.SelectOrientationVectors = 'None'
appendAttributes2Display.ScaleFactor = 12.0
appendAttributes2Display.SelectScaleArray = 'None'
appendAttributes2Display.GlyphType = 'Arrow'
appendAttributes2Display.GlyphTableIndexArray = 'None'
appendAttributes2Display.GaussianRadius = 0.6
appendAttributes2Display.SetScaleArray = ['POINTS', 'currK2']
appendAttributes2Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes2Display.OpacityArray = ['POINTS', 'currK2']
appendAttributes2Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes2Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes2Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes2Display.ScalarOpacityUnitDistance = 2.5028001676159013
appendAttributes2Display.OpacityArrayName = ['POINTS', 'currK2']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes2Display.ScaleTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes2Display.OpacityTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
appendAttributes2Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
appendAttributes2Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
appendAttributes2Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
appendAttributes2Display.DataAxesGrid.XTitleBold = 1
appendAttributes2Display.DataAxesGrid.XTitleFontSize = 24
appendAttributes2Display.DataAxesGrid.YTitleBold = 1
appendAttributes2Display.DataAxesGrid.YTitleFontSize = 24
appendAttributes2Display.DataAxesGrid.ZTitleBold = 1
appendAttributes2Display.DataAxesGrid.ZTitleFontSize = 23
appendAttributes2Display.DataAxesGrid.XLabelBold = 1
appendAttributes2Display.DataAxesGrid.XLabelFontSize = 17
appendAttributes2Display.DataAxesGrid.YLabelBold = 1
appendAttributes2Display.DataAxesGrid.YLabelFontSize = 17
appendAttributes2Display.DataAxesGrid.ZLabelBold = 1
appendAttributes2Display.DataAxesGrid.ZLabelFontSize = 17

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
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=appendAttributes2)
mergeVectorComponents2.XArray = 'currK2X'
# mergeVectorComponents2.YArray = 'currK2X'
# mergeVectorComponents2.ZArray = 'currK2X'

# Properties modified on mergeVectorComponents2
mergeVectorComponents2.YArray = 'currK2Y'
mergeVectorComponents2.ZArray = 'currK2Z'
mergeVectorComponents2.OutputVectorName = 'currK2'

# show data in view
mergeVectorComponents2Display = Show(mergeVectorComponents2, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents2Display.Representation = 'Surface'
mergeVectorComponents2Display.ColorArrayName = [None, '']
mergeVectorComponents2Display.SelectTCoordArray = 'None'
mergeVectorComponents2Display.SelectNormalArray = 'None'
mergeVectorComponents2Display.SelectTangentArray = 'None'
mergeVectorComponents2Display.OSPRayScaleArray = 'currK2'
mergeVectorComponents2Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.SelectOrientationVectors = 'None'
mergeVectorComponents2Display.ScaleFactor = 12.0
mergeVectorComponents2Display.SelectScaleArray = 'None'
mergeVectorComponents2Display.GlyphType = 'Arrow'
mergeVectorComponents2Display.GlyphTableIndexArray = 'None'
mergeVectorComponents2Display.GaussianRadius = 0.6
mergeVectorComponents2Display.SetScaleArray = ['POINTS', 'currK2']
mergeVectorComponents2Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.OpacityArray = ['POINTS', 'currK2']
mergeVectorComponents2Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents2Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents2Display.ScalarOpacityUnitDistance = 2.5028001676159013
mergeVectorComponents2Display.OpacityArrayName = ['POINTS', 'currK2']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents2Display.ScaleTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents2Display.OpacityTransferFunction.Points = [-0.0009655003960969376, 0.0, 0.5, 0.0, 0.0011813889236263336, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mergeVectorComponents2Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
mergeVectorComponents2Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
mergeVectorComponents2Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
mergeVectorComponents2Display.DataAxesGrid.XTitleBold = 1
mergeVectorComponents2Display.DataAxesGrid.XTitleFontSize = 24
mergeVectorComponents2Display.DataAxesGrid.YTitleBold = 1
mergeVectorComponents2Display.DataAxesGrid.YTitleFontSize = 24
mergeVectorComponents2Display.DataAxesGrid.ZTitleBold = 1
mergeVectorComponents2Display.DataAxesGrid.ZTitleFontSize = 23
mergeVectorComponents2Display.DataAxesGrid.XLabelBold = 1
mergeVectorComponents2Display.DataAxesGrid.XLabelFontSize = 17
mergeVectorComponents2Display.DataAxesGrid.YLabelBold = 1
mergeVectorComponents2Display.DataAxesGrid.YLabelFontSize = 17
mergeVectorComponents2Display.DataAxesGrid.ZLabelBold = 1
mergeVectorComponents2Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(appendAttributes2, renderView2)

# update the view to ensure updated data information
renderView2.Update()

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
renderView2.CameraPosition = [-4.914883380006738, -1.7358159363190553, 309.39856969822534]
renderView2.CameraViewUp = [-5.242531761370049e-05, 0.999984265987824, 0.0056093696953431705]
renderView2.CameraParallelScale = 80.08960536370884

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
