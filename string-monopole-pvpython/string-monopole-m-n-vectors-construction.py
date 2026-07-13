# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# phi phase angle
# phi=

# create a new 'XML Partitioned Unstructured Grid Reader'
setup_conf_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='setup_conf_00.pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/lumi/string-monople/runs-32bar-0Hfield/t-0.50/refine-cycle_2/setup_conf_00.pvtu'])
setup_conf_00pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# Properties modified on setup_conf_00pvtu
setup_conf_00pvtu.PointArrayStatus = ['subdomain', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33']
setup_conf_00pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=setup_conf_00pvtu)

# Properties modified on calculator1
calculator1.ResultArrayName = 'm1'
calculator1.Function = '(sqrt(2)*cos(0.600084)*(u_11 + v_11*tan(0.600084)))/3.87091'

# show data in view
# calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'm2'
calculator2.Function = '(sqrt(2)*cos(0.600084)*(u_12 + v_12*tan(0.600084)))/3.87091'

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.Function = ''

# Properties modified on calculator3
calculator3.ResultArrayName = 'm3'
calculator3.Function = '(sqrt(2)*(v_13 + u_13*cot(0.600084))*sin(0.600084))/3.87091'

# show data in view
# calculator3Display = Show(calculator3, renderView1, 'UnstructuredGridRepresentation')

# # hide data in view
# Hide(calculator2, renderView1)

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.Function = ''

# Properties modified on calculator4
calculator4.ResultArrayName = 'n1'
calculator4.Function = '(sqrt(2)*(v_11*cos(0.600084) - u_11*sin(0.600084)))/3.87091'

# show data in view
# calculator4Display = Show(calculator4, renderView1, 'UnstructuredGridRepresentation')

# # hide data in view
# Hide(calculator3, renderView1)

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
calculator5.Function = ''

# Properties modified on calculator5
calculator5.ResultArrayName = 'n2'
calculator5.Function = '(sqrt(2)*(v_12*cos(0.600084) - u_12*sin(0.600084)))/3.87091'

# show data in view
# calculator5Display = Show(calculator5, renderView1, 'UnstructuredGridRepresentation')

# # hide data in view
# Hide(calculator4, renderView1)

# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
calculator6.Function = ''

# Properties modified on calculator6
calculator6.ResultArrayName = 'n3'
calculator6.Function = '(sqrt(2)*(v_13*cos(0.600084) - u_13*sin(0.600084)))/3.87091'

# show data in view
calculator6Display = Show(calculator6, renderView1, 'UnstructuredGridRepresentation')

# # hide data in view
# Hide(calculator5, renderView1)

# create a new 'Merge Vector Components'
mergeVectorComponents1 = MergeVectorComponents(registrationName='MergeVectorComponents1', Input=calculator6)
mergeVectorComponents1.XArray = 'm1'
mergeVectorComponents1.YArray = 'm2'
mergeVectorComponents1.ZArray = 'm3'
mergeVectorComponents1.OutputVectorName = 'm'

# show data in view
mergeVectorComponents1Display = Show(mergeVectorComponents1, renderView1, 'UnstructuredGridRepresentation')

# # hide data in view
# Hide(calculator6, renderView1)

# # show color bar/color legend
# mergeVectorComponents1Display.SetScalarBarVisibility(renderView1, True)

# # update the view to ensure updated data information
renderView1.Update()

# create a new 'Merge Vector Components'
mergeVectorComponents2 = MergeVectorComponents(registrationName='MergeVectorComponents2', Input=mergeVectorComponents1)
mergeVectorComponents2.XArray = 'n1'
mergeVectorComponents2.YArray = 'n2'
mergeVectorComponents2.ZArray = 'n3'
mergeVectorComponents2.OutputVectorName = 'n'

# show data in view
mergeVectorComponents2Display = Show(mergeVectorComponents2, renderView1, 'UnstructuredGridRepresentation')

# # hide data in view
# Hide(mergeVectorComponents1, renderView1)

# # update the view to ensure updated data information
renderView1.Update()

# -3 m3 (m22 m31 - m21 m32) + 3 m3 (-m22 m31 + m21 m32 ) + 3 m2 (m23 m31 - m21 m33 )
# - 3 m2 (-m23 m31 + m21 m33 ) - 3 m1 (m23 m32 - m22 m33 ) + 3 m1 (-m23 m32 + m22 m33 )

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
