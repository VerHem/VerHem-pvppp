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

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')


# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

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

# find source
output_conf_00pvtu = FindSource('output_conf_00.pvtu')


# create a new 'Python Calculator'
pythonCalculator19 = PythonCalculator(registrationName='PythonCalculator19', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])



## mass current K2 contribution formilism:
# -u11i v11 - u21i v12 - u31i v13 - u12i v21 - u22i v22 - u32i v23 - u13i v31 - u23i v32 - u33i v33 +
# u11 v11i + u21 v12i + u31 v13i + u12 v21i + u22 v22i + u32 v23i + u13 v31i + u23 v32i + u33 v33i


# Properties modified on pythonCalculator19
pythonCalculator19.Expression = "-inputs[1].PointData['u_i11']*inputs[0].PointData['v_11']-inputs[2].PointData['u_i12']*inputs[0].PointData['v_12']-inputs[3].PointData['u_i13']*inputs[0].PointData['v_13']-inputs[4].PointData['u_i21']*inputs[0].PointData['v_21']-inputs[5].PointData['u_i22']*inputs[0].PointData['v_22']-inputs[6].PointData['u_i23']*inputs[0].PointData['v_23']-inputs[7].PointData['u_i31']*inputs[0].PointData['v_31']-inputs[8].PointData['u_i32']*inputs[0].PointData['v_32']-inputs[9].PointData['u_i33']*inputs[0].PointData['v_33']+inputs[0].PointData['u_11']*inputs[10].PointData['v_i11']+inputs[0].PointData['u_12']*inputs[11].PointData['v_i12']+inputs[0].PointData['u_13']*inputs[12].PointData['v_i13']+inputs[0].PointData['u_21']*inputs[13].PointData['v_i21']+inputs[0].PointData['u_22']*inputs[14].PointData['v_i22']+inputs[0].PointData['u_23']*inputs[15].PointData['v_i23']+inputs[0].PointData['u_31']*inputs[16].PointData['v_i31']+inputs[0].PointData['u_32']*inputs[17].PointData['v_i32']+inputs[0].PointData['u_33']*inputs[18].PointData['v_i33']"

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
# pythonCalculator4 = FindSource('PythonCalculator4')

# find source
# pythonCalculator5 = FindSource('PythonCalculator5')

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
