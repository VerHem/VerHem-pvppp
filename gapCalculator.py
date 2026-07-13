# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
output_conf_00pvtu = FindSource('output_conf_00.pvtu')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=output_conf_00pvtu)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'gap'
calculator1.Function = 'sqrt(u_11^2+u_12^2+u_13^2+u_21^2+u_22^2+u_23^2+u_31^2+u_32^2+u_33^2+v_11^2+v_12^2+v_13^2+v_21^2+v_22^2+v_23^2+v_31^2+v_32^2+v_33^2)'

# get active view
# renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
# calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'gap'
# gapLUT = GetColorTransferFunction('gap')
# gapLUT.RGBPoints = [3.259890219342394, 0.231373, 0.298039, 0.752941, 3.4514874995122438, 0.865003, 0.865003, 0.865003, 3.6430847796820935, 0.705882, 0.0156863, 0.14902]
# gapLUT.ScalarRangeInitialized = 1.0

# # get opacity transfer function/opacity map for 'gap'
# gapPWF = GetOpacityTransferFunction('gap')
# gapPWF.Points = [3.259890219342394, 0.0, 0.5, 0.0, 3.6430847796820935, 1.0, 0.5, 0.0]
# gapPWF.ScalarRangeInitialized = 1

# # trace defaults for the display properties.
# calculator1Display.Representation = 'Surface'
# calculator1Display.ColorArrayName = ['POINTS', 'gap']
# calculator1Display.LookupTable = gapLUT
# calculator1Display.SelectTCoordArray = 'None'
# calculator1Display.SelectNormalArray = 'None'
# calculator1Display.SelectTangentArray = 'None'
# calculator1Display.OSPRayScaleArray = 'gap'
# calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# calculator1Display.SelectOrientationVectors = 'None'
# calculator1Display.ScaleFactor = 3.0
# calculator1Display.SelectScaleArray = 'gap'
# calculator1Display.GlyphType = 'Arrow'
# calculator1Display.GlyphTableIndexArray = 'gap'
# calculator1Display.GaussianRadius = 0.15
# calculator1Display.SetScaleArray = ['POINTS', 'gap']
# calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
# calculator1Display.OpacityArray = ['POINTS', 'gap']
# calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
# calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
# calculator1Display.PolarAxes = 'PolarAxesRepresentation'
# calculator1Display.ScalarOpacityFunction = gapPWF
# calculator1Display.ScalarOpacityUnitDistance = 0.9742785792574935
# calculator1Display.OpacityArrayName = ['POINTS', 'gap']

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# calculator1Display.ScaleTransferFunction.Points = [3.259890219342394, 0.0, 0.5, 0.0, 3.6430847796820935, 1.0, 0.5, 0.0]

# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# calculator1Display.OpacityTransferFunction.Points = [3.259890219342394, 0.0, 0.5, 0.0, 3.6430847796820935, 1.0, 0.5, 0.0]

# # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
# calculator1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
# calculator1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
# calculator1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
# calculator1Display.DataAxesGrid.XTitleBold = 1
# calculator1Display.DataAxesGrid.XTitleFontSize = 24
# calculator1Display.DataAxesGrid.YTitleBold = 1
# calculator1Display.DataAxesGrid.YTitleFontSize = 24
# calculator1Display.DataAxesGrid.ZTitleBold = 1
# calculator1Display.DataAxesGrid.ZTitleFontSize = 23
# calculator1Display.DataAxesGrid.XLabelBold = 1
# calculator1Display.DataAxesGrid.XLabelFontSize = 17
# calculator1Display.DataAxesGrid.YLabelBold = 1
# calculator1Display.DataAxesGrid.YLabelFontSize = 17
# calculator1Display.DataAxesGrid.ZLabelBold = 1
# calculator1Display.DataAxesGrid.ZLabelFontSize = 17

# # reset view to fit data
# renderView1.ResetCamera(False)

# # get the material library
# materialLibrary1 = GetMaterialLibrary()

# # show color bar/color legend
# calculator1Display.SetScalarBarVisibility(renderView1, True)

# # update the view to ensure updated data information
# renderView1.Update()

# hide data in view
# Hide(calculator1, renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
# layout1 = GetLayout()

# #--------------------------------
# # saving layout sizes for layouts

# # layout/tab size in pixels
# layout1.SetSize(1429, 1120)

# #-----------------------------------
# # saving camera placements for views

# # current camera placement for renderView1
# renderView1.CameraPosition = [-0.5296335975714092, -60.22589734014029, 0.3378798368587227]
# renderView1.CameraViewUp = [2.4666402156508206e-05, 0.005609903227179151, 0.9999842640648654]
# renderView1.CameraParallelScale = 15.588457268119896

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
