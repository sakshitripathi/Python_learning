#single inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return f"{self.name} makes sound"
class Dog(Animal):
    def sound(self):
        return f"{self.name} barks"

dog=Dog("labrador")
print(dog.sound())

#multiple inheritance
class Brand:        
    def __init__(self,brandname):
        self.brandname=brandname
    
class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
class Car(Brand,Engine):
    def __init__(self,horsepower, brandname, model):
        Engine.__init__(self,horsepower)
        Brand.__init__(self,brandname)
        self.model=model
    def characteristics(self):
        return f"{self.brandname}'s {self.model} has {self.horsepower}"
car=Car("750hp","Mercedes","power Engine")
print(car.characteristics())

##multilevel inheritance

class Person:
    def __init__(self,name):
        self.name=name
    def intro(self):
        return f"my name is {self.name}"    
class Employee(Person):
    def __init__(self,name,empid):
        super().__init__(name)
        self.empid=empid
    def work(self):
        return f"{self.name} has employee id {self.empid}"    
class Manager(Employee):
    def __init__(self,name,empid,teamsize):
        super().__init__(name,empid)
        self.teamsize=teamsize
    def manage(self):
        return f"{self.name}'s employee id is {self.empid} and they manages {self.teamsize} people"    
manager=Manager("Alice",1,40)
print(manager.intro())
print(manager.work())
print(manager.manage())
        
        
                           