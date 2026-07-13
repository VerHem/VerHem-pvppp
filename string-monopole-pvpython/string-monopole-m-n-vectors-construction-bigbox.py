# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
setup_conf_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='setup_conf_00.pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/lumi/test-dealii-9.5-Trilinos-14.4-IV/refine-cycle_1/solution_14.pvtu'])
#setup_conf_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']
setup_conf_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'v_11', 'v_12', 'v_13', 'subdomain']

# Properties modified on setup_conf_00pvtu
# setup_conf_00pvtu.PointArrayStatus = ['subdomain', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33']
setup_conf_00pvtu.PointArrayStatus = ['subdomain', 'u_11', 'u_12', 'u_13', 'v_11', 'v_12', 'v_13']
setup_conf_00pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
setup_conf_00pvtuDisplay = Show(setup_conf_00pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
setup_conf_00pvtuDisplay.Representation = 'Surface'
setup_conf_00pvtuDisplay.ColorArrayName = [None, '']
setup_conf_00pvtuDisplay.SelectTCoordArray = 'None'
setup_conf_00pvtuDisplay.SelectNormalArray = 'None'
setup_conf_00pvtuDisplay.SelectTangentArray = 'None'
setup_conf_00pvtuDisplay.OSPRayScaleArray = 'subdomain'
setup_conf_00pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
setup_conf_00pvtuDisplay.SelectOrientationVectors = 'None'
setup_conf_00pvtuDisplay.ScaleFactor = 3.0
setup_conf_00pvtuDisplay.SelectScaleArray = 'None'
setup_conf_00pvtuDisplay.GlyphType = 'Arrow'
setup_conf_00pvtuDisplay.GlyphTableIndexArray = 'None'
setup_conf_00pvtuDisplay.GaussianRadius = 0.15
setup_conf_00pvtuDisplay.SetScaleArray = ['POINTS', 'subdomain']
setup_conf_00pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
setup_conf_00pvtuDisplay.OpacityArray = ['POINTS', 'subdomain']
setup_conf_00pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
setup_conf_00pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
setup_conf_00pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
setup_conf_00pvtuDisplay.ScalarOpacityUnitDistance = 1.447513849627623
setup_conf_00pvtuDisplay.OpacityArrayName = ['POINTS', 'subdomain']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
setup_conf_00pvtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 511.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
setup_conf_00pvtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 511.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=setup_conf_00pvtu)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'm1'
calculator1.Function = '(sqrt(2)*cos(0.60459)*(u_11 + v_11*tan(0.60459)))/2.4973256688320586'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'm1'
m1LUT = GetColorTransferFunction('m1')
m1LUT.RGBPoints = [-1.576769484823424, 0.231373, 0.298039, 0.752941, 1.5421665324230907, 0.865003, 0.865003, 0.865003, 4.6611025496696055, 0.705882, 0.0156863, 0.14902]
m1LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'm1'
m1PWF = GetOpacityTransferFunction('m1')
m1PWF.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]
m1PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'm1']
calculator1Display.LookupTable = m1LUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'm1'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 3.0
calculator1Display.SelectScaleArray = 'm1'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'm1'
calculator1Display.GaussianRadius = 0.15
calculator1Display.SetScaleArray = ['POINTS', 'm1']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'm1']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = m1PWF
calculator1Display.ScalarOpacityUnitDistance = 1.447513849627623
calculator1Display.OpacityArrayName = ['POINTS', 'm1']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# hide data in view
Hide(setup_conf_00pvtu, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'm2'
calculator2.Function = '(sqrt(2)*cos(0.60459)*(u_12 + v_12*tan(0.60459)))/2.4973256688320586'

# show data in view
calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'm2'
m2LUT = GetColorTransferFunction('m2')
m2LUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.8079601160717313, 0.865003, 0.865003, 0.865003, 3.6159202321434627, 0.705882, 0.0156863, 0.14902]
m2LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'm2'
m2PWF = GetOpacityTransferFunction('m2')
m2PWF.Points = [0.0, 0.0, 0.5, 0.0, 3.6159202321434627, 1.0, 0.5, 0.0]
m2PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'm2']
calculator2Display.LookupTable = m2LUT
calculator2Display.SelectTCoordArray = 'None'
calculator2Display.SelectNormalArray = 'None'
calculator2Display.SelectTangentArray = 'None'
calculator2Display.OSPRayScaleArray = 'm2'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'None'
calculator2Display.ScaleFactor = 3.0
calculator2Display.SelectScaleArray = 'm2'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'm2'
calculator2Display.GaussianRadius = 0.15
calculator2Display.SetScaleArray = ['POINTS', 'm2']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'm2']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityFunction = m2PWF
calculator2Display.ScalarOpacityUnitDistance = 1.447513849627623
calculator2Display.OpacityArrayName = ['POINTS', 'm2']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.6159202321434627, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.6159202321434627, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.Function = ''

# Properties modified on calculator3
calculator3.ResultArrayName = 'm3'
calculator3.Function = '(sqrt(2)*(v_13 + u_13*cot(0.60459))*sin(0.60459))/2.4973256688320586'

# show data in view
calculator3Display = Show(calculator3, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'm3'
m3LUT = GetColorTransferFunction('m3')
m3LUT.RGBPoints = [-3.731727093026552, 0.231373, 0.298039, 0.752941, 2.872057577985032e-06, 0.865003, 0.865003, 0.865003, 3.731732837141708, 0.705882, 0.0156863, 0.14902]
m3LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'm3'
m3PWF = GetOpacityTransferFunction('m3')
m3PWF.Points = [-3.731727093026552, 0.0, 0.5, 0.0, 3.731732837141708, 1.0, 0.5, 0.0]
m3PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'm3']
calculator3Display.LookupTable = m3LUT
calculator3Display.SelectTCoordArray = 'None'
calculator3Display.SelectNormalArray = 'None'
calculator3Display.SelectTangentArray = 'None'
calculator3Display.OSPRayScaleArray = 'm3'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'None'
calculator3Display.ScaleFactor = 3.0
calculator3Display.SelectScaleArray = 'm3'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'm3'
calculator3Display.GaussianRadius = 0.15
calculator3Display.SetScaleArray = ['POINTS', 'm3']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'm3']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityFunction = m3PWF
calculator3Display.ScalarOpacityUnitDistance = 1.447513849627623
calculator3Display.OpacityArrayName = ['POINTS', 'm3']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [-3.731727093026552, 0.0, 0.5, 0.0, 3.731732837141708, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [-3.731727093026552, 0.0, 0.5, 0.0, 3.731732837141708, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.Function = ''

# Properties modified on calculator4
calculator4.ResultArrayName = 'n1'
calculator4.Function = '(sqrt(2)*(v_11*cos(0.60459) - u_11*sin(0.60459)))/2.4973256688320586'

# show data in view
calculator4Display = Show(calculator4, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'n1'
n1LUT = GetColorTransferFunction('n1')
n1LUT.RGBPoints = [-1.576769484823424, 0.231373, 0.298039, 0.752941, 1.5421665324230907, 0.865003, 0.865003, 0.865003, 4.6611025496696055, 0.705882, 0.0156863, 0.14902]
n1LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'n1'
n1PWF = GetOpacityTransferFunction('n1')
n1PWF.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]
n1PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator4Display.Representation = 'Surface'
calculator4Display.ColorArrayName = ['POINTS', 'n1']
calculator4Display.LookupTable = n1LUT
calculator4Display.SelectTCoordArray = 'None'
calculator4Display.SelectNormalArray = 'None'
calculator4Display.SelectTangentArray = 'None'
calculator4Display.OSPRayScaleArray = 'n1'
calculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator4Display.SelectOrientationVectors = 'None'
calculator4Display.ScaleFactor = 3.0
calculator4Display.SelectScaleArray = 'n1'
calculator4Display.GlyphType = 'Arrow'
calculator4Display.GlyphTableIndexArray = 'n1'
calculator4Display.GaussianRadius = 0.15
calculator4Display.SetScaleArray = ['POINTS', 'n1']
calculator4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator4Display.OpacityArray = ['POINTS', 'n1']
calculator4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator4Display.PolarAxes = 'PolarAxesRepresentation'
calculator4Display.ScalarOpacityFunction = n1PWF
calculator4Display.ScalarOpacityUnitDistance = 1.447513849627623
calculator4Display.OpacityArrayName = ['POINTS', 'n1']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator4Display.ScaleTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator4Display.OpacityTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator3, renderView1)

# show color bar/color legend
calculator4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
calculator5.Function = ''

# Properties modified on calculator5
calculator5.ResultArrayName = 'n2'
calculator5.Function = '(sqrt(2)*(v_12*cos(0.60459) - u_12*sin(0.60459)))/2.4973256688320586'

# show data in view
calculator5Display = Show(calculator5, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'n2'
n2LUT = GetColorTransferFunction('n2')
n2LUT.RGBPoints = [-1.576769484823424, 0.231373, 0.298039, 0.752941, 1.5421665324230907, 0.865003, 0.865003, 0.865003, 4.6611025496696055, 0.705882, 0.0156863, 0.14902]
n2LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'n2'
n2PWF = GetOpacityTransferFunction('n2')
n2PWF.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]
n2PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator5Display.Representation = 'Surface'
calculator5Display.ColorArrayName = ['POINTS', 'n2']
calculator5Display.LookupTable = n2LUT
calculator5Display.SelectTCoordArray = 'None'
calculator5Display.SelectNormalArray = 'None'
calculator5Display.SelectTangentArray = 'None'
calculator5Display.OSPRayScaleArray = 'n2'
calculator5Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator5Display.SelectOrientationVectors = 'None'
calculator5Display.ScaleFactor = 3.0
calculator5Display.SelectScaleArray = 'n2'
calculator5Display.GlyphType = 'Arrow'
calculator5Display.GlyphTableIndexArray = 'n2'
calculator5Display.GaussianRadius = 0.15
calculator5Display.SetScaleArray = ['POINTS', 'n2']
calculator5Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator5Display.OpacityArray = ['POINTS', 'n2']
calculator5Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator5Display.DataAxesGrid = 'GridAxesRepresentation'
calculator5Display.PolarAxes = 'PolarAxesRepresentation'
calculator5Display.ScalarOpacityFunction = n2PWF
calculator5Display.ScalarOpacityUnitDistance = 1.447513849627623
calculator5Display.OpacityArrayName = ['POINTS', 'n2']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator5Display.ScaleTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator5Display.OpacityTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator4, renderView1)

# show color bar/color legend
calculator5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
calculator6.Function = ''

# Properties modified on calculator6
calculator6.ResultArrayName = 'n3'
calculator6.Function = '(sqrt(2)*(v_13*cos(0.60459) - u_13*sin(0.60459)))/2.4973256688320586'

# show data in view
calculator6Display = Show(calculator6, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'n3'
n3LUT = GetColorTransferFunction('n3')
n3LUT.RGBPoints = [-1.576769484823424, 0.231373, 0.298039, 0.752941, 1.5421665324230907, 0.865003, 0.865003, 0.865003, 4.6611025496696055, 0.705882, 0.0156863, 0.14902]
n3LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'n3'
n3PWF = GetOpacityTransferFunction('n3')
n3PWF.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]
n3PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator6Display.Representation = 'Surface'
calculator6Display.ColorArrayName = ['POINTS', 'n3']
calculator6Display.LookupTable = n3LUT
calculator6Display.SelectTCoordArray = 'None'
calculator6Display.SelectNormalArray = 'None'
calculator6Display.SelectTangentArray = 'None'
calculator6Display.OSPRayScaleArray = 'n3'
calculator6Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator6Display.SelectOrientationVectors = 'None'
calculator6Display.ScaleFactor = 3.0
calculator6Display.SelectScaleArray = 'n3'
calculator6Display.GlyphType = 'Arrow'
calculator6Display.GlyphTableIndexArray = 'n3'
calculator6Display.GaussianRadius = 0.15
calculator6Display.SetScaleArray = ['POINTS', 'n3']
calculator6Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator6Display.OpacityArray = ['POINTS', 'n3']
calculator6Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator6Display.DataAxesGrid = 'GridAxesRepresentation'
calculator6Display.PolarAxes = 'PolarAxesRepresentation'
calculator6Display.ScalarOpacityFunction = n3PWF
calculator6Display.ScalarOpacityUnitDistance = 1.447513849627623
calculator6Display.OpacityArrayName = ['POINTS', 'n3']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator6Display.ScaleTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator6Display.OpacityTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator5, renderView1)

# show color bar/color legend
calculator6Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=calculator6)
mergeVectorComponents1.XArray = 'n3'
mergeVectorComponents1.YArray = 'n3'
mergeVectorComponents1.ZArray = 'n3'

# Properties modified on mergeVectorComponents1
mergeVectorComponents1.XArray = 'm1'
mergeVectorComponents1.YArray = 'm2'
mergeVectorComponents1.ZArray = 'm3'
mergeVectorComponents1.OutputVectorName = 'm'

# show data in view
mergeVectorComponents1Display = Show(mergeVectorComponents1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents1Display.Representation = 'Surface'
mergeVectorComponents1Display.ColorArrayName = ['POINTS', 'n3']
mergeVectorComponents1Display.LookupTable = n3LUT
mergeVectorComponents1Display.SelectTCoordArray = 'None'
mergeVectorComponents1Display.SelectNormalArray = 'None'
mergeVectorComponents1Display.SelectTangentArray = 'None'
mergeVectorComponents1Display.OSPRayScaleArray = 'n3'
mergeVectorComponents1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.SelectOrientationVectors = 'None'
mergeVectorComponents1Display.ScaleFactor = 3.0
mergeVectorComponents1Display.SelectScaleArray = 'n3'
mergeVectorComponents1Display.GlyphType = 'Arrow'
mergeVectorComponents1Display.GlyphTableIndexArray = 'n3'
mergeVectorComponents1Display.GaussianRadius = 0.15
mergeVectorComponents1Display.SetScaleArray = ['POINTS', 'n3']
mergeVectorComponents1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.OpacityArray = ['POINTS', 'n3']
mergeVectorComponents1Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents1Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents1Display.ScalarOpacityFunction = n3PWF
mergeVectorComponents1Display.ScalarOpacityUnitDistance = 1.447513849627623
mergeVectorComponents1Display.OpacityArrayName = ['POINTS', 'n3']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents1Display.ScaleTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents1Display.OpacityTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator6, renderView1)

# show color bar/color legend
mergeVectorComponents1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents2 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=mergeVectorComponents1)
mergeVectorComponents2.XArray = 'n3'
mergeVectorComponents2.YArray = 'n3'
mergeVectorComponents2.ZArray = 'n3'

# Properties modified on mergeVectorComponents2
mergeVectorComponents2.XArray = 'n1'
mergeVectorComponents2.YArray = 'n2'
mergeVectorComponents2.OutputVectorName = 'n'

# show data in view
mergeVectorComponents2Display = Show(mergeVectorComponents2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mergeVectorComponents2Display.Representation = 'Surface'
mergeVectorComponents2Display.ColorArrayName = ['POINTS', 'n3']
mergeVectorComponents2Display.LookupTable = n3LUT
mergeVectorComponents2Display.SelectTCoordArray = 'None'
mergeVectorComponents2Display.SelectNormalArray = 'None'
mergeVectorComponents2Display.SelectTangentArray = 'None'
mergeVectorComponents2Display.OSPRayScaleArray = 'n3'
mergeVectorComponents2Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.SelectOrientationVectors = 'None'
mergeVectorComponents2Display.ScaleFactor = 3.0
mergeVectorComponents2Display.SelectScaleArray = 'n3'
mergeVectorComponents2Display.GlyphType = 'Arrow'
mergeVectorComponents2Display.GlyphTableIndexArray = 'n3'
mergeVectorComponents2Display.GaussianRadius = 0.15
mergeVectorComponents2Display.SetScaleArray = ['POINTS', 'n3']
mergeVectorComponents2Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.OpacityArray = ['POINTS', 'n3']
mergeVectorComponents2Display.OpacityTransferFunction = 'PiecewiseFunction'
mergeVectorComponents2Display.DataAxesGrid = 'GridAxesRepresentation'
mergeVectorComponents2Display.PolarAxes = 'PolarAxesRepresentation'
mergeVectorComponents2Display.ScalarOpacityFunction = n3PWF
mergeVectorComponents2Display.ScalarOpacityUnitDistance = 1.447513849627623
mergeVectorComponents2Display.OpacityArrayName = ['POINTS', 'n3']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergeVectorComponents2Display.ScaleTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergeVectorComponents2Display.OpacityTransferFunction.Points = [-1.576769484823424, 0.0, 0.5, 0.0, 4.6611025496696055, 1.0, 0.5, 0.0]

# hide data in view
Hide(mergeVectorComponents1, renderView1)

# show color bar/color legend
mergeVectorComponents2Display.SetScalarBarVisibility(renderView1, True)

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
renderView1.CameraPosition = [0.0, 0.0, 100.38195644853695]
renderView1.CameraParallelScale = 25.98076211353316

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
