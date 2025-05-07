# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
pythonCalculator1 = FindSource('PythonCalculator1')

# set active source
SetActiveSource(pythonCalculator1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
pythonCalculator1Display = GetDisplayProperties(pythonCalculator1, view=renderView1)

# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# set active source
SetActiveSource(pythonCalculator2)

# get display properties
pythonCalculator2Display = GetDisplayProperties(pythonCalculator2, view=renderView1)

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

# set active source
SetActiveSource(pythonCalculator3)

# get display properties
pythonCalculator3Display = GetDisplayProperties(pythonCalculator3, view=renderView1)

# find source
output_conf_00pvtu = FindSource('output_conf_00.pvtu')

# create a new 'Python Calculator'
pythonCalculator19 = PythonCalculator(registrationName='PythonCalculator19', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3])
pythonCalculator19.Expression = ''

# find source
pythonCalculator9 = FindSource('PythonCalculator9')

# find source
pythonCalculator12 = FindSource('PythonCalculator12')

# find source
pythonCalculator7 = FindSource('PythonCalculator7')

# find source
pythonCalculator13 = FindSource('PythonCalculator13')

# find source
pythonCalculator11 = FindSource('PythonCalculator11')

# find source
pythonCalculator15 = FindSource('PythonCalculator15')

# find source
pythonCalculator16 = FindSource('PythonCalculator16')

# find source
pythonCalculator18 = FindSource('PythonCalculator18')

# find source
pythonCalculator8 = FindSource('PythonCalculator8')

# find source
pythonCalculator10 = FindSource('PythonCalculator10')

# find source
pythonCalculator14 = FindSource('PythonCalculator14')

# find source
pythonCalculator6 = FindSource('PythonCalculator6')

# find source
pythonCalculator17 = FindSource('PythonCalculator17')

# Properties modified on pythonCalculator19
pythonCalculator19.Expression = "-inputs[1].PointData['u_i11']*inputs[0].PointData['v_11']-inputs[2].PointData['u_i12']*inputs[0].PointData['v_12']-inputs[3].PointData['u_i13']*inputs[0].PointData['v_13']"
pythonCalculator19.ArrayName = 'currK1'
pythonCalculator19.CopyArrays = 0

# show data in view
pythonCalculator19Display = Show(pythonCalculator19, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator19Display.Representation = 'Surface'
pythonCalculator19Display.ColorArrayName = [None, '']
pythonCalculator19Display.SelectTCoordArray = 'None'
pythonCalculator19Display.SelectNormalArray = 'None'
pythonCalculator19Display.SelectTangentArray = 'None'
pythonCalculator19Display.OSPRayScaleArray = 'currK1'
pythonCalculator19Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator19Display.SelectOrientationVectors = 'None'
pythonCalculator19Display.ScaleFactor = 12.0
pythonCalculator19Display.SelectScaleArray = 'None'
pythonCalculator19Display.GlyphType = 'Arrow'
pythonCalculator19Display.GlyphTableIndexArray = 'None'
pythonCalculator19Display.GaussianRadius = 0.6
pythonCalculator19Display.SetScaleArray = ['POINTS', 'currK1']
pythonCalculator19Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator19Display.OpacityArray = ['POINTS', 'currK1']
pythonCalculator19Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator19Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator19Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator19Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator19Display.OpacityArrayName = ['POINTS', 'currK1']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator19Display.ScaleTransferFunction.Points = [-0.05295347401882098, 0.0, 0.5, 0.0, 0.05299203415300493, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator19Display.OpacityTransferFunction.Points = [-0.05295347401882098, 0.0, 0.5, 0.0, 0.05299203415300493, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator19Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator19Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator19Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator19Display.DataAxesGrid.XTitleBold = 1
pythonCalculator19Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator19Display.DataAxesGrid.YTitleBold = 1
pythonCalculator19Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator19Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator19Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator19Display.DataAxesGrid.XLabelBold = 1
pythonCalculator19Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator19Display.DataAxesGrid.YLabelBold = 1
pythonCalculator19Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator19Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator19Display.DataAxesGrid.ZLabelFontSize = 17

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# hide data in view
Hide(pythonCalculator2, renderView1)

# hide data in view
Hide(pythonCalculator1, renderView1)

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# hide data in view
Hide(pythonCalculator3, renderView1)

# find source
pythonCalculator4 = FindSource('PythonCalculator4')

# find source
pythonCalculator5 = FindSource('PythonCalculator5')

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
renderView1.CameraPosition = [0.0, -1.7359591081103158, 309.43760358574116]
renderView1.CameraViewUp = [0.0, 0.9999842640648654, 0.005609957455249585]
renderView1.CameraParallelScale = 80.08960536370884

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).