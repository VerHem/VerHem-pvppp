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

# find source
setup_conf_00pvtu = FindSource('setup_conf_00.pvtu')

# find source
calculator2 = FindSource('Calculator2')

# find source
calculator6 = FindSource('Calculator6')

# find source
mergeVectorComponents2 = FindSource('MergeVectorComponents2')

# find source
pythonCalculator1 = FindSource('PythonCalculator1')

# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# find source
mergeVectorComponents1 = FindSource('MergeVectorComponents1')

# find source
calculator4 = FindSource('Calculator4')

# find source
calculator5 = FindSource('Calculator5')

# find source
pythonCalculator4 = FindSource('PythonCalculator4')

# find source
calculator3 = FindSource('Calculator3')

# find source
pythonCalculator6 = FindSource('PythonCalculator6')

# Properties modified on sphere1
sphere1.Center = [-15.0, -15.0, -15.0]
sphere1.Radius = 30.0
sphere1.ThetaResolution = 1000
sphere1.EndTheta = 90.0
sphere1.PhiResolution = 1000
sphere1.EndPhi = 90.0

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
sphere1Display = Show(sphere1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
# sphere1Display.Representation = 'Surface'
# sphere1Display.ColorArrayName = [None, '']
# sphere1Display.SelectTCoordArray = 'None'
# sphere1Display.SelectNormalArray = 'Normals'
# sphere1Display.SelectTangentArray = 'None'
# sphere1Display.OSPRayScaleArray = 'Normals'
# sphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# sphere1Display.SelectOrientationVectors = 'None'
# sphere1Display.ScaleFactor = 3.0
# sphere1Display.SelectScaleArray = 'None'
# sphere1Display.GlyphType = 'Arrow'
# sphere1Display.GlyphTableIndexArray = 'None'
# sphere1Display.GaussianRadius = 0.15
# sphere1Display.SetScaleArray = ['POINTS', 'Normals']
# sphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
# sphere1Display.OpacityArray = ['POINTS', 'Normals']
# sphere1Display.OpacityTransferFunction = 'PiecewiseFunction'
# sphere1Display.DataAxesGrid = 'GridAxesRepresentation'
# sphere1Display.PolarAxes = 'PolarAxesRepresentation'

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# sphere1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# sphere1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# sphere1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# sphere1Display.DataAxesGrid.XTitleBold = 1
# sphere1Display.DataAxesGrid.XTitleFontSize = 24
# sphere1Display.DataAxesGrid.YTitleBold = 1
# sphere1Display.DataAxesGrid.YTitleFontSize = 24
# sphere1Display.DataAxesGrid.ZTitleBold = 1
# sphere1Display.DataAxesGrid.ZTitleFontSize = 23
# sphere1Display.DataAxesGrid.XLabelBold = 1
# sphere1Display.DataAxesGrid.XLabelFontSize = 17
# sphere1Display.DataAxesGrid.YLabelBold = 1
# sphere1Display.DataAxesGrid.YLabelFontSize = 17
# sphere1Display.DataAxesGrid.ZLabelBold = 1
# sphere1Display.DataAxesGrid.ZLabelFontSize = 17

# # reset view to fit data
# renderView1.ResetCamera(False)

# # get the material library
# materialLibrary1 = GetMaterialLibrary()

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

# find source
pythonCalculator5 = FindSource('PythonCalculator5')

# find source
mergeVectorComponents3 = FindSource('MergeVectorComponents3')

# find source
appendAttributes1 = FindSource('AppendAttributes1')

# find source
calculator1 = FindSource('Calculator1')

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(sphere1, renderView1)

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(registrationName='ResampleWithDataset1', SourceDataArrays=mergeVectorComponents3,
    DestinationMesh=sphere1)
resampleWithDataset1.CellLocator = 'Static Cell Locator'

# Properties modified on resampleWithDataset1
resampleWithDataset1.PassPointArrays = 1

# show data in view
resampleWithDataset1Display = Show(resampleWithDataset1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
# resampleWithDataset1Display.Representation = 'Surface'
# resampleWithDataset1Display.ColorArrayName = [None, '']
# resampleWithDataset1Display.SelectTCoordArray = 'None'
# resampleWithDataset1Display.SelectNormalArray = 'Normals'
# resampleWithDataset1Display.SelectTangentArray = 'None'
# resampleWithDataset1Display.OSPRayScaleArray = 'Normals'
# resampleWithDataset1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# resampleWithDataset1Display.SelectOrientationVectors = 'None'
# resampleWithDataset1Display.ScaleFactor = 3.0
# resampleWithDataset1Display.SelectScaleArray = 'None'
# resampleWithDataset1Display.GlyphType = 'Arrow'
# resampleWithDataset1Display.GlyphTableIndexArray = 'None'
# resampleWithDataset1Display.GaussianRadius = 0.15
# resampleWithDataset1Display.SetScaleArray = ['POINTS', 'Normals']
# resampleWithDataset1Display.ScaleTransferFunction = 'PiecewiseFunction'
# resampleWithDataset1Display.OpacityArray = ['POINTS', 'Normals']
# resampleWithDataset1Display.OpacityTransferFunction = 'PiecewiseFunction'
# resampleWithDataset1Display.DataAxesGrid = 'GridAxesRepresentation'
# resampleWithDataset1Display.PolarAxes = 'PolarAxesRepresentation'

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# resampleWithDataset1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# resampleWithDataset1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# resampleWithDataset1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# resampleWithDataset1Display.DataAxesGrid.XTitleBold = 1
# resampleWithDataset1Display.DataAxesGrid.XTitleFontSize = 24
# resampleWithDataset1Display.DataAxesGrid.YTitleBold = 1
# resampleWithDataset1Display.DataAxesGrid.YTitleFontSize = 24
# resampleWithDataset1Display.DataAxesGrid.ZTitleBold = 1
# resampleWithDataset1Display.DataAxesGrid.ZTitleFontSize = 23
# resampleWithDataset1Display.DataAxesGrid.XLabelBold = 1
# resampleWithDataset1Display.DataAxesGrid.XLabelFontSize = 17
# resampleWithDataset1Display.DataAxesGrid.YLabelBold = 1
# resampleWithDataset1Display.DataAxesGrid.YLabelFontSize = 17
# resampleWithDataset1Display.DataAxesGrid.ZLabelBold = 1
# resampleWithDataset1Display.DataAxesGrid.ZLabelFontSize = 17

# # reset view to fit data
# renderView1.ResetCamera(False)

# hide data in view
Hide(sphere1, renderView1)

# hide data in view
Hide(mergeVectorComponents3, renderView1)

# update the view to ensure updated data information
# renderView1.Update()

# hide data in view
Hide(resampleWithDataset1, renderView1)

# create a new 'Calculator'
calculator7 = Calculator(registrationName='Calculator7', Input=resampleWithDataset1)

calculator7.ResultArrayName = 'empmpm.n'
calculator7.Function = 'dot(empmpm,Normals)'

# show data in view
calculator7Display = Show(calculator7, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'empmpmn'
# empmpmnLUT = GetColorTransferFunction('empmpmn')
# empmpmnLUT.RGBPoints = [-0.0794431796070515, 0.231373, 0.298039, 0.752941, -0.00990042582386047, 0.865003, 0.865003, 0.865003, 0.059642327959330554, 0.705882, 0.0156863, 0.14902]
# empmpmnLUT.ScalarRangeInitialized = 1.0

# # trace defaults for the display properties.
# calculator7Display.Representation = 'Surface'
# calculator7Display.ColorArrayName = ['POINTS', 'empmpm.n']
# calculator7Display.LookupTable = empmpmnLUT
# calculator7Display.SelectTCoordArray = 'None'
# calculator7Display.SelectNormalArray = 'Normals'
# calculator7Display.SelectTangentArray = 'None'
# calculator7Display.OSPRayScaleArray = 'empmpm.n'
# calculator7Display.OSPRayScaleFunction = 'PiecewiseFunction'
# calculator7Display.SelectOrientationVectors = 'None'
# calculator7Display.ScaleFactor = 3.0
# calculator7Display.SelectScaleArray = 'empmpm.n'
# calculator7Display.GlyphType = 'Arrow'
# calculator7Display.GlyphTableIndexArray = 'empmpm.n'
# calculator7Display.GaussianRadius = 0.15
# calculator7Display.SetScaleArray = ['POINTS', 'empmpm.n']
# calculator7Display.ScaleTransferFunction = 'PiecewiseFunction'
# calculator7Display.OpacityArray = ['POINTS', 'empmpm.n']
# calculator7Display.OpacityTransferFunction = 'PiecewiseFunction'
# calculator7Display.DataAxesGrid = 'GridAxesRepresentation'
# calculator7Display.PolarAxes = 'PolarAxesRepresentation'

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# calculator7Display.ScaleTransferFunction.Points = [-0.0794431796070515, 0.0, 0.5, 0.0, 0.059642327959330554, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# calculator7Display.OpacityTransferFunction.Points = [-0.0794431796070515, 0.0, 0.5, 0.0, 0.059642327959330554, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# calculator7Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# calculator7Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# calculator7Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# calculator7Display.DataAxesGrid.XTitleBold = 1
# calculator7Display.DataAxesGrid.XTitleFontSize = 24
# calculator7Display.DataAxesGrid.YTitleBold = 1
# calculator7Display.DataAxesGrid.YTitleFontSize = 24
# calculator7Display.DataAxesGrid.ZTitleBold = 1
# calculator7Display.DataAxesGrid.ZTitleFontSize = 23
# calculator7Display.DataAxesGrid.XLabelBold = 1
# calculator7Display.DataAxesGrid.XLabelFontSize = 17
# calculator7Display.DataAxesGrid.YLabelBold = 1
# calculator7Display.DataAxesGrid.YLabelFontSize = 17
# calculator7Display.DataAxesGrid.ZLabelBold = 1
# calculator7Display.DataAxesGrid.ZLabelFontSize = 17

# # reset view to fit data
# renderView1.ResetCamera(False)

# hide data in view
Hide(resampleWithDataset1, renderView1)

# show color bar/color legend
calculator7Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
# empmpmnLUT.RescaleTransferFunction(-0.0794431796070515, 0.05964232795933056)

# # get opacity transfer function/opacity map for 'empmpmn'
# empmpmnPWF = GetOpacityTransferFunction('empmpmn')
# empmpmnPWF.Points = [-0.0794431796070515, 0.0, 0.5, 0.0, 0.059642327959330554, 1.0, 0.5, 0.0]
# empmpmnPWF.ScalarRangeInitialized = 1

# # Rescale transfer function
# empmpmnPWF.RescaleTransferFunction(-0.0794431796070515, 0.05964232795933056)

# hide data in view
Hide(calculator7, renderView1)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=calculator7)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# Properties modified on integrateVariables1Display
integrateVariables1Display.Assembly = ''

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1300, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
# renderView1.CameraPosition = [-27.669348646204945, 21.9055206827265, -93.97389259549361]
# renderView1.CameraViewUp = [0.6558245544129228, 0.7547180043688183, -0.017172294856532627]
# renderView1.CameraParallelScale = 25.98076211353316

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
