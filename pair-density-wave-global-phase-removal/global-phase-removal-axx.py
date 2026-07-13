# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
# output_conf_00pvtu = XMLPartitionedUnstructuredGridReader(registrationName='output_conf_00.pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/lumi/2dPDW/z-axis-300nm-xy-perodic-2dPDW-test-X-random-iniconf-IV-120x105x15.24-breakgoodrun/refine-cycle_2/output_conf_00.pvtu'])
# output_conf_00pvtu.PointArrayStatus = ['du_11', 'du_12', 'du_13', 'du_21', 'du_22', 'du_23', 'du_31', 'du_32', 'du_33', 'dv_11', 'dv_12', 'dv_13', 'dv_21', 'dv_22', 'dv_23', 'dv_31', 'dv_32', 'dv_33', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']

# # Properties modified on output_conf_00pvtu
# output_conf_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33']
# output_conf_00pvtu.TimeArray = 'None'

# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')

# # show data in view
# output_conf_00pvtuDisplay = Show(output_conf_00pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# reset view to fit data

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=output_conf_00pvtu)

# Properties modified on calculator1
calculator1.ResultArrayName = 'phi'
calculator1.Function = 'atan(v_21/u_21)'
calculator1.ResultArrayType = 'Float'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'phi'

# hide data in view
Hide(output_conf_00pvtu, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)

# Properties modified on calculator2
calculator2.ResultArrayName = 'a23'
calculator2.Function = 'u_23/cos(phi)'

# show data in view
calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'a11'

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
