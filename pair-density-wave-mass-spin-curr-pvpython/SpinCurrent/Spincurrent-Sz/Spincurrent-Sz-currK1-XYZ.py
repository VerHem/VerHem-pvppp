# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# find source
pythonCalculator1 = FindSource('PythonCalculator1')

# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

# find source
pythonCalculator4 = FindSource('PythonCalculator4')

# find source
pythonCalculator5 = FindSource('PythonCalculator5')

# find source
pythonCalculator6 = FindSource('PythonCalculator6')

# find source
pythonCalculator7 = FindSource('PythonCalculator7')

# find source
pythonCalculator8 = FindSource('PythonCalculator8')

# find source
pythonCalculator9 = FindSource('PythonCalculator9')

# find source
pythonCalculator10 = FindSource('PythonCalculator10')

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
pythonCalculator16 = FindSource('PythonCalculator16')

# find source
pythonCalculator17 = FindSource('PythonCalculator17')

# find source
pythonCalculator18 = FindSource('PythonCalculator18')

# find source
output_conf_00pvtu = FindSource('output_conf_00.pvtu')


#########################################################################################
# spatial i = 1 i.e., x-component

# create a new 'Python Calculator'
pythonCalculator19 = PythonCalculator(registrationName='PythonCalculator19', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

## spin current K1 Sz contribution formilism:

# u2i u111 - u1i u121 + u2i u212 
# - u1i u222 + u2i u313 - u1i u323 

# + v2i v111 - v1i v121 + v2i v212 
# - v1i v222 + v2i v313 - v1i v323 

# Properties modified on pythonCalculator19, i = 1 i.e., X
pythonCalculator19.Expression = "inputs[0].PointData['u_21']*inputs[1].PointData['u_i11'][:,0]-inputs[0].PointData['u_11']*inputs[4].PointData['u_i21'][:,0]+inputs[0].PointData['u_21']*inputs[2].PointData['u_i12'][:,1]-inputs[0].PointData['u_11']*inputs[5].PointData['u_i22'][:,1]+inputs[0].PointData['u_21']*inputs[3].PointData['u_i13'][:,2]-inputs[0].PointData['u_11']*inputs[6].PointData['u_i23'][:,2]+inputs[0].PointData['v_21']*inputs[10].PointData['v_i11'][:,0]-inputs[0].PointData['v_11']*inputs[13].PointData['v_i21'][:,0]+inputs[0].PointData['v_21']*inputs[11].PointData['v_i12'][:,1]-inputs[0].PointData['v_11']*inputs[14].PointData['v_i22'][:,1]+inputs[0].PointData['v_21']*inputs[12].PointData['v_i13'][:,2]-inputs[0].PointData['v_11']*inputs[15].PointData['v_i23'][:,2]"

pythonCalculator19.ArrayName = 'SzcurrK1X'
pythonCalculator19.CopyArrays = 0

# show data in view
# pythonCalculator19Display = Show(pythonCalculator19, renderView1, 'UnstructuredGridRepresentation')

# # trace defaults for the display properties.
# pythonCalculator19Display.Representation = 'Surface'
# pythonCalculator19Display.ColorArrayName = [None, '']
# pythonCalculator19Display.SelectTCoordArray = 'None'
# pythonCalculator19Display.SelectNormalArray = 'None'
# pythonCalculator19Display.SelectTangentArray = 'None'
# pythonCalculator19Display.OSPRayScaleArray = 'SzcurrK1X'
# pythonCalculator19Display.OSPRayScaleFunction = 'PiecewiseFunction'
# pythonCalculator19Display.SelectOrientationVectors = 'None'
# pythonCalculator19Display.ScaleFactor = 12.0
# pythonCalculator19Display.SelectScaleArray = 'None'
# pythonCalculator19Display.GlyphType = 'Arrow'
# pythonCalculator19Display.GlyphTableIndexArray = 'None'
# pythonCalculator19Display.GaussianRadius = 0.6
# pythonCalculator19Display.SetScaleArray = ['POINTS', 'SzcurrK1X']
# pythonCalculator19Display.ScaleTransferFunction = 'PiecewiseFunction'
# pythonCalculator19Display.OpacityArray = ['POINTS', 'SzcurrK1X']
# pythonCalculator19Display.OpacityTransferFunction = 'PiecewiseFunction'
# pythonCalculator19Display.DataAxesGrid = 'GridAxesRepresentation'
# pythonCalculator19Display.PolarAxes = 'PolarAxesRepresentation'
# pythonCalculator19Display.ScalarOpacityUnitDistance = 2.5028001676159013
# pythonCalculator19Display.OpacityArrayName = ['POINTS', 'SzcurrK1X']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# pythonCalculator19Display.ScaleTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# pythonCalculator19Display.OpacityTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# pythonCalculator19Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# pythonCalculator19Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# pythonCalculator19Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# pythonCalculator19Display.DataAxesGrid.XTitleBold = 1
# pythonCalculator19Display.DataAxesGrid.XTitleFontSize = 24
# pythonCalculator19Display.DataAxesGrid.YTitleBold = 1
# pythonCalculator19Display.DataAxesGrid.YTitleFontSize = 24
# pythonCalculator19Display.DataAxesGrid.ZTitleBold = 1
# pythonCalculator19Display.DataAxesGrid.ZTitleFontSize = 23
# pythonCalculator19Display.DataAxesGrid.XLabelBold = 1
# pythonCalculator19Display.DataAxesGrid.XLabelFontSize = 17
# pythonCalculator19Display.DataAxesGrid.YLabelBold = 1
# pythonCalculator19Display.DataAxesGrid.YLabelFontSize = 17
# pythonCalculator19Display.DataAxesGrid.ZLabelBold = 1
# pythonCalculator19Display.DataAxesGrid.ZLabelFontSize = 17


#########################################################################################
# spatial i = 2 i.e., y-component

# create a new 'Python Calculator'
pythonCalculator20 = PythonCalculator(registrationName='PythonCalculator20', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

## spin current K1 Sz contribution formilism:

# u2i u111 - u1i u121 + u2i u212 
# - u1i u222 + u2i u313 - u1i u323 

# + v2i v111 - v1i v121 + v2i v212 
# - v1i v222 + v2i v313 - v1i v323 

# Properties modified on pythonCalculator19, i = 2 i.e., Y
pythonCalculator20.Expression = "inputs[0].PointData['u_22']*inputs[1].PointData['u_i11'][:,0]-inputs[0].PointData['u_12']*inputs[4].PointData['u_i21'][:,0]+inputs[0].PointData['u_22']*inputs[2].PointData['u_i12'][:,1]-inputs[0].PointData['u_12']*inputs[5].PointData['u_i22'][:,1]+inputs[0].PointData['u_22']*inputs[3].PointData['u_i13'][:,2]-inputs[0].PointData['u_12']*inputs[6].PointData['u_i23'][:,2]+inputs[0].PointData['v_22']*inputs[10].PointData['v_i11'][:,0]-inputs[0].PointData['v_12']*inputs[13].PointData['v_i21'][:,0]+inputs[0].PointData['v_22']*inputs[11].PointData['v_i12'][:,1]-inputs[0].PointData['v_12']*inputs[14].PointData['v_i22'][:,1]+inputs[0].PointData['v_22']*inputs[12].PointData['v_i13'][:,2]-inputs[0].PointData['v_12']*inputs[15].PointData['v_i23'][:,2]"


pythonCalculator20.ArrayName = 'SzcurrK1Y'
pythonCalculator20.CopyArrays = 0

# show data in view
# pythonCalculator20Display = Show(pythonCalculator20, renderView1, 'UnstructuredGridRepresentation')

# # trace defaults for the display properties.
# pythonCalculator20Display.Representation = 'Surface'
# pythonCalculator20Display.ColorArrayName = [None, '']
# pythonCalculator20Display.SelectTCoordArray = 'None'
# pythonCalculator20Display.SelectNormalArray = 'None'
# pythonCalculator20Display.SelectTangentArray = 'None'
# pythonCalculator20Display.OSPRayScaleArray = 'SzcurrK1Y'
# pythonCalculator20Display.OSPRayScaleFunction = 'PiecewiseFunction'
# pythonCalculator20Display.SelectOrientationVectors = 'None'
# pythonCalculator20Display.ScaleFactor = 12.0
# pythonCalculator20Display.SelectScaleArray = 'None'
# pythonCalculator20Display.GlyphType = 'Arrow'
# pythonCalculator20Display.GlyphTableIndexArray = 'None'
# pythonCalculator20Display.GaussianRadius = 0.6
# pythonCalculator20Display.SetScaleArray = ['POINTS', 'SzcurrK1Y']
# pythonCalculator20Display.ScaleTransferFunction = 'PiecewiseFunction'
# pythonCalculator20Display.OpacityArray = ['POINTS', 'SzcurrK1Y']
# pythonCalculator20Display.OpacityTransferFunction = 'PiecewiseFunction'
# pythonCalculator20Display.DataAxesGrid = 'GridAxesRepresentation'
# pythonCalculator20Display.PolarAxes = 'PolarAxesRepresentation'
# pythonCalculator20Display.ScalarOpacityUnitDistance = 2.5028001676159013
# pythonCalculator20Display.OpacityArrayName = ['POINTS', 'SzcurrK1Y']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# pythonCalculator20Display.ScaleTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# pythonCalculator20Display.OpacityTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# pythonCalculator20Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# pythonCalculator20Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# pythonCalculator20Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# pythonCalculator20Display.DataAxesGrid.XTitleBold = 1
# pythonCalculator20Display.DataAxesGrid.XTitleFontSize = 24
# pythonCalculator20Display.DataAxesGrid.YTitleBold = 1
# pythonCalculator20Display.DataAxesGrid.YTitleFontSize = 24
# pythonCalculator20Display.DataAxesGrid.ZTitleBold = 1
# pythonCalculator20Display.DataAxesGrid.ZTitleFontSize = 23
# pythonCalculator20Display.DataAxesGrid.XLabelBold = 1
# pythonCalculator20Display.DataAxesGrid.XLabelFontSize = 17
# pythonCalculator20Display.DataAxesGrid.YLabelBold = 1
# pythonCalculator20Display.DataAxesGrid.YLabelFontSize = 17
# pythonCalculator20Display.DataAxesGrid.ZLabelBold = 1
# pythonCalculator20Display.DataAxesGrid.ZLabelFontSize = 17


#########################################################################################
# spatial i = 3 i.e., z-component

# create a new 'Python Calculator'
pythonCalculator21 = PythonCalculator(registrationName='PythonCalculator21', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

## spin current K1 Sz contribution formilism:

# u2i u111 - u1i u121 + u2i u212 
# - u1i u222 + u2i u313 - u1i u323 

# + v2i v111 - v1i v121 + v2i v212 
# - v1i v222 + v2i v313 - v1i v323 

# Properties modified on pythonCalculator19, i = 1 i.e., Z
pythonCalculator21.Expression = "inputs[0].PointData['u_23']*inputs[1].PointData['u_i11'][:,0]-inputs[0].PointData['u_13']*inputs[4].PointData['u_i21'][:,0]+inputs[0].PointData['u_23']*inputs[2].PointData['u_i12'][:,1]-inputs[0].PointData['u_13']*inputs[5].PointData['u_i22'][:,1]+inputs[0].PointData['u_23']*inputs[3].PointData['u_i13'][:,2]-inputs[0].PointData['u_13']*inputs[6].PointData['u_i23'][:,2]+inputs[0].PointData['v_23']*inputs[10].PointData['v_i11'][:,0]-inputs[0].PointData['v_13']*inputs[13].PointData['v_i21'][:,0]+inputs[0].PointData['v_23']*inputs[11].PointData['v_i12'][:,1]-inputs[0].PointData['v_13']*inputs[14].PointData['v_i22'][:,1]+inputs[0].PointData['v_23']*inputs[12].PointData['v_i13'][:,2]-inputs[0].PointData['v_13']*inputs[15].PointData['v_i23'][:,2]"


pythonCalculator21.ArrayName = 'SzcurrK1Z'
pythonCalculator21.CopyArrays = 0

# show data in view
# pythonCalculator21Display = Show(pythonCalculator21, renderView1, 'UnstructuredGridRepresentation')

# # trace defaults for the display properties.
# pythonCalculator21Display.Representation = 'Surface'
# pythonCalculator21Display.ColorArrayName = [None, '']
# pythonCalculator21Display.SelectTCoordArray = 'None'
# pythonCalculator21Display.SelectNormalArray = 'None'
# pythonCalculator21Display.SelectTangentArray = 'None'
# pythonCalculator21Display.OSPRayScaleArray = 'SzcurrK1Z'
# pythonCalculator21Display.OSPRayScaleFunction = 'PiecewiseFunction'
# pythonCalculator21Display.SelectOrientationVectors = 'None'
# pythonCalculator21Display.ScaleFactor = 12.0
# pythonCalculator21Display.SelectScaleArray = 'None'
# pythonCalculator21Display.GlyphType = 'Arrow'
# pythonCalculator21Display.GlyphTableIndexArray = 'None'
# pythonCalculator21Display.GaussianRadius = 0.6
# pythonCalculator21Display.SetScaleArray = ['POINTS', 'SzcurrK1Z']
# pythonCalculator21Display.ScaleTransferFunction = 'PiecewiseFunction'
# pythonCalculator21Display.OpacityArray = ['POINTS', 'SzcurrK1Z']
# pythonCalculator21Display.OpacityTransferFunction = 'PiecewiseFunction'
# pythonCalculator21Display.DataAxesGrid = 'GridAxesRepresentation'
# pythonCalculator21Display.PolarAxes = 'PolarAxesRepresentation'
# pythonCalculator21Display.ScalarOpacityUnitDistance = 2.5028001676159013
# pythonCalculator21Display.OpacityArrayName = ['POINTS', 'SzcurrK1Z']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# pythonCalculator21Display.ScaleTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# pythonCalculator21Display.OpacityTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# pythonCalculator21Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# pythonCalculator21Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# pythonCalculator21Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# pythonCalculator21Display.DataAxesGrid.XTitleBold = 1
# pythonCalculator21Display.DataAxesGrid.XTitleFontSize = 24
# pythonCalculator21Display.DataAxesGrid.YTitleBold = 1
# pythonCalculator21Display.DataAxesGrid.YTitleFontSize = 24
# pythonCalculator21Display.DataAxesGrid.ZTitleBold = 1
# pythonCalculator21Display.DataAxesGrid.ZTitleFontSize = 23
# pythonCalculator21Display.DataAxesGrid.XLabelBold = 1
# pythonCalculator21Display.DataAxesGrid.XLabelFontSize = 17
# pythonCalculator21Display.DataAxesGrid.YLabelBold = 1
# pythonCalculator21Display.DataAxesGrid.YLabelFontSize = 17
# pythonCalculator21Display.DataAxesGrid.ZLabelBold = 1
# pythonCalculator21Display.DataAxesGrid.ZLabelFontSize = 17


# reset view to fit data
# renderView1.ResetCamera(False)

# get the material library
# materialLibrary1 = GetMaterialLibrary()

# hide data in view
# Hide(pythonCalculator2, renderView1)

# hide data in view
# Hide(pythonCalculator1, renderView1)

# hide data in view
# Hide(output_conf_00pvtu, renderView1)

# hide data in view
# Hide(pythonCalculator3, renderView1)


# update the view to ensure updated data information
# renderView1.Update()

# Properties modified on pythonCalculator21
# pythonCalculator21.CopyArrays = 0

# update the view to ensure updated data information
# renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
# layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
# layout1.SetSize(931, 1120)
# layout1.SetSize(1922, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
# renderView1.CameraPosition = [0.0, 0.0, 368.3884445988151]
# renderView1.CameraViewUp = [0.0, 0.9999842640648654, 0.005609957455249585]
# renderView1.CameraParallelScale = 96.34839743002567
# renderView1.CameraPosition = [0.0, -1.7359591081103158, 309.43760358574116]
# renderView1.CameraViewUp = [0.0, 0.9999842640648654, 0.005609957455249585]
# renderView1.CameraParallelScale = 80.08960536370884

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
