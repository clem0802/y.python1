#-------------------------------------- (Baseball player's weight in lb)(1)
# pic n° 23(NP-6-exo1)
baseball = [180, 215, 210, 188, 176, 209, 200]
import numpy as np
np_baseball = np.array(baseball)
print(type(np_baseball))  # <class 'numpy.ndarray'>

#-------------------------------------- (Baseball players' height in m)(2)
# pic n° 23(NP-6-exo2)
import numpy as np
height_in = [74, 74, 72, 71, 70, 75, 75, 73]
# create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)
print(np_height_in)  # [74, 74, 72, 71, 70, 75, 75, 73]
np_height_m = np_height_in * 0.0254
print(np_height_m)  # [1.8796 1.8796 1.8288 1.8034 1.778  1.905  1.905  1.8542]


#-------------------------------------- (Baseball players' weight in kg & BMI)(3)
# pic n° 23(NP-6-exo3)
import numpy as np
weight_lb = [180, 215, 210, 188, 156, 140, 200, 212]
# height_in array
np_height_m = np.array(height_in) * 0.0254
# weight_in array
np_weight_kg = np.array(weight_lb) * 0.453592

bmi = np_weight_kg / np_height_m **2
print(bmi)  
# [23.11037639 27.60406069 28.48080465 26.22038745 22.38342142 17.49860637 24.99800911 27.96971839]
light = bmi < 21
print(light)  # [False False False False False True False False]
print(bmi[light])  # [17.49860637]