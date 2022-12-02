# pic n° 22-
#-------------------------------------- numpy
# import the numpy package
import numpy as np
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.65, "dad", 1.70 ] 
fam_ext = fam + ["me", 1.75]
print(str(len(fam_ext)) + " elements in fam_ext")
# 10 elements in fam_ext
# len() => means "length"


#--------------------------------------
# definition of radius
r = 3

# import the math package
import math

# calculate C (circumference) => => π × R × 2
C = math.pi*r*2

# calculate A (area) => π × R × R
A = math.pi*r**2 

print(C)  # 18.84955592153876
print(A)  # 28.274333882308138
print("Circumference: " + str(C))  # Circumference: 18.84955592153876
print("Area: " + str(A))  # Area: 28.274333882308138



#--------------------------------------