x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #
print(x is y) #
print(x == y) #

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) #checks for values
print(x is y) #checks for pointing same object

print("-------------------Membership operators-------------")
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # true

fruits = ["apple", "banana", "cherry"]

print("------------------------Bitwise operators-----------------------------")
a = 4
b = 3
print("a & b =", a & b) #
print("a | b =", a | b) #
print("a ^ b =", a ^ b) #
print("~a =", ~a) #
print("a << 1 =", a << 1) #
print("a >> 1 =", a >> 1) #

print("--------------------Ternary operator in python----------------------------")
num = 15
res = "Even" if num % 2 == 0 else "odd"
print(res)

#wap to find largest of 3 numbers