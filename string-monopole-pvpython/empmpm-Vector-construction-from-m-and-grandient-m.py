# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
mergeVectorComponents1 = FindSource('MergeVectorComponents1')

# find source
mergeVectorComponents2 = FindSource('MergeVectorComponents2')

# set active source
SetActiveSource(mergeVectorComponents2)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
mergeVectorComponents2Display = GetDisplayProperties(mergeVectorComponents2, view=renderView1)

# find source
pythonCalculator1 = FindSource('PythonCalculator1')

# set active source
SetActiveSource(pythonCalculator1)

# get display properties
pythonCalculator1Display = GetDisplayProperties(pythonCalculator1, view=renderView1)

# find source
pythonCalculator2 = FindSource('PythonCalculator2')

# set active source
SetActiveSource(pythonCalculator2)

# get display properties
pythonCalculator2Display = GetDisplayProperties(pythonCalculator2, view=renderView1)

# find source
pythonCalculator3 = FindSource('PythonCalculator3')

# set active source
SetActiveSource(pythonCalculator3)

# get display properties
pythonCalculator3Display = GetDisplayProperties(pythonCalculator3, view=renderView1)

#############################################
#############################################

# create a new 'Python Calculator'
pythonCalculator4 = PythonCalculator(registrationName='PythonCalculator4', Input=[mergeVectorComponents2, pythonCalculator1, pythonCalculator2, pythonCalculator3])

# e^ijk m. pm x pm, k = 1
# - 3 m3 (m22 m31 - m21 m32)
# + 3 m3 (-m22 m31 + m21 m32)
# + 3 m2 (m23 m31 - m21 m33)

# - 3 m2 (-m23 m31 + m21 m33)
# - 3 m1 (m23 m32 - m22 m33)
# + 3 m1 (-m23 m32 + m22 m33)

# Properties modified on pythonCalculator4
# pythonCalculator4.Expression = "inputs[0].PointData['m1']*(inputs[1].PointData['m_i1'][:,0]*inputs[2].PointData['m_i2'][:,2])"
pythonCalculator4.Expression = "-3.*inputs[0].PointData['m3']*(inputs[2].PointData['m_i2'][:,1]*inputs[1].PointData['m_i1'][:,2]-inputs[1].PointData['m_i1'][:,1]*inputs[2].PointData['m_i2'][:,2])+3.*inputs[0].PointData['m3']*(-inputs[2].PointData['m_i2'][:,1]*inputs[1].PointData['m_i1'][:,2]+inputs[1].PointData['m_i1'][:,1]*inputs[2].PointData['m_i2'][:,2])+3.*inputs[0].PointData['m2']*(inputs[3].PointData['m_i3'][:,1]*inputs[1].PointData['m_i1'][:,2]-inputs[1].PointData['m_i1'][:,1]*inputs[3].PointData['m_i3'][:,2])-3.*inputs[0].PointData['m2']*(-inputs[3].PointData['m_i3'][:,1]*inputs[1].PointData['m_i1'][:,2]+inputs[1].PointData['m_i1'][:,1]*inputs[3].PointData['m_i3'][:,2])-3.*inputs[0].PointData['m1']*(inputs[3].PointData['m_i3'][:,1]*inputs[2].PointData['m_i2'][:,2]-inputs[2].PointData['m_i2'][:,1]*inputs[3].PointData['m_i3'][:,2])+3.*inputs[0].PointData['m1']*(-inputs[3].PointData['m_i3'][:,1]*inputs[2].PointData['m_i2'][:,2]+inputs[2].PointData['m_i2'][:,1]*inputs[3].PointData['m_i3'][:,2])"

pythonCalculator4.ArrayName = 'empmpm1'
pythonCalculator4.CopyArrays = 0

# show data in view
pythonCalculator4Display = Show(pythonCalculator4, renderView1, 'UnstructuredGridRepresentation')

# set active source
SetActiveSource(mergeVectorComponents2)

# set active source
SetActiveSource(pythonCalculator1)

# set active source
SetActiveSource(pythonCalculator2)

# set active source
SetActiveSource(pythonCalculator3)

# create a new 'Python Calculator'
pythonCalculator5 = PythonCalculator(registrationName='PythonCalculator5', Input=[mergeVectorComponents2, pythonCalculator1, pythonCalculator2, pythonCalculator3])

# e^ijk m. pm x pm, k = 2
# 3 m3 (m12 m31 - m11 m32)
# -3 m3 (-m12 m31 + m11 m32)
# -3 m2 (m13 m31 - m11 m33)

# +3 m2 (-m13 m31 + m11 m33)
# +3 m1 (m13 m32 - m12 m33)
# -3 m1 (-m13 m32 + m12 m33) 

# Properties modified on pythonCalculator5
# pythonCalculator5.Expression = "inputs[0].PointData['m2']*(inputs[2].PointData['m_i2'][:,1])"
pythonCalculator5.Expression = "3.*inputs[0].PointData['m3']*(inputs[2].PointData['m_i2'][:,0]*inputs[1].PointData['m_i1'][:,2]-inputs[1].PointData['m_i1'][:,0]*inputs[2].PointData['m_i2'][:,2])-3.*inputs[0].PointData['m3']*(-inputs[2].PointData['m_i2'][:,0]*inputs[1].PointData['m_i1'][:,2]+inputs[1].PointData['m_i1'][:,0]*inputs[2].PointData['m_i2'][:,2])-3.*inputs[0].PointData['m2']*(inputs[3].PointData['m_i3'][:,0]*inputs[1].PointData['m_i1'][:,2]-inputs[1].PointData['m_i1'][:,0]*inputs[3].PointData['m_i3'][:,2])+3.*inputs[0].PointData['m2']*(-inputs[3].PointData['m_i3'][:,0]*inputs[1].PointData['m_i1'][:,2]+inputs[1].PointData['m_i1'][:,0]*inputs[3].PointData['m_i3'][:,2])+3.*inputs[0].PointData['m1']*(inputs[3].PointData['m_i3'][:,0]*inputs[2].PointData['m_i2'][:,2]-inputs[2].PointData['m_i2'][:,0]*inputs[3].PointData['m_i3'][:,2])-3.*inputs[0].PointData['m1']*(-inputs[3].PointData['m_i3'][:,0]*inputs[2].PointData['m_i2'][:,2]+inputs[2].PointData['m_i2'][:,0]*inputs[3].PointData['m_i3'][:,2])"

pythonCalculator5.ArrayName = 'empmpm2'
pythonCalculator5.CopyArrays = 0

# show data in view
pythonCalculator5Display = Show(pythonCalculator5, renderView1, 'UnstructuredGridRepresentation')

# set active source
SetActiveSource(mergeVectorComponents2)

# set active source
SetActiveSource(pythonCalculator1)

# set active source
SetActiveSource(pythonCalculator2)

# set active source
SetActiveSource(pythonCalculator3)

# e^ijk m. pm x pm, k = 3
# -3 m3 (m12 m21 - m11 m22)
# +3 m3 (-m12 m21 + m11 m22)
# +3 m2 (m13 m21 - m11 m23)

# -3 m2 (-m13 m21 + m11 m23)
# -3 m1 (m13 m22 - m12 m23)
# +3 m1 (-m13 m22 + m12 m23)

# create a new 'Python Calculator'
pythonCalculator6 = PythonCalculator(registrationName='PythonCalculator6', Input=[mergeVectorComponents2, pythonCalculator1, pythonCalculator2, pythonCalculator3])

# Properties modified on pythonCalculator6
pythonCalculator6.Expression = "-3.*inputs[0].PointData['m3']*(inputs[2].PointData['m_i2'][:,0]*inputs[1].PointData['m_i1'][:,1]-inputs[1].PointData['m_i1'][:,0]*inputs[2].PointData['m_i2'][:,1])+3.*inputs[0].PointData['m3']*(-inputs[2].PointData['m_i2'][:,0]*inputs[1].PointData['m_i1'][:,1]+inputs[1].PointData['m_i1'][:,0]*inputs[2].PointData['m_i2'][:,1])+3.*inputs[0].PointData['m2']*(inputs[3].PointData['m_i3'][:,0]*inputs[1].PointData['m_i1'][:,1]-inputs[1].PointData['m_i1'][:,0]*inputs[3].PointData['m_i3'][:,1])-3.*inputs[0].PointData['m2']*(-inputs[3].PointData['m_i3'][:,0]*inputs[1].PointData['m_i1'][:,1]+inputs[1].PointData['m_i1'][:,0]*inputs[3].PointData['m_i3'][:,1])-3.*inputs[0].PointData['m1']*(inputs[3].PointData['m_i3'][:,0]*inputs[2].PointData['m_i2'][:,1]-inputs[2].PointData['m_i2'][:,0]*inputs[3].PointData['m_i3'][:,1])+3.*inputs[0].PointData['m1']*(-inputs[3].PointData['m_i3'][:,0]*inputs[2].PointData['m_i2'][:,1]+inputs[2].PointData['m_i2'][:,0]*inputs[3].PointData['m_i3'][:,1])"

pythonCalculator6.ArrayName = 'empmpm3'
pythonCalculator6.CopyArrays = 0

# show data in view
pythonCalculator6Display = Show(pythonCalculator6, renderView1, 'UnstructuredGridRepresentation')


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
renderView1.CameraPosition = [-27.669348646204952, 21.905520682726507, -93.97389259549364]
renderView1.CameraViewUp = [0.6558245544129228, 0.7547180043688183, -0.017172294856532627]
renderView1.CameraParallelScale = 25.98076211353316

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
