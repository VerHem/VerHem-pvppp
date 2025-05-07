# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [639, 874]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.040289878845214844, -0.0022296905517578125, -0.012837409973144531]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [214.825, -0.0022296899999999995, -0.012837400000000443]
renderView1.CameraFocalPoint = [0.00234604, -0.0540686, -4.08366]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 56.47791343909125
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [646, 874]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [0.040289878845214844, -0.0022296905517578125, -0.012837409973144531]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [214.825, -0.0022296899999999995, -0.012837400000000443]
renderView2.CameraFocalPoint = [0.00234604, -0.0540686, -4.08366]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 56.47791343909125
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [645, 874]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.CenterOfRotation = [0.040289878845214844, -0.0022296905517578125, -0.012837409973144531]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [214.825, -0.0022296899999999995, -0.012837400000000443]
renderView3.CameraFocalPoint = [0.00234604, -0.0540686, -4.08366]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 56.47791343909125
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.330266)
layout1.AssignView(1, renderView1)
layout1.SplitHorizontal(2, 0.500000)
layout1.AssignView(5, renderView2)
layout1.AssignView(6, renderView3)
layout1.SetSize(1932, 874)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView3)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Partitioned Unstructured Grid Reader'
solution_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='solution_00.pvtu', FileName=['/home/heidi/Documents/VerHem-repo_and_data/visualization-and-data/xyzAdGR/VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-monople-config-run-4/refine-cycle_2/solution_09.pvtu'])
solution_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']
solution_00pvtu.TimeArray = 'None'

# create a new 'Merge Vector Components'
mergeVectorComponents2 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=solution_00pvtu)
mergeVectorComponents2.XArray = 'v_11'
mergeVectorComponents2.YArray = 'v_12'
mergeVectorComponents2.ZArray = 'v_13'
mergeVectorComponents2.OutputVectorName = 'N'

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=solution_00pvtu)
mergeVectorComponents1.XArray = 'u_11'
mergeVectorComponents1.YArray = 'u_12'
mergeVectorComponents1.ZArray = 'u_13'
mergeVectorComponents1.OutputVectorName = 'M'

# create a new 'XML Partitioned Unstructured Grid Reader'
solution_12pvtu = XMLPartitionedUnstructuredGridReader(registrationName='solution_12.pvtu', FileName=['/home/heidi/Documents/VerHem-repo_and_data/visualization-and-data/xyzAdGR/VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-monople-config-run-4/refine-cycle_2/solution_09.pvtu'])
solution_12pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']
solution_12pvtu.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=solution_12pvtu)
calculator1.ResultArrayName = 'gap'
calculator1.Function = 'sqrt(u_11^2+u_12^2+u_13^2+u_21^2+u_22^2+u_23^2+u_31^2+u_32^2+u_33^2+v_11^2+v_12^2+v_13^2+v_21^2+v_22^2+v_23^2+v_31^2+v_32^2+v_33^2)'

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[mergeVectorComponents1, mergeVectorComponents2])

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=appendAttributes1)
calculator3.ResultArrayName = 'n'
calculator3.Function = 'norm(N)'

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=appendAttributes1)
calculator2.ResultArrayName = 'm'
calculator2.Function = 'norm(M)'

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=calculator1)
contour1.ContourBy = ['POINTS', 'gap']
contour1.Isosurfaces = [1.9]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Calculator'
calculator1_1 = Calculator(registrationName='Calculator1', Input=appendAttributes1)
calculator1_1.ResultArrayName = 'l'
calculator1_1.Function = 'cross(M,N)/((2.49733/1.414213562)^2)'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculator1_1,
    SeedType='Point Cloud')
streamTracer1.Vectors = ['POINTS', 'l']
streamTracer1.MaximumStreamlineLength = 36.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer1.SeedType.NumberOfPoints = 4000
streamTracer1.SeedType.Radius = 40.0

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'l']
tube1.Radius = 0.14758005867004392

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(registrationName='StreamTracer2', Input=calculator2,
    SeedType='Point Cloud')
streamTracer2.Vectors = ['POINTS', 'm']
streamTracer2.MaximumStreamlineLength = 60.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer2.SeedType.NumberOfPoints = 2000
streamTracer2.SeedType.Radius = 40.0

# create a new 'Tube'
tube2 = Tube(registrationName='Tube2', Input=streamTracer2)
tube2.Scalars = ['POINTS', 'AngularVelocity']
tube2.Vectors = ['POINTS', 'm']
tube2.Radius = 0.2878515197753906

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=tube2)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'AngularVelocity']
clip1.Value = -0.11061224878438514

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Normal = [1.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [-1.9073486328125e-06, 2.6702880859375e-05, -0.10199832916259766]

# create a new 'Stream Tracer'
streamTracer3 = StreamTracer(registrationName='StreamTracer3', Input=calculator3,
    SeedType='Point Cloud')
streamTracer3.Vectors = ['POINTS', 'n']
streamTracer3.MaximumSteps = 1000
streamTracer3.MaximumStreamlineLength = 60.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer3.SeedType.Center = [0.0, 0.0, -15.0]
streamTracer3.SeedType.Radius = 20.0

# create a new 'Tube'
tube3 = Tube(registrationName='Tube3', Input=streamTracer3)
tube3.Scalars = ['POINTS', 'AngularVelocity']
tube3.Vectors = ['POINTS', 'n']
tube3.Radius = 0.25669845542907715

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tube1
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'l'
lLUT = GetColorTransferFunction('l')
lLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5081255689845642, 0.865003, 0.865003, 0.865003, 1.0162511379691284, 0.705882, 0.0156863, 0.14902]
lLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = ['POINTS', 'l']
tube1Display.LookupTable = lLUT
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.ScaleFactor = 3.6007057189941407
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.GaussianRadius = 0.18003528594970702
tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-0.0017468127945454537, 0.0, 0.5, 0.0, 0.03703710146310884, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-0.0017468127945454537, 0.0, 0.5, 0.0, 0.03703710146310884, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_{0}$'
tube1Display.DataAxesGrid.XTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.XTitleBold = 1
tube1Display.DataAxesGrid.XTitleFontSize = 24
tube1Display.DataAxesGrid.YTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.YTitleBold = 1
tube1Display.DataAxesGrid.YTitleFontSize = 24
tube1Display.DataAxesGrid.ZTitleFontFamily = 'Times'
tube1Display.DataAxesGrid.ZTitleBold = 1
tube1Display.DataAxesGrid.ZTitleFontSize = 24
tube1Display.DataAxesGrid.XLabelFontFamily = 'Times'
tube1Display.DataAxesGrid.XLabelBold = 1
tube1Display.DataAxesGrid.XLabelFontSize = 18
tube1Display.DataAxesGrid.YLabelFontFamily = 'Times'
tube1Display.DataAxesGrid.YLabelBold = 1
tube1Display.DataAxesGrid.YLabelFontSize = 18
tube1Display.DataAxesGrid.ZLabelFontFamily = 'Times'
tube1Display.DataAxesGrid.ZLabelBold = 1
tube1Display.DataAxesGrid.ZLabelFontSize = 18

# setup the color legend parameters for each legend in this view

# get color legend/bar for lLUT in view renderView1
lLUTColorBar = GetScalarBar(lLUT, renderView1)
lLUTColorBar.Orientation = 'Horizontal'
lLUTColorBar.WindowLocation = 'Any Location'
lLUTColorBar.Position = [0.3390545418978517, 0.9127701046093495]
lLUTColorBar.Title = '$\\mathbf{l}$'
lLUTColorBar.ComponentTitle = ''
lLUTColorBar.TitleFontFamily = 'Times'
lLUTColorBar.TitleBold = 1
lLUTColorBar.TitleItalic = 1
lLUTColorBar.TitleFontSize = 19
lLUTColorBar.LabelFontFamily = 'Times'
lLUTColorBar.LabelBold = 1
lLUTColorBar.LabelItalic = 1
lLUTColorBar.LabelFontSize = 19
lLUTColorBar.ScalarBarLength = 0.32999999999999957

# set color bar visibility
lLUTColorBar.Visibility = 1

# show color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from clip1
clip1Display = Show(clip1, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'm'
mLUT = GetColorTransferFunction('m')
mLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5000000000000001, 0.865003, 0.865003, 0.865003, 1.0000000000000002, 0.705882, 0.0156863, 0.14902]
mLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'm'
mPWF = GetOpacityTransferFunction('m')
mPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0000000000000002, 1.0, 0.5, 0.0]
mPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'm']
clip1Display.LookupTable = mLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'TubeNormals'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'AngularVelocity'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'Normals'
clip1Display.ScaleFactor = 6.031807136535645
clip1Display.SelectScaleArray = 'AngularVelocity'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'AngularVelocity'
clip1Display.GaussianRadius = 0.30159035682678226
clip1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'AngularVelocity']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = mPWF
clip1Display.ScalarOpacityUnitDistance = 1.1778213460080713
clip1Display.OpacityArrayName = ['POINTS', 'AngularVelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-0.302737397718959, 0.0, 0.5, 0.0, 0.08607178927645193, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-0.302737397718959, 0.0, 0.5, 0.0, 0.08607178927645193, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display = Show(contour1, renderView2, 'GeometryRepresentation')

# get color transfer function/color map for 'gap'
gapLUT = GetColorTransferFunction('gap')
gapLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.2615471917570853, 0.865003, 0.865003, 0.865003, 2.5230943835141706, 0.705882, 0.0156863, 0.14902]
gapLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'gap']
contour1Display.LookupTable = gapLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'gap'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 6.0
contour1Display.SelectScaleArray = 'gap'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'gap'
contour1Display.GaussianRadius = 0.3
contour1Display.SetScaleArray = ['POINTS', 'gap']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'gap']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [1.85, 0.0, 0.5, 0.0, 1.850244164466858, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [1.85, 0.0, 0.5, 0.0, 1.850244164466858, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for mLUT in view renderView2
mLUTColorBar = GetScalarBar(mLUT, renderView2)
mLUTColorBar.Orientation = 'Horizontal'
mLUTColorBar.WindowLocation = 'Any Location'
mLUTColorBar.Position = [0.33181973480842725, 0.9036167865315463]
mLUTColorBar.Title = 'm'
mLUTColorBar.ComponentTitle = 'Magnitude'
mLUTColorBar.TitleFontFamily = 'Times'
mLUTColorBar.TitleBold = 1
mLUTColorBar.LabelFontFamily = 'Times'
mLUTColorBar.LabelBold = 1
mLUTColorBar.ScalarBarLength = 0.33000000000000024

# set color bar visibility
mLUTColorBar.Visibility = 1

# get color legend/bar for gapLUT in view renderView2
gapLUTColorBar = GetScalarBar(gapLUT, renderView2)
gapLUTColorBar.Orientation = 'Horizontal'
gapLUTColorBar.WindowLocation = 'Any Location'
gapLUTColorBar.Position = [0.3342122968116718, 0.06646820856489055]
gapLUTColorBar.Title = 'gap'
gapLUTColorBar.ComponentTitle = ''
gapLUTColorBar.ScalarBarLength = 0.3299999999999999

# set color bar visibility
gapLUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView2, True)

# show color legend
contour1Display.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from tube3
tube3Display = Show(tube3, renderView3, 'GeometryRepresentation')

# get color transfer function/color map for 'n'
nLUT = GetColorTransferFunction('n')
nLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5000000000000001, 0.865003, 0.865003, 0.865003, 1.0000000000000002, 0.705882, 0.0156863, 0.14902]
nLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = ['POINTS', 'n']
tube3Display.LookupTable = nLUT
tube3Display.SelectTCoordArray = 'None'
tube3Display.SelectNormalArray = 'TubeNormals'
tube3Display.SelectTangentArray = 'None'
tube3Display.OSPRayScaleArray = 'AngularVelocity'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'Normals'
tube3Display.ScaleFactor = 6.084593963623047
tube3Display.SelectScaleArray = 'AngularVelocity'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'AngularVelocity'
tube3Display.GaussianRadius = 0.30422969818115236
tube3Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube3Display.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display.DataAxesGrid = 'GridAxesRepresentation'
tube3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube3Display.ScaleTransferFunction.Points = [-0.13286091108408243, 0.0, 0.5, 0.0, 2.130264287049815, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube3Display.OpacityTransferFunction.Points = [-0.13286091108408243, 0.0, 0.5, 0.0, 2.130264287049815, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_1 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', 'gap']
contour1Display_1.LookupTable = gapLUT
contour1Display_1.SelectTCoordArray = 'None'
contour1Display_1.SelectNormalArray = 'Normals'
contour1Display_1.SelectTangentArray = 'None'
contour1Display_1.OSPRayScaleArray = 'gap'
contour1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_1.SelectOrientationVectors = 'None'
contour1Display_1.ScaleFactor = 6.0
contour1Display_1.SelectScaleArray = 'gap'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GlyphTableIndexArray = 'gap'
contour1Display_1.GaussianRadius = 0.3
contour1Display_1.SetScaleArray = ['POINTS', 'gap']
contour1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_1.OpacityArray = ['POINTS', 'gap']
contour1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_1.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_1.ScaleTransferFunction.Points = [1.9, 0.0, 0.5, 0.0, 1.900244116783142, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_1.OpacityTransferFunction.Points = [1.9, 0.0, 0.5, 0.0, 1.900244116783142, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for nLUT in view renderView3
nLUTColorBar = GetScalarBar(nLUT, renderView3)
nLUTColorBar.Orientation = 'Horizontal'
nLUTColorBar.WindowLocation = 'Any Location'
nLUTColorBar.Position = [0.3379326565387477, 0.9061564236678651]
nLUTColorBar.Title = 'n'
nLUTColorBar.ComponentTitle = 'Magnitude'
nLUTColorBar.TitleFontFamily = 'Times'
nLUTColorBar.TitleBold = 1
nLUTColorBar.LabelFontFamily = 'Times'
nLUTColorBar.LabelBold = 1
nLUTColorBar.ScalarBarLength = 0.32999999999999996

# set color bar visibility
nLUTColorBar.Visibility = 1

# get color legend/bar for gapLUT in view renderView3
gapLUTColorBar_1 = GetScalarBar(gapLUT, renderView3)
gapLUTColorBar_1.Orientation = 'Horizontal'
gapLUTColorBar_1.WindowLocation = 'Any Location'
gapLUTColorBar_1.Position = [0.3580444956440352, 0.06392857142857146]
gapLUTColorBar_1.Title = 'gap'
gapLUTColorBar_1.ComponentTitle = ''
gapLUTColorBar_1.ScalarBarLength = 0.3299999999999996

# set color bar visibility
gapLUTColorBar_1.Visibility = 1

# show color legend
tube3Display.SetScalarBarVisibility(renderView3, True)

# show color legend
contour1Display_1.SetScalarBarVisibility(renderView3, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'n'
nPWF = GetOpacityTransferFunction('n')
nPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0000000000000002, 1.0, 0.5, 0.0]
nPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'l'
lPWF = GetOpacityTransferFunction('l')
lPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0162511379691284, 1.0, 0.5, 0.0]
lPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'gap'
gapPWF = GetOpacityTransferFunction('gap')
gapPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.5230943835141706, 1.0, 0.5, 0.0]
gapPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(tube3)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='/home/heidi/Documents/VerHem-repo_and_data/paraview-pvpython-py-scripts/state-saved')