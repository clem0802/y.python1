# pic n° 13-19

#--------------------------------------
# create list "areas"
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# create list "areas_copy"
areas_copy = list(areas)

# reassign 1 value of areas_copy
areas_copy[0] = 5.0

# print 
print(areas)
[11.25, 18.0, 20.0, 10.75, 9.5]
print(areas_copy)
[5.0, 18.0, 20.0, 10.75, 9.5]


#--------------------------------------
# the ; sign is used to place commands on the same line
# the following two code chunks are equivalent:

# (1) on the same line
# command1; command2

# (2) on separate lines
# command1
# command2


#--------------------------------------
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75, "bathroom", 10.50, "poolhouse", 24.5, "garage", 15.45]
del(areas[-4:-2])
print(areas)
#['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'garage', 15.45] => "poolhouse", 24.5,   (TAKEN OFF [-4]&[-3])



#-------------------------------------- MAX()
# to get help on the max() FUNCTION
# help(max)
# ?(max)

#-------------------------------------- POW()
# pow() takes three arguments: BASE-EXP-MOD
# "base" & "exp" are required arguments => BASE ** EXP
# "mod" is optional argument => BASE ** EXP % MOD


#-------------------------------------- merge 2 lists
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second

full_sorted = sorted(full, reverse=False)
print(full_sorted) # [9.5, 10.75, 11.25, 18.0, 20.0]

full_sorted = sorted(full, reverse=True)
print(full_sorted) # [20.0, 18.0, 11.25, 10.75, 9.5]
