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
solution_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='solution_00.pvtu', FileName=['/home/heidi/Documents/VerHem-repo_and_data/visualization-and-data/xyzAdGR/VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-monople-config-run-6/refine-cycle_2/solution_00.pvtu'])
solution_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']
solution_00pvtu.TimeArray = 'None'

# create a new 'Merge Vector Components'
mergeVectorComponents2 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=solution_00pvtu)
mergeVectorComponents2.XArray = 'v_11'
mergeVectorComponents2.YArray = 'v_12'
mergeVectorComponents2.ZArray = 'v_13'
mergeVectorComponents2.OutputVectorName = 'N'

# create a new 'XML Partitioned Unstructured Grid Reader'
solution_12pvtu = XMLPartitionedUnstructuredGridReader(registrationName='solution_12.pvtu', FileName=['/home/heidi/Documents/VerHem-repo_and_data/visualization-and-data/xyzAdGR/VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-monople-config-run-6/refine-cycle_2/solution_00.pvtu'])
solution_12pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']
solution_12pvtu.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=solution_12pvtu)
calculator1.ResultArrayName = 'gap'
calculator1.Function = 'sqrt(u_11^2+u_12^2+u_13^2+u_21^2+u_22^2+u_23^2+u_31^2+u_32^2+u_33^2+v_11^2+v_12^2+v_13^2+v_21^2+v_22^2+v_23^2+v_31^2+v_32^2+v_33^2)'

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=calculator1)
contour1.ContourBy = ['POINTS', 'gap']
contour1.Isosurfaces = [1.9]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=solution_00pvtu)
mergeVectorComponents1.XArray = 'u_11'
mergeVectorComponents1.YArray = 'u_12'
mergeVectorComponents1.ZArray = 'u_13'
mergeVectorComponents1.OutputVectorName = 'M'

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[mergeVectorComponents1, mergeVectorComponents2])

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=appendAttributes1)
calculator2.ResultArrayName = 'm'
calculator2.Function = 'norm(M)'

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(registrationName='StreamTracer2', Input=calculator2,
    SeedType='Point Cloud')
streamTracer2.Vectors = ['POINTS', 'm']
streamTracer2.MaximumStreamlineLength = 60.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer2.SeedType.NumberOfPoints = 2000
streamTracer2.SeedType.Radius = 40.0

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

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=appendAttributes1)
calculator3.ResultArrayName = 'n'
calculator3.Function = 'norm(N)'

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
clip1.ClipType.Normal = [1.0, 0.0, 0.0]

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

# show data from solution_00pvtu
solution_00pvtuDisplay = Show(solution_00pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
solution_00pvtuDisplay.Representation = 'Surface'
solution_00pvtuDisplay.ColorArrayName = ['POINTS', '']
solution_00pvtuDisplay.SelectTCoordArray = 'None'
solution_00pvtuDisplay.SelectNormalArray = 'None'
solution_00pvtuDisplay.SelectTangentArray = 'None'
solution_00pvtuDisplay.OSPRayScaleArray = 'subdomain'
solution_00pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution_00pvtuDisplay.SelectOrientationVectors = 'None'
solution_00pvtuDisplay.ScaleFactor = 3.6
solution_00pvtuDisplay.SelectScaleArray = 'None'
solution_00pvtuDisplay.GlyphType = 'Arrow'
solution_00pvtuDisplay.GlyphTableIndexArray = 'None'
solution_00pvtuDisplay.GaussianRadius = 0.18
solution_00pvtuDisplay.SetScaleArray = ['POINTS', 'subdomain']
solution_00pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution_00pvtuDisplay.OpacityArray = ['POINTS', 'subdomain']
solution_00pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution_00pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution_00pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
solution_00pvtuDisplay.ScalarOpacityUnitDistance = 0.8694017339527222
solution_00pvtuDisplay.OpacityArrayName = ['POINTS', 'subdomain']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution_00pvtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution_00pvtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# show data from mergeVectorComponents1
mergeVectorComponents1Display = Show(mergeVectorComponents1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents1Display.Representation = 'Surface'
mergeVectorComponents1Display.ColorArrayName = ['POINTS', '']
mergeVectorComponents1Display.SelectTCoordArray = 'None'
mergeVectorComponents1Display.SelectNormalArray = 'None'
mergeVectorComponents1Display.SelectTangentArray = 'None'
mergeVectorComponents1Display.OSPRayScaleArray = 'M'
mergeVectorComponents1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.SelectOrientationVectors = 'M'
mergeVectorComponents1Display.ScaleFactor = 3.6
mergeVectorComponents1Display.SelectScaleArray = 'M'
mergeVectorComponents1Display.GlyphType = 'Arrow'
mergeVectorComponents1Display.GlyphTableIndexArray = 'M'
mergeVectorComponents1Display.GaussianRadius = 0.18
mergeVectorComponents1Display.SetScaleArray = ['POINTS', 'M']
mergeVectorComponents1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.OpacityArray = ['POINTS', 'M']
mergeVectorComponents1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents1Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents1Display.ScalarOpacityUnitDistance = 0.8694017339527222
mergeVectorComponents1Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# show data from mergeVectorComponents2
mergeVectorComponents2Display = Show(mergeVectorComponents2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents2Display.Representation = 'Surface'
mergeVectorComponents2Display.ColorArrayName = ['POINTS', '']
mergeVectorComponents2Display.SelectTCoordArray = 'None'
mergeVectorComponents2Display.SelectNormalArray = 'None'
mergeVectorComponents2Display.SelectTangentArray = 'None'
mergeVectorComponents2Display.OSPRayScaleArray = 'N'
mergeVectorComponents2Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.SelectOrientationVectors = 'N'
mergeVectorComponents2Display.ScaleFactor = 3.6
mergeVectorComponents2Display.SelectScaleArray = 'N'
mergeVectorComponents2Display.GlyphType = 'Arrow'
mergeVectorComponents2Display.GlyphTableIndexArray = 'N'
mergeVectorComponents2Display.GaussianRadius = 0.18
mergeVectorComponents2Display.SetScaleArray = ['POINTS', 'N']
mergeVectorComponents2Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.OpacityArray = ['POINTS', 'N']
mergeVectorComponents2Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents2Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents2Display.ScalarOpacityUnitDistance = 0.8694017339527222
mergeVectorComponents2Display.OpacityArrayName = ['POINTS', 'N']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents2Display.ScaleTransferFunction.Points = [-1.4717285633087158, 0.0, 0.5, 0.0, 1.5255942344665527, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents2Display.OpacityTransferFunction.Points = [-1.4717285633087158, 0.0, 0.5, 0.0, 1.5255942344665527, 1.0, 0.5, 0.0]

# show data from appendAttributes1
appendAttributes1Display = Show(appendAttributes1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Surface'
appendAttributes1Display.ColorArrayName = ['POINTS', '']
appendAttributes1Display.SelectTCoordArray = 'None'
appendAttributes1Display.SelectNormalArray = 'None'
appendAttributes1Display.SelectTangentArray = 'None'
appendAttributes1Display.OSPRayScaleArray = 'M'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'M'
appendAttributes1Display.ScaleFactor = 3.6
appendAttributes1Display.SelectScaleArray = 'M'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'M'
appendAttributes1Display.GaussianRadius = 0.18
appendAttributes1Display.SetScaleArray = ['POINTS', 'M']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'M']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityUnitDistance = 0.8694017339527222
appendAttributes1Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# show data from calculator1_1
calculator1_1Display = Show(calculator1_1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'
calculator1_1Display.ColorArrayName = ['POINTS', '']
calculator1_1Display.SelectTCoordArray = 'None'
calculator1_1Display.SelectNormalArray = 'None'
calculator1_1Display.SelectTangentArray = 'None'
calculator1_1Display.OSPRayScaleArray = 'M'
calculator1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_1Display.SelectOrientationVectors = 'l'
calculator1_1Display.ScaleFactor = 3.6
calculator1_1Display.SelectScaleArray = 'M'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'M'
calculator1_1Display.GaussianRadius = 0.18
calculator1_1Display.SetScaleArray = ['POINTS', 'M']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = ['POINTS', 'M']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.ScalarOpacityUnitDistance = 0.8694017339527222
calculator1_1Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.7504940032958984, 1.0, 0.5, 0.0]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', '']
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 3.599513626098633
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.17997568130493163
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-0.0017468127945454537, 0.0, 0.5, 0.0, 0.03703710146310884, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-0.0017468127945454537, 0.0, 0.5, 0.0, 0.03703710146310884, 1.0, 0.5, 0.0]

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

# show data from calculator2
calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = [None, '']
calculator2Display.SelectTCoordArray = 'None'
calculator2Display.SelectNormalArray = 'None'
calculator2Display.SelectTangentArray = 'None'
calculator2Display.OSPRayScaleArray = 'M'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'm'
calculator2Display.ScaleFactor = 6.0
calculator2Display.SelectScaleArray = 'M'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'M'
calculator2Display.GaussianRadius = 0.3
calculator2Display.SetScaleArray = ['POINTS', 'M']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'M']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 1.288470508005519
calculator2Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.8430583477020264, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.8430583477020264, 1.0, 0.5, 0.0]

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

# get color transfer function/color map for 'subdomain'
subdomainLUT = GetColorTransferFunction('subdomain')
subdomainLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 127.5, 0.865003, 0.865003, 0.865003, 255.0, 0.705882, 0.0156863, 0.14902]
subdomainLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for subdomainLUT in view renderView1
subdomainLUTColorBar = GetScalarBar(subdomainLUT, renderView1)
subdomainLUTColorBar.Title = 'subdomain'
subdomainLUTColorBar.ComponentTitle = ''

# set color bar visibility
subdomainLUTColorBar.Visibility = 0

# get color transfer function/color map for 'subdomain_input_1'
subdomain_input_1LUT = GetColorTransferFunction('subdomain_input_1')
subdomain_input_1LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 127.5, 0.865003, 0.865003, 0.865003, 255.0, 0.705882, 0.0156863, 0.14902]
subdomain_input_1LUT.ScalarRangeInitialized = 1.0

# get color legend/bar for subdomain_input_1LUT in view renderView1
subdomain_input_1LUTColorBar = GetScalarBar(subdomain_input_1LUT, renderView1)
subdomain_input_1LUTColorBar.Title = 'subdomain_input_1'
subdomain_input_1LUTColorBar.ComponentTitle = ''

# set color bar visibility
subdomain_input_1LUTColorBar.Visibility = 0

# get color transfer function/color map for 'u_11'
u_11LUT = GetColorTransferFunction('u_11')
u_11LUT.RGBPoints = [3.553301576175727e-05, 0.231373, 0.298039, 0.752941, 0.8746152563417127, 0.865003, 0.865003, 0.865003, 1.7491949796676636, 0.705882, 0.0156863, 0.14902]
u_11LUT.ScalarRangeInitialized = 1.0

# get color legend/bar for u_11LUT in view renderView1
u_11LUTColorBar = GetScalarBar(u_11LUT, renderView1)
u_11LUTColorBar.Title = 'u_11'
u_11LUTColorBar.ComponentTitle = ''

# set color bar visibility
u_11LUTColorBar.Visibility = 0

# hide data in view
Hide(solution_00pvtu, renderView1)

# hide data in view
Hide(mergeVectorComponents1, renderView1)

# hide data in view
Hide(mergeVectorComponents2, renderView1)

# hide data in view
Hide(appendAttributes1, renderView1)

# hide data in view
Hide(calculator1_1, renderView1)

# hide data in view
Hide(streamTracer1, renderView1)

# show color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(calculator2, renderView1)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from calculator2
calculator2Display_1 = Show(calculator2, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator2Display_1.Representation = 'Surface'
calculator2Display_1.ColorArrayName = [None, '']
calculator2Display_1.SelectTCoordArray = 'None'
calculator2Display_1.SelectNormalArray = 'None'
calculator2Display_1.SelectTangentArray = 'None'
calculator2Display_1.OSPRayScaleArray = 'M'
calculator2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display_1.SelectOrientationVectors = 'm'
calculator2Display_1.ScaleFactor = 6.0
calculator2Display_1.SelectScaleArray = 'M'
calculator2Display_1.GlyphType = 'Arrow'
calculator2Display_1.GlyphTableIndexArray = 'M'
calculator2Display_1.GaussianRadius = 0.3
calculator2Display_1.SetScaleArray = ['POINTS', 'M']
calculator2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display_1.OpacityArray = ['POINTS', 'M']
calculator2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display_1.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display_1.PolarAxes = 'PolarAxesRepresentation'
calculator2Display_1.ScalarOpacityUnitDistance = 1.288470508005519
calculator2Display_1.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.8430583477020264, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.8430583477020264, 1.0, 0.5, 0.0]

# show data from streamTracer2
streamTracer2Display = Show(streamTracer2, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer2Display.Representation = 'Surface'
streamTracer2Display.ColorArrayName = [None, '']
streamTracer2Display.SelectTCoordArray = 'None'
streamTracer2Display.SelectNormalArray = 'None'
streamTracer2Display.SelectTangentArray = 'None'
streamTracer2Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer2Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer2Display.SelectOrientationVectors = 'Normals'
streamTracer2Display.ScaleFactor = 5.9998662948608406
streamTracer2Display.SelectScaleArray = 'AngularVelocity'
streamTracer2Display.GlyphType = 'Arrow'
streamTracer2Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer2Display.GaussianRadius = 0.29999331474304197
streamTracer2Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer2Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer2Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer2Display.ScaleTransferFunction.Points = [-0.3105265582886515, 0.0, 0.5, 0.0, 0.14634774044042437, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer2Display.OpacityTransferFunction.Points = [-0.3105265582886515, 0.0, 0.5, 0.0, 0.14634774044042437, 1.0, 0.5, 0.0]

# show data from tube2
tube2Display = Show(tube2, renderView2, 'GeometryRepresentation')

# get color transfer function/color map for 'm'
mLUT = GetColorTransferFunction('m')
mLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5000000000000001, 0.865003, 0.865003, 0.865003, 1.0000000000000002, 0.705882, 0.0156863, 0.14902]
mLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = ['POINTS', 'm']
tube2Display.LookupTable = mLUT
tube2Display.SelectTCoordArray = 'None'
tube2Display.SelectNormalArray = 'TubeNormals'
tube2Display.SelectTangentArray = 'None'
tube2Display.OSPRayScaleArray = 'AngularVelocity'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Normals'
tube2Display.ScaleFactor = 6.1048078536987305
tube2Display.SelectScaleArray = 'AngularVelocity'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'AngularVelocity'
tube2Display.GaussianRadius = 0.3052403926849365
tube2Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display.ScaleTransferFunction.Points = [-0.31093452636825575, 0.0, 0.5, 0.0, 0.08437953948871735, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display.OpacityTransferFunction.Points = [-0.31093452636825575, 0.0, 0.5, 0.0, 0.08437953948871735, 1.0, 0.5, 0.0]

# show data from clip1
clip1Display = Show(clip1, renderView2, 'UnstructuredGridRepresentation')

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

# show data from solution_12pvtu
solution_12pvtuDisplay = Show(solution_12pvtu, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
solution_12pvtuDisplay.Representation = 'Surface'
solution_12pvtuDisplay.ColorArrayName = ['POINTS', '']
solution_12pvtuDisplay.SelectTCoordArray = 'None'
solution_12pvtuDisplay.SelectNormalArray = 'None'
solution_12pvtuDisplay.SelectTangentArray = 'None'
solution_12pvtuDisplay.OSPRayScaleArray = 'subdomain'
solution_12pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solution_12pvtuDisplay.SelectOrientationVectors = 'None'
solution_12pvtuDisplay.ScaleFactor = 6.0
solution_12pvtuDisplay.SelectScaleArray = 'None'
solution_12pvtuDisplay.GlyphType = 'Arrow'
solution_12pvtuDisplay.GlyphTableIndexArray = 'None'
solution_12pvtuDisplay.GaussianRadius = 0.3
solution_12pvtuDisplay.SetScaleArray = ['POINTS', 'subdomain']
solution_12pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solution_12pvtuDisplay.OpacityArray = ['POINTS', 'subdomain']
solution_12pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solution_12pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
solution_12pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
solution_12pvtuDisplay.ScalarOpacityUnitDistance = 5.153882032022076
solution_12pvtuDisplay.OpacityArrayName = ['POINTS', 'subdomain']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solution_12pvtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solution_12pvtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# show data from calculator1
calculator1Display = Show(calculator1, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'gap'
gapLUT = GetColorTransferFunction('gap')
gapLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.2615471917570853, 0.865003, 0.865003, 0.865003, 2.5230943835141706, 0.705882, 0.0156863, 0.14902]
gapLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'gap'
gapPWF = GetOpacityTransferFunction('gap')
gapPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.5230943835141706, 1.0, 0.5, 0.0]
gapPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'gap']
calculator1Display.LookupTable = gapLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'gap'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 6.0
calculator1Display.SelectScaleArray = 'gap'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'gap'
calculator1Display.GaussianRadius = 0.3
calculator1Display.SetScaleArray = ['POINTS', 'gap']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'gap']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = gapPWF
calculator1Display.ScalarOpacityUnitDistance = 5.153882032022076
calculator1Display.OpacityArrayName = ['POINTS', 'gap']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5230943835141706, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5230943835141706, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitle = '$x/\\xi^{GL}_0$'
calculator1Display.DataAxesGrid.YTitle = '$y/\\xi^{GL}_0$'
calculator1Display.DataAxesGrid.ZTitle = '$z/\\xi^{GL}_0$'
calculator1Display.DataAxesGrid.XTitleFontFamily = 'Times'
calculator1Display.DataAxesGrid.XTitleBold = 1
calculator1Display.DataAxesGrid.XTitleFontSize = 24
calculator1Display.DataAxesGrid.YTitleFontFamily = 'Times'
calculator1Display.DataAxesGrid.YTitleBold = 1
calculator1Display.DataAxesGrid.YTitleFontSize = 24
calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Times'
calculator1Display.DataAxesGrid.ZTitleBold = 1
calculator1Display.DataAxesGrid.ZTitleFontSize = 24
calculator1Display.DataAxesGrid.XLabelFontFamily = 'Times'
calculator1Display.DataAxesGrid.XLabelBold = 1
calculator1Display.DataAxesGrid.XLabelFontSize = 18
calculator1Display.DataAxesGrid.YLabelFontFamily = 'Times'
calculator1Display.DataAxesGrid.YLabelBold = 1
calculator1Display.DataAxesGrid.YLabelFontSize = 18
calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Times'
calculator1Display.DataAxesGrid.ZLabelBold = 1
calculator1Display.DataAxesGrid.ZLabelFontSize = 18

# show data from contour1
contour1Display = Show(contour1, renderView2, 'GeometryRepresentation')

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

# hide data in view
Hide(calculator2, renderView2)

# hide data in view
Hide(streamTracer2, renderView2)

# show color legend
tube2Display.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(tube2, renderView2)

# show color legend
clip1Display.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(solution_12pvtu, renderView2)

# show color legend
calculator1Display.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(calculator1, renderView2)

# show color legend
contour1Display.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from calculator3
calculator3Display = Show(calculator3, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = [None, '']
calculator3Display.SelectTCoordArray = 'None'
calculator3Display.SelectNormalArray = 'None'
calculator3Display.SelectTangentArray = 'None'
calculator3Display.OSPRayScaleArray = 'M'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'n'
calculator3Display.ScaleFactor = 6.0
calculator3Display.SelectScaleArray = 'M'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'M'
calculator3Display.GaussianRadius = 0.3
calculator3Display.SetScaleArray = ['POINTS', 'M']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'M']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityUnitDistance = 1.288470508005519
calculator3Display.OpacityArrayName = ['POINTS', 'M']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.8430583477020264, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.8430583477020264, 1.0, 0.5, 0.0]

# show data from streamTracer3
streamTracer3Display = Show(streamTracer3, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer3Display.Representation = 'Surface'
streamTracer3Display.ColorArrayName = [None, '']
streamTracer3Display.SelectTCoordArray = 'None'
streamTracer3Display.SelectNormalArray = 'None'
streamTracer3Display.SelectTangentArray = 'None'
streamTracer3Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer3Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer3Display.SelectOrientationVectors = 'Normals'
streamTracer3Display.ScaleFactor = 5.9697315216064455
streamTracer3Display.SelectScaleArray = 'AngularVelocity'
streamTracer3Display.GlyphType = 'Arrow'
streamTracer3Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer3Display.GaussianRadius = 0.29848657608032225
streamTracer3Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer3Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer3Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer3Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer3Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer3Display.ScaleTransferFunction.Points = [-0.13286091108408243, 0.0, 0.5, 0.0, 2.130264287049815, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer3Display.OpacityTransferFunction.Points = [-0.13286091108408243, 0.0, 0.5, 0.0, 2.130264287049815, 1.0, 0.5, 0.0]

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

# show data from clip1
clip1Display_1 = Show(clip1, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display_1.Representation = 'Surface'
clip1Display_1.ColorArrayName = [None, '']
clip1Display_1.SelectTCoordArray = 'None'
clip1Display_1.SelectNormalArray = 'TubeNormals'
clip1Display_1.SelectTangentArray = 'None'
clip1Display_1.OSPRayScaleArray = 'AngularVelocity'
clip1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display_1.SelectOrientationVectors = 'Normals'
clip1Display_1.ScaleFactor = 6.04471435546875
clip1Display_1.SelectScaleArray = 'AngularVelocity'
clip1Display_1.GlyphType = 'Arrow'
clip1Display_1.GlyphTableIndexArray = 'AngularVelocity'
clip1Display_1.GaussianRadius = 0.3022357177734375
clip1Display_1.SetScaleArray = ['POINTS', 'AngularVelocity']
clip1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display_1.OpacityArray = ['POINTS', 'AngularVelocity']
clip1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display_1.DataAxesGrid = 'GridAxesRepresentation'
clip1Display_1.PolarAxes = 'PolarAxesRepresentation'
clip1Display_1.ScalarOpacityUnitDistance = 0.8895404876761676
clip1Display_1.OpacityArrayName = ['POINTS', 'AngularVelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display_1.ScaleTransferFunction.Points = [-0.3092884999423243, 0.0, 0.5, 0.0, 0.12296302924712293, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display_1.OpacityTransferFunction.Points = [-0.3092884999423243, 0.0, 0.5, 0.0, 0.12296302924712293, 1.0, 0.5, 0.0]

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

# hide data in view
Hide(calculator3, renderView3)

# hide data in view
Hide(streamTracer3, renderView3)

# show color legend
tube3Display.SetScalarBarVisibility(renderView3, True)

# hide data in view
Hide(clip1, renderView3)

# show color legend
contour1Display_1.SetScalarBarVisibility(renderView3, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'subdomain_input_1'
subdomain_input_1PWF = GetOpacityTransferFunction('subdomain_input_1')
subdomain_input_1PWF.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
subdomain_input_1PWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'l'
lPWF = GetOpacityTransferFunction('l')
lPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0162511379691284, 1.0, 0.5, 0.0]
lPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'subdomain'
subdomainPWF = GetOpacityTransferFunction('subdomain')
subdomainPWF.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
subdomainPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'n'
nPWF = GetOpacityTransferFunction('n')
nPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0000000000000002, 1.0, 0.5, 0.0]
nPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'u_11'
u_11PWF = GetOpacityTransferFunction('u_11')
u_11PWF.Points = [3.553301576175727e-05, 0.0, 0.5, 0.0, 1.7491949796676636, 1.0, 0.5, 0.0]
u_11PWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(tube3)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='/home/heidi/Documents/VerHem-repo_and_data/paraview-pvpython-py-scripts/state-saved')
