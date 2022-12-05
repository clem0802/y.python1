#--------------------------------------
# pic n° 24(1-NP.array-nd)
# the ND-array (N-dimensional array) is the star of the show for NumPy
import numpy as np

height_in = [68, 74, 69, 70]
weight_lb = [140, 150, 138, 185]
np_height = np.array(height_in) #converting list into array
np_weight = np.array(weight_lb) 
type(np_height)  # <class 'numpy.ndarray'>
type(np_weight)  # <class 'numpy.ndarray'>


