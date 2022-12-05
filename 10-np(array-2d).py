#--------------------------------------
# pic n° 24(2-NP.array-2d.shape)
import numpy as np
np_2d = np.array([[1.72, 1.87, 1.75, 1.77],
                  [64, 68, 62, 83]])
np_2d
# array([[ 1.72,  1.87,  1.75,  1.77],
#        [64.  , 68.  , 62.  , 83.  ]])

np_2d.shape
# (2, 4)  => 2 rows, 4 columns


#--------------------------------------
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
import numpy as np
np_baseball = np.array(baseball) # create a 2D numpy array from baseball
print(type(np_baseball))  # <class 'numpy.ndarray'>
print(np_baseball.shape)  # (4, 2) => 4 rows, 2 columns  