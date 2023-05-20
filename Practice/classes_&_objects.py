#https://www.codecademy.com/courses/python-for-programmers/articles/classes-and-objects-python

#A class is a data type that encapsulates information and functions as a blueprint for objects.

class Dog:
   # this is a blank class
   pass
pepper = Dog()
print(pepper)

# Constructors are special functions that are executed when an object is instantiated. 
# In Python, the __init__() function is used as the constructor and is called when creating an object.

class ClassSchedule:
   def __init__(self, course):
       self.course = course
 
first = ClassSchedule('Chemistry')
print(first.course)

################

class Car:
    def __init__(self, make, model): #constructor that instantiates and initializes the new class object
        self.make = make
        self.model = model

    def drive(self):
        print("Your "+ self.model +" car is driving")

    def stop(self):
        print("Your "+ self.model +" car is stopping")
    
    def info(self):
        print("Your car is a " + self.make + " " + self.model)

    def __del__(self): #destructor that deletes the object
        print("You have lost your car :()")

my_car=Car("2023","Maybach")
my_car.drive()
my_car.stop()
del my_car #built in del function that deletes the object

try: my_car.info()
except: print("Your class does not work")
