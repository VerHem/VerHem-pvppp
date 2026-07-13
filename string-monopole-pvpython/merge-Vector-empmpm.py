# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
pythonCalculator4 = FindSource('PythonCalculator4')

# set active source
SetActiveSource(pythonCalculator4)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
pythonCalculator4Display = GetDisplayProperties(pythonCalculator4, view=renderView1)

# find source
pythonCalculator5 = FindSource('PythonCalculator5')

# set active source
SetActiveSource(pythonCalculator5)

# get display properties
pythonCalculator5Display = GetDisplayProperties(pythonCalculator5, view=renderView1)

# find source
pythonCalculator6 = FindSource('PythonCalculator6')

# set active source
SetActiveSource(pythonCalculator6)

# get display properties
pythonCalculator6Display = GetDisplayProperties(pythonCalculator6, view=renderView1)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pythonCalculator4, pythonCalculator5, pythonCalculator6])

# find source
mergeVectorComponents2 = FindSource('MergeVectorComponents2')

# find source
mergeVectorComponents1 = FindSource('MergeVectorComponents1')

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
# appendAttributes1Display.Representation = 'Surface'
# appendAttributes1Display.ColorArrayName = [None, '']
# appendAttributes1Display.SelectTCoordArray = 'None'
# appendAttributes1Display.SelectNormalArray = 'None'
# appendAttributes1Display.SelectTangentArray = 'None'
# appendAttributes1Display.OSPRayScaleArray = 'empmpm1'
# appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# appendAttributes1Display.SelectOrientationVectors = 'None'
# appendAttributes1Display.ScaleFactor = 3.0
# appendAttributes1Display.SelectScaleArray = 'None'
# appendAttributes1Display.GlyphType = 'Arrow'
# appendAttributes1Display.GlyphTableIndexArray = 'None'
# appendAttributes1Display.GaussianRadius = 0.15
# appendAttributes1Display.SetScaleArray = ['POINTS', 'empmpm1']
# appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
# appendAttributes1Display.OpacityArray = ['POINTS', 'empmpm1']
# appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
# appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
# appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
# appendAttributes1Display.ScalarOpacityUnitDistance = 1.447513849627623
# appendAttributes1Display.OpacityArrayName = ['POINTS', 'empmpm1']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# appendAttributes1Display.ScaleTransferFunction.Points = [-0.4081325403831525, 0.0, 0.5, 0.0, 0.1608497263205667, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# appendAttributes1Display.OpacityTransferFunction.Points = [-0.4081325403831525, 0.0, 0.5, 0.0, 0.1608497263205667, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# appendAttributes1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# appendAttributes1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# appendAttributes1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# appendAttributes1Display.DataAxesGrid.XTitleBold = 1
# appendAttributes1Display.DataAxesGrid.XTitleFontSize = 24
# appendAttributes1Display.DataAxesGrid.YTitleBold = 1
# appendAttributes1Display.DataAxesGrid.YTitleFontSize = 24
# appendAttributes1Display.DataAxesGrid.ZTitleBold = 1
# appendAttributes1Display.DataAxesGrid.ZTitleFontSize = 23
# appendAttributes1Display.DataAxesGrid.XLabelBold = 1
# appendAttributes1Display.DataAxesGrid.XLabelFontSize = 17
# appendAttributes1Display.DataAxesGrid.YLabelBold = 1
# appendAttributes1Display.DataAxesGrid.YLabelFontSize = 17
# appendAttributes1Display.DataAxesGrid.ZLabelBold = 1
# appendAttributes1Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# hide data in view
Hide(pythonCalculator5, renderView1)

# hide data in view
Hide(pythonCalculator4, renderView1)

# hide data in view
Hide(pythonCalculator6, renderView1)

# find source
calculator1 = FindSource('Calculator1')

# find source
calculator4 = FindSource('Calculator4')

# find source
calculator3 = FindSource('Calculator3')

# find source
calculator5 = FindSource('Calculator5')

# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

# find source
calculator6 = FindSource('Calculator6')

# find source
setup_conf_00pvtu = FindSource('setup_conf_00.pvtu')

# Properties modified on setup_conf_00pvtu
setup_conf_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# find source
calculator2 = FindSource('Calculator2')

# find source
pythonCalculator1 = FindSource('PythonCalculator1')

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents3 = MergeVectorComponents(registrationName='MergeVectorComponents3', Input=appendAttributes1)
mergeVectorComponents3.XArray = 'empmpm1'
mergeVectorComponents3.YArray = 'empmpm2'
mergeVectorComponents3.ZArray = 'empmpm3'
mergeVectorComponents3.OutputVectorName = 'empmpm'

# show data in view
mergeVectorComponents3Display = Show(mergeVectorComponents3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
# mergeVectorComponents3Display.Representation = 'Surface'
# mergeVectorComponents3Display.ColorArrayName = [None, '']
# mergeVectorComponents3Display.SelectTCoordArray = 'None'
# mergeVectorComponents3Display.SelectNormalArray = 'None'
# mergeVectorComponents3Display.SelectTangentArray = 'None'
# mergeVectorComponents3Display.OSPRayScaleArray = 'empmpm'
# mergeVectorComponents3Display.OSPRayScaleFunction = 'PiecewiseFunction'
# mergeVectorComponents3Display.SelectOrientationVectors = 'None'
# mergeVectorComponents3Display.ScaleFactor = 3.0
# mergeVectorComponents3Display.SelectScaleArray = 'None'
# mergeVectorComponents3Display.GlyphType = 'Arrow'
# mergeVectorComponents3Display.GlyphTableIndexArray = 'None'
# mergeVectorComponents3Display.GaussianRadius = 0.15
# mergeVectorComponents3Display.SetScaleArray = ['POINTS', 'empmpm']
# mergeVectorComponents3Display.ScaleTransferFunction = 'PiecewiseFunction'
# mergeVectorComponents3Display.OpacityArray = ['POINTS', 'empmpm']
# mergeVectorComponents3Display.OpacityTransferFunction = 'PiecewiseFunction'
# mergeVectorComponents3Display.DataAxesGrid = 'GridAxesRepresentation'
# mergeVectorComponents3Display.PolarAxes = 'PolarAxesRepresentation'
# mergeVectorComponents3Display.ScalarOpacityUnitDistance = 1.447513849627623
# mergeVectorComponents3Display.OpacityArrayName = ['POINTS', 'empmpm']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# mergeVectorComponents3Display.ScaleTransferFunction.Points = [-0.4081325403831525, 0.0, 0.5, 0.0, 0.1608497263205667, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# mergeVectorComponents3Display.OpacityTransferFunction.Points = [-0.4081325403831525, 0.0, 0.5, 0.0, 0.1608497263205667, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# mergeVectorComponents3Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# mergeVectorComponents3Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# mergeVectorComponents3Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# mergeVectorComponents3Display.DataAxesGrid.XTitleBold = 1
# mergeVectorComponents3Display.DataAxesGrid.XTitleFontSize = 24
# mergeVectorComponents3Display.DataAxesGrid.YTitleBold = 1
# mergeVectorComponents3Display.DataAxesGrid.YTitleFontSize = 24
# mergeVectorComponents3Display.DataAxesGrid.ZTitleBold = 1
# mergeVectorComponents3Display.DataAxesGrid.ZTitleFontSize = 23
# mergeVectorComponents3Display.DataAxesGrid.XLabelBold = 1
# mergeVectorComponents3Display.DataAxesGrid.XLabelFontSize = 17
# mergeVectorComponents3Display.DataAxesGrid.YLabelBold = 1
# mergeVectorComponents3Display.DataAxesGrid.YLabelFontSize = 17
# mergeVectorComponents3Display.DataAxesGrid.ZLabelBold = 1
# mergeVectorComponents3Display.DataAxesGrid.ZLabelFontSize = 17

# hide data in view
Hide(appendAttributes1, renderView1)

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
layout1.SetSize(1939, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-27.669348646204945, 21.9055206827265, -93.97389259549361]
renderView1.CameraViewUp = [0.6558245544129228, 0.7547180043688183, -0.017172294856532627]
renderView1.CameraParallelScale = 25.98076211353316

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
