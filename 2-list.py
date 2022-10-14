# all pics n° 10-12

# to call a certain element in a list
fruits = ['apple','orange','banana','pear','lemon','cherry','strawberry',189]
fruits[0]  # 'apple'
fruits[2]  # 'banana'
fruits[6]  # 'strawberry'
fruits[-1]  # 189
fruits[7] # 189
#--------------------------------------


# SLICE
# [     start : end ]
# [ inclusive : exclusive ]
fruits = ['apple','orange','banana','pear','lemon','cherry','strawberry',189]
fruits[0:3]  # ['apple', 'orange', 'banana']
fruits[4:7]  # ['lemon', 'cherry', 'strawberry']
#--------------------------------------


# LIST-SLICING
# [     start : end ]
# [ inclusive : exclusive ]
fruits = ['apple','orange','banana','pear','lemon','cherry','strawberry',189]
fruits[:3]  # ['apple', 'orange', 'banana']       /(same as [0:3])
fruits[4:]  # ['lemon', 'cherry', 'strawberry', 189]       (NOT same as [4:7])
#--------------------------------------


# SUBSET & ADD
x = ["a","b","c","d"]
x[1] # 'b'
x[-3] # 'b'

x + ['e','f']   
# ['a', 'b', 'c', 'd', 'e', 'f']
x 
# ['a', 'b', 'c', 'd']

x = x + ['e','f']
x
# ['a', 'b', 'c', 'd', 'e', 'f']

y = x + ['g','h']
y 
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#--------------------------------------


# DELETE
del(y[7])
y
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']