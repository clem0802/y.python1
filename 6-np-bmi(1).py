#-------------------------------------- BMI (Body Mass Index)
# pic n° 23(NP-2,3,5)
# pip install numpy (in the vscode terminal) => no more "numpy" underlined in yellow
import numpy as np
height=[1.7,1.8,1.75,1.8]
weight=[70,80,75,70]
np_height=np.array(height) #converting list into array
np_weight=np.array(weight)
BMI=np_weight /np_height **2 #Body Mass Index
print(BMI) # [24.22145329 24.69135802 24.48979592 21.60493827]


import numpy as np
height = [1.73, 1.68, 1.89, 1.79]
weight = [65, 59, 63, 88]
np_height = np.array(height) #converting list into array
np_weight = np.array(weight) #converting list into array
bmi = np_weight/np_height **2
print(bmi) # [21.71806609 20.90419501 17.6366843  27.46481071]
bmi[1]  # 20.904195011337873
bmi > 23  # array([False, False, False,  True])
bmi[bmi > 23]  # array([27.46481071])
