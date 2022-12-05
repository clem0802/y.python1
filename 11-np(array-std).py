#--------------------------------------(SUBSETTING)
# pic n° 24(3-NP.array-2d.shape)
# pic n° 25(Big Data-1.2-mean.median)
import numpy as np
#                col[0]  col[1] col[2] col[3]  col[4] 
np_2d = np.array([[1.73,  1.68,  1.71,  1.89,  1.79],   # row[0] - taille
                  [65.4,  59.2,  63.6,  88.4,  68.7],   # row[1] - poids
                  [20,    30,    25,    28,    31]])    # row[2] - âge

np_2d[0]  # array([1.73, 1.68, 1.71, 1.89, 1.79])
np_2d[0][2]  # 1.71 (data of row[0], col[2])
np_2d[0, 2]  # 1.71 (data of row[0], col[2])
np.mean(np_2d[:, 0])  # 29.043333333333337 (all rows,col[1]) => (1.73 + 65.4 + 20)/3 =29.04
np.mean(np_2d[:, 1])  # 30.293333333333333 (all rows,col[1]) => (1.68 + 59.2 + 30)/3 =30.29
np.mean(np_2d[0, :])  # 1.7600000000000002 (rows[0], all cols) 
np.mean(np_2d[1, :])  # 69.06 (rows[1], all cols) 
np.mean(np_2d[2, :])  # 26.8 (rows[2], all cols) 
#----------------------
np.std(np_2d[:, 0])  # 26.7681855110793 (standard deviation) => 716
                     # mean = (1.73+65.4+20)/3 = 29.04
                     # std = 26.7681855110793

np.std(np_2d[:, 1])  # 23.483357700484166 (standard deviation) 
#----------------------
np.median(np_2d[0, :])  # 1.73
np.median(np_2d[0, 1])  # 1.68
np.median(np_2d[0, 2])  # 1.71
np.median(np_2d[0, :])  # 1.73
np.median(np_2d[1, :])  # 65.4
np.median(np_2d[2, :])  # 28.0


#--------------------------------------(Standard Deviation-1)
# https://pythonexamples.org/numpy-std/
import numpy as np
A = np.array([2, 1, 6])
output = np.std(A)
print(output) # 2.160246899469287

# Mean = (2 + 1 + 6)/3
#      = 3
# Standard Deviation = sqrt( ((2-3)^2 + (1-3)^2 + (6-3)^2)/3 )
#                    = sqrt( (1+4+9)/3 )
#                    = sqrt(14/3)
#                    = sqrt(4.666666666666667)
#                    = 2.160246899469287

#--------------------------------------(Standard Deviation-2)
import numpy as np
B = np.array([20, 30, 40, 50, 60])
print(np.std(B))  # 14.142135623730951
# mean = (20+30+40+50+60)/5 = 40
# std = sqrt( ((20-40)^2 + (30-40)^2 + (40-40)^2 + (50-40)^2 + (60-40)^2) /5)
#     = sqrt((400+100+100+400) /5)
#     = sqrt(1000/5)
#     = sqrt(200)
#     = 14.14213562373095

#--------------------------------------(Standard Deviation-3)
import numpy as np
C = np.array([[2, 3], [6, 5]])
print(np.std(C))  # 1.5811388300841898
# mean = (2+3+6+5)/4 = 4
# std = sqrt( ((2-4)^2 + (3-4)^2 + (6-4)^2 + (5-4)^2) /4)
#     = sqrt((4+1+4+1) /4)
#     = sqrt(10/4)
#     = sqrt(2.5)
#     = 1.5811388300841898

#--------------------------------------(Standard Deviation-4)
# if the axis is 0 : direction down the row
# if the axis is 1 : direction down the column
import numpy as np
D = np.array([[2, 3], [6, 5]])
print(np.std(D, axis=0))  # [2. 1.]
# mean = (2+6)/2 = 4
# std = sqrt(((2-4)^2 + (6-4)^2)/2)
#     = sqrt(4)
#     = 2

print(np.std(D, axis=1))  # [0.5 0.5]
# mean = (3+5)/2 = 4
# std = sqrt(((3-4)^2 + (3-4)^2)/2)
#     = sqrt(1)
#     = 1





#--------------------------------------(Standard Deviation)
# https://www.educative.io/answers/how-to-use-the-numpystd-in-python

# numpy.std(
#              arr,
#              axis=None,
#              out=None,
#              overwrite_input=False,
#              dtype=data-type
#             )
# => if the axis is 0 : direction down the row
# => if the axis is 1 : direction down the column