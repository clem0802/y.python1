#--------------------------------------
# pic n° 23(NP-6-exo5)
import numpy as np
# height_meter = [1.72, 1.87, 1.75, 1.77]
# weight_kilo = [64, 68, 62, 83]

height_in = [68, 74, 69, 70]
weight_lb = [140, 150, 138, 185]
np_height = np.array(height_in) #converting list into array
np_weight = np.array(weight_lb) #converting list into array
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m **2
bmi  # array([21.28669136, 19.25864699, 20.37881177, 26.54444207])

#--------------------------------------
np.array([4, 3, 0]) + np.array([0, 2, 2]) # array([4, 5, 2])




