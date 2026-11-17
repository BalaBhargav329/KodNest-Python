#[1]
class calculator:
    def add(self, a, b):
        print(a+b)
obj = calculator()
obj.add(10, 20) #30
obj.add(10, 30) #40



#[2]
class calculator:
    def add(self, a, b, c=0):
        print(a + b + c)

obj = calculator()
obj.add(10, 20)   #30
obj.add(10, 10, 10) #30
obj.add(10, 20, 30) #60


#[3]
def stu_info(**kwargs):
    print(kwargs)

stu_info(name="Bhargav", age=22, cgpa=7.8)


#[4]
class Payment:
    def pay(self):
        print("Pay money")

class Gpay(Payment):
    def pay(self):
        print("Pay money using Gpay")

class Phonepay(Payment):
    def pay(self):
        print("Pay money using Phonepay")

class Cash(Payment):
    def pay(self):
        print("Pay money using Cash")

g = Gpay()
g.pay()

p = Phonepay()
p.pay()

c = Cash()
c.pay()