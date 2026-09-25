age = int(input("Enter the age"))
if age >= 18:
   print("Eligible for vote")
else:
    print("Not eligible for vote")


marks = int(input("Enter the marks:"))
if marks > 90:
    print("Grade A")
elif marks > 70:
    print("Grade B")
elif marks > 50:
    print("Grade C")
elif marks > 35:
    print("Grade D")
else:
    print("Fail")

free_tonight = True
frinds_available = True
if(free_tonight):
    if(friends_available):
        print("Go out for party")
    else:
        print("seat and watch the movie at home")
else:
    print("not available for party")


day = int(input("Enter a number between 1 to 7:"))
match day:
     case 1:
        print("Monday")
     case 2:
        print("Tuesday")
     case 3:
        print("Wednesday")
     case 4:
        print("Thusday")
     case 5:
        print("Friday")
     case 6:
        print("Saturday")
     case 7:
        print("Sunday")
     case 8:
        print("invalid input")

month = int(input("enter month number(1-12):"))
match-case

month = 3,4,5
   print("Summer")
month = 6,7,8
   print("Rainy")
month = 9,10,11
   print("Winter")
month = 12
   print("Cold")
   else:
      print("invalid month")

#looping statements
#for loop with range
for i in range(1,0):
   print(i)

for i in range(s):
   print(i)

for i in range(1,11):
   if i % 2 == 0:
      print(i)

while i <= 4:
   print(i)
   i += 1 # i - i + 1


# jumping statements
# break statement
# write a python Program to print number from 1 to 5, but stop
for i in range(1, 6):
   if i == 4:
      break
   print(i)

   for i in range(1, 6):
      if i == 4:
         continue
      print(i)

      for i in range(1, 10):
         pass

      def add():
         pass

      def square(n):
         return n*n
      print(square(3))