#1
marks = [72, 81, 60]
student_marks = marks
student_marks[0] = 100
print(student_marks) # [100, 81, 60]
print(marks) # [100, 81, 60]


#2
first = [1, 2, 3]
second = first
print(first is second) # True
print(first == second) # True


#3
first = [1, 2, 3]
second = [1, 2, 3]
print(first is second) # False
print(first == second) # True


#4
num = [10, 20]
values = num
values.append(30)
print(num) # [10, 20, 30]
print(values) # [10, 20, 30]


#5
num = [10, 20]
values = num
values = [100, 200]
print(num) # [10, 20]
print(values) # [100, 200]

