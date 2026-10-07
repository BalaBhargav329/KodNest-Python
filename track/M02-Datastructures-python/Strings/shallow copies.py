# Normal assignment(Not a copy)
original = [[10, 20] , [30, 40]]
copy = original
copy[0][0] = 100
print(copy) #[[100,20],[30,40]]
print(original)  #[[100,20],[30,40]]

# Shallow Copy(.copy)
original = [[10, 20] , [30, 40]]
copy = original.copy()
copy[0][0] = 100
print(copy) #[[100,20],[30,40]]
print(original)  #[[10,20],[30,40]]


# # deepcopy(..)
import copy 
original = [[10, 20] , [30, 40]]
copy_list = copy.deepcopy(original)
copy_list[0][0] = 100
print(original)  #[[10,20],[30,40]]
print(copy_list) #[[100,20],[30,40]]




