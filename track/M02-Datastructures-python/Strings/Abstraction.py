from abc import abstractmethod, ABC

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#Abstract class
class Car(Vehicle):
    def start(self):
        print("car starts")

    @abstractmethod
    def stop(self):
        pass

# Concrete class
class SportsCar(Car):
    def stop(self):
        print("bike stops")

v = SportsCar()
v.start()
v.stop()

