# To print Hello World
"""Start
  print "Hello World" 
 stop"""
print("Hello world" , end=" - ") 
print("Thank you for learning python")
name = "Balu"
print("Name:\t", name)

# To find wheather number (n) is even or odd
"""START
INPUT n
IF n%2 == 0
    PRINT "Even"
ELSE
    PRINT "Odd"
END"""

n = 10
if n%2 == 0:
    print("Even")
else:
    print("odd")

# To find the number is pos, neg or zero
"""START
INPUT n
IF n>0
    PRINT "Positive"
ELSE IF n==0
    PRINT "Zero"
ELSE
    PRINT"Negative"
END"""
n = 2
if n > 0:
     print("Positive")
elif n < 0:
     print("Negative")
else:
    print("Zero")
   

# To find the largest among 3 number a, b, c
""""START
INPUT a,b,c
IF a>b AND a>c
    PRINT "Largest is a"
ELSE IF b>a AND b>c
    PRINT "Largest is b"
ELSE
    PRINT "Largest is c"
END"""

a = 10; b = 2; c = 0
if a >= b and a >= c:
    print("Largest is a")
elif b >= a and b >= c:
    print("Largest is b")
else:
    print("Largest is c")