# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
output_conf_00pvtu = FindSource('output_conf_00.pvtu')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=output_conf_00pvtu)

# Properties modified on calculator1
calculator1.ResultArrayName = 'gapA'
calculator1.Function = 'sqrt(u_11^2+u_12^2+u_13^2+v_11^2+v_12^2+v_13^2)'

UpdatePipeline(time=0.0, proxy=calculator1)