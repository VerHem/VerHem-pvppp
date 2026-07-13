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
# SetActiveSource(pythonCalculator1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
# pythonCalculator1Display = GetDisplayProperties(pythonCalculator1, view=renderView1)

# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# set active source
# SetActiveSource(pythonCalculator2)

# get display properties
# pythonCalculator2Display = GetDisplayProperties(pythonCalculator2, view=renderView1)

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

# set active source
# SetActiveSource(pythonCalculator3)

# get display properties
# pythonCalculator3Display = GetDisplayProperties(pythonCalculator3, view=renderView1)

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
pythonCalculator4 = FindSource('PythonCalculator4')

# find source
pythonCalculator5 = FindSource('PythonCalculator5')

# find source
output_conf_00pvtu = FindSource('output_conf_00.pvtu')


#########################################################################################


# create a new 'Python Calculator'
pythonCalculator23 = PythonCalculator(registrationName='PythonCalculator23', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

## mass current K3 contribution formilism:
# -u111 v1i - u212 v1i - u313 v1i
# -u121 v2i - u222 v2i - u323 v2i
# -u131 v3i - u232 v3i - u333 v3i
# +u1i v111 + u2i v121 + u3i v131
# +u1i v212 + u2i v222 + u3i v232
# +u1i v313 + u2i v323 + u3i v333

# Properties modified on pythonCalculator23, i = 1 i.e., X
pythonCalculator23.Expression = "-inputs[1].PointData['u_i11'][:,0]*inputs[0].PointData['v_11']-inputs[2].PointData['u_i12'][:,1]*inputs[0].PointData['v_11']-inputs[3].PointData['u_i13'][:,2]*inputs[0].PointData['v_11']-inputs[4].PointData['u_i21'][:,0]*inputs[0].PointData['v_21']-inputs[5].PointData['u_i22'][:,1]*inputs[0].PointData['v_21']-inputs[6].PointData['u_i23'][:,2]*inputs[0].PointData['v_21']-inputs[7].PointData['u_i31'][:,0]*inputs[0].PointData['v_31']-inputs[8].PointData['u_i32'][:,1]*inputs[0].PointData['v_31']-inputs[9].PointData['u_i33'][:,2]*inputs[0].PointData['v_31']+inputs[0].PointData['u_11']*inputs[10].PointData['v_i11'][:,0]+inputs[0].PointData['u_21']*inputs[13].PointData['v_i21'][:,0]+inputs[0].PointData['u_31']*inputs[16].PointData['v_i31'][:,0]+inputs[0].PointData['u_11']*inputs[11].PointData['v_i12'][:,1]+inputs[0].PointData['u_21']*inputs[14].PointData['v_i22'][:,1]+inputs[0].PointData['u_31']*inputs[17].PointData['v_i32'][:,1]+inputs[0].PointData['u_11']*inputs[12].PointData['v_i13'][:,2]+inputs[0].PointData['u_21']*inputs[15].PointData['v_i23'][:,2]+inputs[0].PointData['u_31']*inputs[18].PointData['v_i33'][:,2]"

pythonCalculator23.ArrayName = 'currK3X'
pythonCalculator23.CopyArrays = 0

# show data in view
pythonCalculator23Display = Show(pythonCalculator23, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator23Display.Representation = 'Surface'
pythonCalculator23Display.ColorArrayName = [None, '']
pythonCalculator23Display.SelectTCoordArray = 'None'
pythonCalculator23Display.SelectNormalArray = 'None'
pythonCalculator23Display.SelectTangentArray = 'None'
pythonCalculator23Display.OSPRayScaleArray = 'currK3X'
pythonCalculator23Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator23Display.SelectOrientationVectors = 'None'
pythonCalculator23Display.ScaleFactor = 12.0
pythonCalculator23Display.SelectScaleArray = 'None'
pythonCalculator23Display.GlyphType = 'Arrow'
pythonCalculator23Display.GlyphTableIndexArray = 'None'
pythonCalculator23Display.GaussianRadius = 0.6
pythonCalculator23Display.SetScaleArray = ['POINTS', 'currK3X']
pythonCalculator23Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator23Display.OpacityArray = ['POINTS', 'currK3X']
pythonCalculator23Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator23Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator23Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator23Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator23Display.OpacityArrayName = ['POINTS', 'currK3X']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator23Display.ScaleTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator23Display.OpacityTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator23Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator23Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator23Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator23Display.DataAxesGrid.XTitleBold = 1
pythonCalculator23Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator23Display.DataAxesGrid.YTitleBold = 1
pythonCalculator23Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator23Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator23Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator23Display.DataAxesGrid.XLabelBold = 1
pythonCalculator23Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator23Display.DataAxesGrid.YLabelBold = 1
pythonCalculator23Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator23Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator23Display.DataAxesGrid.ZLabelFontSize = 17


#########################################################################################

# create a new 'Python Calculator'
pythonCalculator24 = PythonCalculator(registrationName='PythonCalculator24', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

## mass current K3 contribution formilism:
# -u111 v1i - u212 v1i - u313 v1i
# -u121 v2i - u222 v2i - u323 v2i
# -u131 v3i - u232 v3i - u333 v3i
# +u1i v111 + u2i v121 + u3i v131
# +u1i v212 + u2i v222 + u3i v232
# +u1i v313 + u2i v323 + u3i v333


# Properties modified on pythonCalculator24, i = 2 i.e., Y
# pythonCalculator24.Expression = "-inputs[2].PointData['u_i12'][:,0]*inputs[0].PointData['v_11']-inputs[2].PointData['u_i12'][:,1]*inputs[0].PointData['v_12']-inputs[2].PointData['u_i12'][:,2]*inputs[0].PointData['v_13']-inputs[5].PointData['u_i22'][:,0]*inputs[0].PointData['v_21']-inputs[5].PointData['u_i22'][:,1]*inputs[0].PointData['v_22']-inputs[5].PointData['u_i22'][:,2]*inputs[0].PointData['v_23']-inputs[8].PointData['u_i32'][:,0]*inputs[0].PointData['v_31']-inputs[8].PointData['u_i32'][:,1]*inputs[0].PointData['v_32']-inputs[8].PointData['u_i32'][:,2]*inputs[0].PointData['v_33']+inputs[0].PointData['u_11']*inputs[11].PointData['v_i12'][:,0]+inputs[0].PointData['u_21']*inputs[14].PointData['v_i22'][:,0]+inputs[0].PointData['u_31']*inputs[17].PointData['v_i32'][:,0]+inputs[0].PointData['u_12']*inputs[11].PointData['v_i12'][:,1]+inputs[0].PointData['u_22']*inputs[14].PointData['v_i22'][:,1]+inputs[0].PointData['u_32']*inputs[17].PointData['v_i32'][:,1]+inputs[0].PointData['u_13']*inputs[11].PointData['v_i12'][:,2]+inputs[0].PointData['u_23']*inputs[14].PointData['v_i22'][:,2]+inputs[0].PointData['u_33']*inputs[17].PointData['v_i32'][:,2]"

# Properties modified on pythonCalculator24, i = 2 i.e., Y
pythonCalculator24.Expression = "-inputs[1].PointData['u_i11'][:,0]*inputs[0].PointData['v_12']-inputs[2].PointData['u_i12'][:,1]*inputs[0].PointData['v_12']-inputs[3].PointData['u_i13'][:,2]*inputs[0].PointData['v_12']-inputs[4].PointData['u_i21'][:,0]*inputs[0].PointData['v_22']-inputs[5].PointData['u_i22'][:,1]*inputs[0].PointData['v_22']-inputs[6].PointData['u_i23'][:,2]*inputs[0].PointData['v_22']-inputs[7].PointData['u_i31'][:,0]*inputs[0].PointData['v_32']-inputs[8].PointData['u_i32'][:,1]*inputs[0].PointData['v_32']-inputs[9].PointData['u_i33'][:,2]*inputs[0].PointData['v_32']+inputs[0].PointData['u_12']*inputs[10].PointData['v_i11'][:,0]+inputs[0].PointData['u_22']*inputs[13].PointData['v_i21'][:,0]+inputs[0].PointData['u_32']*inputs[16].PointData['v_i31'][:,0]+inputs[0].PointData['u_12']*inputs[11].PointData['v_i12'][:,1]+inputs[0].PointData['u_22']*inputs[14].PointData['v_i22'][:,1]+inputs[0].PointData['u_32']*inputs[17].PointData['v_i32'][:,1]+inputs[0].PointData['u_12']*inputs[12].PointData['v_i13'][:,2]+inputs[0].PointData['u_22']*inputs[15].PointData['v_i23'][:,2]+inputs[0].PointData['u_32']*inputs[18].PointData['v_i33'][:,2]"


pythonCalculator24.ArrayName = 'currK3Y'
pythonCalculator24.CopyArrays = 0

# show data in view
pythonCalculator24Display = Show(pythonCalculator24, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator24Display.Representation = 'Surface'
pythonCalculator24Display.ColorArrayName = [None, '']
pythonCalculator24Display.SelectTCoordArray = 'None'
pythonCalculator24Display.SelectNormalArray = 'None'
pythonCalculator24Display.SelectTangentArray = 'None'
pythonCalculator24Display.OSPRayScaleArray = 'currK3Y'
pythonCalculator24Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator24Display.SelectOrientationVectors = 'None'
pythonCalculator24Display.ScaleFactor = 12.0
pythonCalculator24Display.SelectScaleArray = 'None'
pythonCalculator24Display.GlyphType = 'Arrow'
pythonCalculator24Display.GlyphTableIndexArray = 'None'
pythonCalculator24Display.GaussianRadius = 0.6
pythonCalculator24Display.SetScaleArray = ['POINTS', 'currK3Y']
pythonCalculator24Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator24Display.OpacityArray = ['POINTS', 'currK3Y']
pythonCalculator24Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator24Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator24Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator24Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator24Display.OpacityArrayName = ['POINTS', 'currK3Y']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator24Display.ScaleTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator24Display.OpacityTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator24Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator24Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator24Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator24Display.DataAxesGrid.XTitleBold = 1
pythonCalculator24Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator24Display.DataAxesGrid.YTitleBold = 1
pythonCalculator24Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator24Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator24Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator24Display.DataAxesGrid.XLabelBold = 1
pythonCalculator24Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator24Display.DataAxesGrid.YLabelBold = 1
pythonCalculator24Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator24Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator24Display.DataAxesGrid.ZLabelFontSize = 17


#########################################################################################

# create a new 'Python Calculator'
pythonCalculator25 = PythonCalculator(registrationName='PythonCalculator25', Input=[output_conf_00pvtu, pythonCalculator1, pythonCalculator2, pythonCalculator3, pythonCalculator4, pythonCalculator5, pythonCalculator6, pythonCalculator7, pythonCalculator8, pythonCalculator9, pythonCalculator10, pythonCalculator11, pythonCalculator12, pythonCalculator13, pythonCalculator14, pythonCalculator15, pythonCalculator16, pythonCalculator17, pythonCalculator18])

## mass current K3 contribution formilism:
# -u111 v1i - u212 v1i - u313 v1i
# -u121 v2i - u222 v2i - u323 v2i
# -u131 v3i - u232 v3i - u333 v3i
# +u1i v111 + u2i v121 + u3i v131
# +u1i v212 + u2i v222 + u3i v232
# +u1i v313 + u2i v323 + u3i v333

# Properties modified on pythonCalculator25, i = 3 i.e., z
pythonCalculator25.Expression = "-inputs[1].PointData['u_i11'][:,0]*inputs[0].PointData['v_13']-inputs[2].PointData['u_i12'][:,1]*inputs[0].PointData['v_13']-inputs[3].PointData['u_i13'][:,2]*inputs[0].PointData['v_13']-inputs[4].PointData['u_i21'][:,0]*inputs[0].PointData['v_23']-inputs[5].PointData['u_i22'][:,1]*inputs[0].PointData['v_23']-inputs[6].PointData['u_i23'][:,2]*inputs[0].PointData['v_23']-inputs[7].PointData['u_i31'][:,0]*inputs[0].PointData['v_33']-inputs[8].PointData['u_i32'][:,1]*inputs[0].PointData['v_33']-inputs[9].PointData['u_i33'][:,2]*inputs[0].PointData['v_33']+inputs[0].PointData['u_13']*inputs[10].PointData['v_i11'][:,0]+inputs[0].PointData['u_23']*inputs[13].PointData['v_i21'][:,0]+inputs[0].PointData['u_33']*inputs[16].PointData['v_i31'][:,0]+inputs[0].PointData['u_13']*inputs[11].PointData['v_i12'][:,1]+inputs[0].PointData['u_23']*inputs[14].PointData['v_i22'][:,1]+inputs[0].PointData['u_33']*inputs[17].PointData['v_i32'][:,1]+inputs[0].PointData['u_13']*inputs[12].PointData['v_i13'][:,2]+inputs[0].PointData['u_23']*inputs[15].PointData['v_i23'][:,2]+inputs[0].PointData['u_33']*inputs[18].PointData['v_i33'][:,2]"






pythonCalculator25.ArrayName = 'currK3Z'
pythonCalculator25.CopyArrays = 0

# show data in view
pythonCalculator25Display = Show(pythonCalculator25, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pythonCalculator25Display.Representation = 'Surface'
pythonCalculator25Display.ColorArrayName = [None, '']
pythonCalculator25Display.SelectTCoordArray = 'None'
pythonCalculator25Display.SelectNormalArray = 'None'
pythonCalculator25Display.SelectTangentArray = 'None'
pythonCalculator25Display.OSPRayScaleArray = 'currK3Z'
pythonCalculator25Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator25Display.SelectOrientationVectors = 'None'
pythonCalculator25Display.ScaleFactor = 12.0
pythonCalculator25Display.SelectScaleArray = 'None'
pythonCalculator25Display.GlyphType = 'Arrow'
pythonCalculator25Display.GlyphTableIndexArray = 'None'
pythonCalculator25Display.GaussianRadius = 0.6
pythonCalculator25Display.SetScaleArray = ['POINTS', 'currK3Z']
pythonCalculator25Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator25Display.OpacityArray = ['POINTS', 'currK3Z']
pythonCalculator25Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator25Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator25Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator25Display.ScalarOpacityUnitDistance = 2.5028001676159013
pythonCalculator25Display.OpacityArrayName = ['POINTS', 'currK3Z']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator25Display.ScaleTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator25Display.OpacityTransferFunction.Points = [-0.03405359625602345, 0.0, 0.5, 0.0, 0.03396098221510176, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pythonCalculator25Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
pythonCalculator25Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
pythonCalculator25Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
pythonCalculator25Display.DataAxesGrid.XTitleBold = 1
pythonCalculator25Display.DataAxesGrid.XTitleFontSize = 24
pythonCalculator25Display.DataAxesGrid.YTitleBold = 1
pythonCalculator25Display.DataAxesGrid.YTitleFontSize = 24
pythonCalculator25Display.DataAxesGrid.ZTitleBold = 1
pythonCalculator25Display.DataAxesGrid.ZTitleFontSize = 23
pythonCalculator25Display.DataAxesGrid.XLabelBold = 1
pythonCalculator25Display.DataAxesGrid.XLabelFontSize = 17
pythonCalculator25Display.DataAxesGrid.YLabelBold = 1
pythonCalculator25Display.DataAxesGrid.YLabelFontSize = 17
pythonCalculator25Display.DataAxesGrid.ZLabelBold = 1
pythonCalculator25Display.DataAxesGrid.ZLabelFontSize = 17


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


# update the view to ensure updated data information
# renderView1.Update()

# Properties modified on pythonCalculator25
# pythonCalculator25.CopyArrays = 0

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
# layout1.SetSize(931, 1120)
layout1.SetSize(1922, 1120)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
# renderView1.CameraPosition = [0.0, 0.0, 368.3884445988151]
# renderView1.CameraViewUp = [0.0, 0.9999842640648654, 0.005609957455249585]
# renderView1.CameraParallelScale = 96.34839743002567
renderView1.CameraPosition = [0.0, -1.7359591081103158, 309.43760358574116]
renderView1.CameraViewUp = [0.0, 0.9999842640648654, 0.005609957455249585]
renderView1.CameraParallelScale = 80.08960536370884

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
