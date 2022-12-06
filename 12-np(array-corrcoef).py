#--------------------------------------(.CORRCOEF())
# pic n° 25(Big Data-1.2-mean.median)
#--------------------------------------(Standard Deviation)
import numpy as np
E = np.array([[2, 4, 6], [1, 3, 5]])
print(np.std(E))  # 1.707825127659933
# mean = ((2+4+6+1+3+5) /6) = 3.5
# std = sqrt(((2-3.5)^2 + (4-3.5)^2 + (6-3.5)^2 + (1-3.5)^2 + (3-3.5)^2 + (5-3.5)^2) /6)
#     = sqrt(2.91)
#     = 1.707825127659933


#--------------------------------------(CORRCOEF())
# "matrix": the cultural, social or political environment in which something develops
# this function returns a matrix of correlations of 
# x with x
# x with y
# y with x
# y with y
import numpy as np
x = [11, 2, 7, 4, 15, 6, 10, 8, 9, 1, 11, 5, 13, 6, 15]
y = [2, 5, 17, 6, 10, 8, 13, 4, 6, 9, 11, 2, 5, 4, 7]

# to return the upper three quartiles
pearsons_coefficient = np.corrcoef(x, y)

print("The pearson's coeffient of the x and y inputs are: \n" ,pearsons_coefficient)
# The pearson's coeffient of the x and y inputs are:
#  [[1.         0.11521488]
#  [0.11521488 1.        ]]
# TO FIGURE OUT the calculation