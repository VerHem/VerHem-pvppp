from paraview.vtk.numpy_interface import dataset_adapter as dsa
from paraview.vtk.numpy_interface import algorithms as algs
import numpy as np

# Code for 'Script'

# 'inputs' is set to an array with data objects produced by inputs to
# this filter.

# Get the first input.
input0 = inputs[0]

# compute a value.
dataArray = input0.PointData["v_12"] / 2.0
v12=input0.PointData['v_12']

# To access cell data, you can use input0.CellData.

# 'output' is a variable set to the output dataset.
output0.PointData.append(dataArray, "V12 half")
output0.PointData.append(v12 + 1, 'v12p1')