# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# setup U(1) phase angle recovered from polar phase core
# polar phase core value 0.3753
U1_phi = 0.605

# pvtu data path
solutionData = '/scratch/project_2006155/string-monopole-VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-StringMonopole-dealii-9.5-Trilinos-14.4-VI/refine-cycle_3-Solution-13-32MPI-Ranks/solution_13_32MPI_Ranks.pvtu'

# create a new 'XML Partitioned Unstructured Grid Reader'
# SMSolution_pvtu = XMLPartitionedUnstructuredGridReader(registrationName='SMSolution_pvtu', FileName=['/home/heidi/Documents/VerHem-project/Data-and-Visualization/lumi/test-dealii-9.5-Trilinos-14.4-IV/refine-cycle_1/solution_14.pvtu'])
SMSolution_pvtu = XMLPartitionedUnstructuredGridReader(registrationName='SMSolution_pvtu', FileName=[solutionData])
#setup_conf_00pvtu.PointArrayStatus = ['u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33', 'subdomain']
# Properties modified on setup_conf_00pvtu
# setup_conf_00pvtu.PointArrayStatus = ['subdomain', 'u_11', 'u_12', 'u_13', 'u_21', 'u_22', 'u_23', 'u_31', 'u_32', 'u_33', 'v_11', 'v_12', 'v_13', 'v_21', 'v_22', 'v_23', 'v_31', 'v_32', 'v_33']
SMSolution_pvtu.PointArrayStatus = ['u_12', 'v_12']
SMSolution_pvtu.TimeArray = 'None'

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
# Properties modified on calculator2
calculator2.ResultArrayName = 'm2'
calculator2.Function = '(sqrt(2)*cos(0.3753)*(u_12 + v_12*tan(0.3753)))/2.4973256688320586'

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
# Properties modified on calculator5
calculator5.ResultArrayName = 'n2'
calculator5.Function = '(sqrt(2)*(v_12*cos(0.3753) - u_12*sin(0.3753)))/2.4973256688320586'
