# 1. SINGLE INHERITANCE
# One child class inherits from one parent.
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    pass

c = Car()
c.start()
# Flow: Vehicle -> Car

# 2. MULTIPLE INHERITANCE
# One child inherits from multiple parents.
class Engine:
    def engine_type(self):
        print("Petrol Engine")
class Wheels:
    def wheel_count(self):
        print("4 Wheels")
class Car(Engine, Wheels):
    pass
c = Car()
c.engine_type()
c.wheel_count()
# Flow: Engine + Wheels -> MultipleCar

# 3. MULTILEVEL INHERITANCE
# A chain of inheritance
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car drives")
class SportsCar(Car):
    def speed(self):
        print("Very fast")
s = SportsCar()
s.start()
s.drive()
s.speed()
# Flow: BaseVehicle -> IntermediateCar -> SportsCar

# 4. HIERARCHICAL INHERITANCE
# Multiple child classes inherit from one parent

class ParentVehicle:
    def start(self):
        print("Vehicle starts")


class Car(ParentVehicle):
    pass
class Bike(ParentVehicle):
    pass
c = Car()
b = Bike()
c.start()
b.start()
# Flow:
#          ParentVehicle
#           /        \
#         Car        Bike

# 5. HYBRID INHERITANCE
# Combination of multiple inheritance types
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Engine(Vehicle):
    def engine(self):
        print("Engine working")

class HybridWheels:
    def wheels(self):
        print("Wheels rolling")

class HybridCar(Engine, HybridWheels):
    pass

c = HybridCar()
c.start()
c.engine()
c.wheels()

# Flow: Combination of hierarchical + multiple inheritance

# QUICK SUMMARY

# Single       : 1 Parent -> 1 Child
# Multiple     : Many Parents -> 1 Child
# Multilevel   : Grandparent -> Parent -> Child
# Hierarchical : 1 Parent -> Many Children
# Hybrid       : Combination of inheritance types
