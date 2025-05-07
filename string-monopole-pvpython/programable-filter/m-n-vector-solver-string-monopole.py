from scipy.optimize import fsolve

# Get the first input.
input0 = inputs[0]

# compute a value.
u11 = input0.PointData["u_11"] 
u12 = input0.PointData["u_12"]
u13 = input0.PointData["u_13"]
v11 = input0.PointData["v_11"]
v12 = input0.PointData["v_12"]
v13 = input0.PointData["v_13"]


# To access cell data, you can use input0.CellData.

# 'output' is a variable set to the output dataset.
output.PointData.append(u11, "u11")
output.PointData.append(u12, "u12")
output.PointData.append(u13, "u13")
output.PointData.append(v11, "v11")
output.PointData.append(v12, "v12")
output.PointData.append(v13, "v13")
