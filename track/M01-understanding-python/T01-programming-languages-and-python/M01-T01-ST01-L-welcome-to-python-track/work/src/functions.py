# add 2 numbers
# No arguments + No return value
def add1():
    a, b = 10, 10
    c = a + b
    print(c)
add1()

# No arguments + return value
def add2():
    a, b = 10, 20
    c = a + b
    return c
print(add2())

# Arguments + No return value
def add3(a, b):
    c = a + b
    print(c)
    add3(10, 50)

# Arguments + return value
def add4(a, b):
    c = a + b
    return c

res = add4(100, 200)
print(res)

# return type
def calc(a, b):
    name = "CHARAN"
    return a + b, a - b
    return 10, 20, 30
    return "charan"
    return f"Good Evening" + name

sum, diff = calc(100, 50)
print(sum)
print(diff)