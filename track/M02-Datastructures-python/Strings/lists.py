# index
numbers = [1, 2, 3, 4, 5, 3]
print(numbers[1:5]) # 2345
print(numbers[3:]) # 453
print(numbers[-4 :- 1]) #345
print(numbers, type(numbers))
print(len(numbers))
print(numbers [3])

# Using constructor
stu = list([1, 2, 3, 4, 45.6, True, "Bhargav"])
print(stu, type(stu))

# adding elements
num = [1, 2, 3, 4, 5]
num.append(6)
num.insert(0, 3)
num.extend([10, 20, 30])
print(num)
# removing the element
num.pop()
num.pop(1)
num.remove(20)
num.clear()
del num
# print(num)

# changing elements
numbers = [1, 2, 3, 4, 5, 3]
numbers[5] = 6
numbers[1:4] = [20, 20, 40]
print(numbers)


a = [1, 2, 3]
b = a.copy()
print(b.index(3)) # 2

lst = [1, 3, 2]
lst.sort(reverse=True)
#lst.reverse()
print(lst)


