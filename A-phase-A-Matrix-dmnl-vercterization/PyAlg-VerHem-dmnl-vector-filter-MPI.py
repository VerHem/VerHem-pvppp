from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase

from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
from vtk.util.numpy_support import numpy_to_vtk

import sys

import os
sys.path.append("/scratch/project_2006155/string-monopole-VerHem-scc-3d-xyz-AdGR-retangle-w-cycle-ReleaseDealii/A-phase-StringMonopole-dealii-9.5-Trilinos-14.4-VI/GL-Calculator")
import Module_GLSCC_calculator as gl

import numpy as np
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain

@smproxy.filter(label="VerHem-DMNL-A-phase-A-matrix-MPI Filter")
@smproperty.input(name="Input")
class verhem_dmnl_A_phase_A_matrix_mpi_Class(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(
            self, nInputPorts=1, nOutputPorts=1
            ,outputType='vtkUnstructuredGrid'
        )
        
    def RequestData(self, request, inInfo, outInfo):

        # input and output portals
        data = dsa.WrapDataObject(vtkDataSet.GetData(inInfo[0]))

        output_vtk = vtkUnstructuredGrid()
        output = dsa.WrapDataObject(output_vtk)
        
        u11_Array=data.PointData['u_11']
        u12_Array=data.PointData['u_12']
        u13_Array=data.PointData['u_13']
        u21_Array=data.PointData['u_21']
        u22_Array=data.PointData['u_22']
        u23_Array=data.PointData['u_23']
        u31_Array=data.PointData['u_31']
        u32_Array=data.PointData['u_32']
        u33_Array=data.PointData['u_33']

        v11_Array=data.PointData['v_11']
        v12_Array=data.PointData['v_12']
        v13_Array=data.PointData['v_13']
        v21_Array=data.PointData['v_21']
        v22_Array=data.PointData['v_22']
        v23_Array=data.PointData['v_23']
        v31_Array=data.PointData['v_31']
        v32_Array=data.PointData['v_32']
        v33_Array=data.PointData['v_33']
                
        # Nofelem = u11_Array.shape[0]
        N = data.GetNumberOfPoints()

        # U(1)/SO(2) angle arrays, same lattice
        # phi_arr = np.zeros(N, dtype=float)

        # SVD sigma[0]
        Sigma0_arr = np.zeros(N, dtype=float)

        # ditortion factor a
        distortion_a_arr = np.zeros(N, dtype=float)
        
        d1_arr = np.zeros(N, dtype=float)
        d2_arr = np.zeros(N, dtype=float)        
        d3_arr = np.zeros(N, dtype=float)
        
        # m1, m2, m3 arrays, same lattice, same dim as u11
        m1_arr = np.zeros(N, dtype=float)
        m2_arr = np.zeros(N, dtype=float)
        m3_arr = np.zeros(N, dtype=float)

        # n1, n2, n3 arrays, same lattice, same dim as u11
        n1_arr = np.zeros(N, dtype=float)
        n2_arr = np.zeros(N, dtype=float)
        n3_arr = np.zeros(N, dtype=float)

        # l1, l2, l3 arrays, same lattice, same dim as u11
        l1_arr = np.zeros(N, dtype=float)
        l2_arr = np.zeros(N, dtype=float)
        l3_arr = np.zeros(N, dtype=float)

        # reference Vh of Delta_A*x (x + iy) A-phase OP
        # z_ref = np.array([1.+0.j, 0.-1.j, 0.+0.j])

        # calculate gapA2
        gapA2 = (gl.gapA(self.pre, self.red_t))**2
        
        """run Singlar Value Decomposition algorithm."""
        for i in range(N):
            
        ###########################################
        #        SVD A-matrix of A-phase          #
        ###########################################
                    
            uxx = np.array([u11_Array[i],u12_Array[i],u13_Array[i],
                            u21_Array[i],u22_Array[i],u23_Array[i],
                            u31_Array[i],u32_Array[i],u33_Array[i]])

            vxx = np.array([v11_Array[i],v12_Array[i],v13_Array[i],
                            v21_Array[i],v22_Array[i],v23_Array[i],
                            v31_Array[i],v32_Array[i],v33_Array[i]])

            # construct A matrix
            u_values = uxx.reshape(3, 3)
            v_values = vxx.reshape(3, 3)
            A = u_values + 1j * v_values
            # print("A = ",A)    

            # compute gapA, and Polar-Distorted A index a
            # A_PdA = \Delta_PdA/sqrt(2) d (m + i n)
            Delta_A = np.sqrt(np.trace(A.conj().T @ A).real)
            TrAdA = np.trace(A.conj().T @ A).real
            a2 = ((2.*TrAdA)/gapA2) - 1
            # a = np.sqrt(a2)
            a = np.sqrt(a2) if a2 >= 0 else 0
            # print("TrAdA = ", TrAdA, ", gapA2 = ", gapA2, ", a^2 = ", a2, ", a = ", a)
            

            # --- SVD on A ---
            U, S, Vh = np.linalg.svd(A, full_matrices=True)

            # 1st sigular value for rank-1 OP tensor
            sigma = S[0]
            # print("S[0] = ", S[0])
            # print()

            # --- Normalize d ---
            d_raw = U[:, 0]
            # print("U[:, 0] = ", U[:, 0])
            d = np.real(d_raw)
            # d /= np.linalg.norm(d)

            # --- Scale z_rot properly ---
            z_rot = Vh[0, :].conj()  # (m + in)/sqrt(1+a) up to phase
            # z_rot /= np.linalg.norm(z_rot) # nomalized by l2 norm    
            scale = (np.sqrt(2) * sigma) / Delta_A
            # scale = np.sqrt(1+a2)
            # z_rot_scaled = z_rot * scale
            # m_plus_i_a_n = z_rot * scale
            m_plus_i_a_n = z_rot * scale * np.exp(-1j * 0.605)
            # m_plus_i_a_n = z_rot * scale * np.exp(-1j * 0.3753)            

            m = np.real(m_plus_i_a_n)
            m = m / np.linalg.norm(m) if np.linalg.norm(m) > self.tol_zero else np.array([0., 0., 0.])
            # This "-" is very nessary for keeping righthandness
            # n = -np.imag(m_plus_i_a_n)/a if a != 0 else np.array([0., 0., 0.])
            n = -np.imag(m_plus_i_a_n)
            n = n / np.linalg.norm(n) if np.linalg.norm(n) > self.tol_zero else np.array([0., 0., 0.])
            # orthogonalize n against m if there is fluctuation   
            n -= np.dot(n, m) * m  

            # l = m x n
            l = np.cross(m, n)

            # compute relative phase against x (x + iy)
            # phase = np.vdot(z_ref, z_rot_scaled)
            # phase = np.vdot(z_ref, m_plus_i_a_n)
            # phi = np.angle(phase)

            ###########################################
            #  put mi, ni, li, di, phi back to arrays #
            ###########################################

            # phi_arr[i] = phi
            Sigma0_arr[i] = sigma
            distortion_a_arr[i] = a

            d1_arr[i], d2_arr[i], d3_arr[i] = d                                        
            m1_arr[i], m2_arr[i], m3_arr[i] = m                                        
            n1_arr[i], n2_arr[i], n3_arr[i] = n                                        
            l1_arr[i], l2_arr[i], l3_arr[i] = l                                        
                                   
            ############################################
            #            SVD of A done at here         #
            ############################################                    


        ###############################
        #   paraview pipline output   #
        ###############################

        #########################################################        
        # --- cell connectivity handling w/ UstracturedGrid --- #
        input_vtk = data.VTKObject

        # # Copy points
        # output_vtk.SetPoints(input_vtk.GetPoints())

        # # Copy cells
        # output_vtk.SetCells(
        #     input_vtk.GetCellTypesArray(),
        #     input_vtk.GetCellLocationsArray(),
        #     input_vtk.GetCells()
        # )

        output_vtk.DeepCopy(input_vtk)

        # --- volumetric cell connectivity w/ UstracturedGrid --- #        
        ###########################################################
                
        # output.PointData.append(phi_arr, "U1_phi")
        output.PointData.append(Sigma0_arr, "Sigma0")
        output.PointData.append(distortion_a_arr, "distortion_a")                        
        
        output.PointData.append(d1_arr, "d1")
        output.PointData.append(d2_arr, "d2")
        output.PointData.append(d3_arr, "d3")        

        output.PointData.append(m1_arr, "m1")
        output.PointData.append(m2_arr, "m2")
        output.PointData.append(m3_arr, "m3")        

        output.PointData.append(n1_arr, "n1")
        output.PointData.append(n2_arr, "n2")
        output.PointData.append(n3_arr, "n3")        

        output.PointData.append(l1_arr, "l1")
        output.PointData.append(l2_arr, "l2")
        output.PointData.append(l3_arr, "l3")        
                
        # output.PointData.SetActiveScalars("U1_phi")
        output.PointData.SetActiveScalars("distortion_a")        

        vtkUnstructuredGrid.GetData(outInfo).ShallowCopy(output.VTKObject)
        
        return 1

    @smproperty.xml("""
        <DoubleVectorProperty name="pressure"
            number_of_elements="1"
            default_values="0.0"
            command="SetPressure">
            <DoubleRangeDomain name="range" />
            <Documentation>Set pressure for gap calculation</Documentation>
        </DoubleVectorProperty>""")
    def SetPressure(self, p):
        self.pre = p
        self.Modified()

    @smproperty.xml("""
        <DoubleVectorProperty name="red_t"
            number_of_elements="1"
            default_values="0.0"
            command="SetReducedT">
            <DoubleRangeDomain name="range" />
            <Documentation>Set reduced Temperature for gap calculation</Documentation>
        </DoubleVectorProperty>""")
    def SetReducedT(self, t):
        self.red_t = t
        self.Modified()    

    @smproperty.xml("""
        <DoubleVectorProperty name="tol_zero"
            number_of_elements="1"
            default_values="0.001"
            command="SetTolZero">
            <DoubleRangeDomain name="range" />
            <Documentation>Set tol for numerical zero of vector norm</Documentation>
        </DoubleVectorProperty>""")
    def SetTolZero(self, tol):
        self.tol_zero = tol
        self.Modified()    
        
