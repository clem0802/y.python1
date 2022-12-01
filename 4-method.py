# pic n° 20-
#-------------------------------------- METHODS
# Methods = Functions that belong to Objects:

#                      (type)   (examples of methods)
#          (1) Object  string   capitalize()
#                               replace()
#          (2) Object  float    bit_length()
#                               conjugate()
#          (3) Object  list     index()
#                               count()


#-------------------------------------- ROUND()
round(1.68, 1)
# 1.7

round(1.68)
# 2


#-------------------------------------- INDEX()/ COUNT() / CAPITALIZE() / REPLACE()
sister = "lisa"
height = 1.73
fam = ["lisa", 1.73, "emma", 1.68, "mom", 1.65, "dad", 1.70 ] 
fam.index("mom") # 4
fam.count(1.70) # 1
sister.capitalize() # Lisa
sister.replace("s", "z") # Liza
print(sister) # lisa

#-------------------------------------- APPEND()
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.65, "dad", 1.70 ] 
fam.append("me")
fam # ['liz', 1.73, 'emma', 1.68, 'mom', 1.65, 'dad', 1.7, 'me']
fam.append(1.65)
fam # ['liz', 1.73, 'emma', 1.68, 'mom', 1.65, 'dad', 1.7, 'me', 1.65]