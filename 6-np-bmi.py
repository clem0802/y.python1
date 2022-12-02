#-------------------------------------- BMI (not solved yet)
# pic n° 23(NP-2,3,5)
# pip install numpy (in the vscode terminal) => no more "numpy" underlined in yellow
import numpy as np
height = [1.73, 1.68, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
weight / height ** 2

import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)
np_weight / np_height ** 2


import numpy as np
height = [1.73, 1.68, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2
bmi
bmi[1]
bmi > 23
bmi[bmi > 23]
