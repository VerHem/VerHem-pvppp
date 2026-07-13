from vtkmodules.vtkCommonDataModel import vtkDataSet
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase

from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid

from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
from vtk.util.numpy_support import numpy_to_vtk

import sys

import os
# sys.path.append("./SCC-GL-calculator")
# import Module_GLSCC_calculator as sc

import numpy as np
np.set_printoptions(precision=10)

from paraview.util.vtkAlgorithm import smproxy, smproperty, smdomain

@smproxy.filter(label="PyAlg-VerHem-lVector-AMatrix-MPI Filter")
@smproperty.input(name="Input")
class PyAlg-VerHem-lVector-AMatrix-MPI(VTKPythonAlgorithmBase):
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

        # l1, l2, l3 arrays, same lattice, same dim as u11
        l1_arr = np.zeros(N, dtype=float)
        l2_arr = np.zeros(N, dtype=float)
        l3_arr = np.zeros(N, dtype=float)
        
        # """run Singlar Value Decomposition algorithm."""
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

            # compute gapA
            Delta_A2 = np.trace(A.conj().T @ A).real

            # compute Im(A^\Degger. A)
            imAdAinvDelta2 = ((A.conj().T @ A).imag)/Delta_A2

            l1_arr[i] = epsilon(1, 2, 0) * imAdAinvDelta2[1, 2] + epsilon(2, 1, 0) * imAdAinvDelta2[2, 1]
            l2_arr[i] = epsilon(0, 2, 1) * imAdAinvDelta2[0, 2] + epsilon(2, 0, 1) * imAdAinvDelta2[2, 0]
            l3_arr[i] = epsilon(0, 1, 2) * imAdAinvDelta2[0, 1] + epsilon(1, 0, 2) * imAdAinvDelta2[1, 0]
            
                                   
            ############################################
            #            l-vector done at here         #
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
                
        output.PointData.append(l1_arr, "l1")
        output.PointData.append(l2_arr, "l2")
        output.PointData.append(l3_arr, "l3")        
                
        output.PointData.SetActiveScalars("l1")

        vtkUnstructuredGrid.GetData(outInfo).ShallowCopy(output.VTKObject)
        
        return 1

    def epsilon(self, i, j, k):
        '''Lev-Civita symbol'''
        # Check for repeated indices
        if i == j or j == k or i == k:
            return 0
    
        # Check for even permutations
        if (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
            return 1
    
        # Check for odd permutations
        if (i, j, k) in [(2, 1, 0), (1, 0, 2), (0, 2, 1)]:
            return -1
        

        
