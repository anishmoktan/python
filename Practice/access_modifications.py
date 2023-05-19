#https://www.codecademy.com/courses/python-for-programmers/articles/access-modifications-python

#Public Access Modifier

# class ClassSchedule:
#    def __init__(self, course, instructor):
#        self.course = course
#        self.instructor = instructor
 
#    def display_course(self):
#        print(f'Course: {self.course}, Instructor: {self.instructor}')


# sched = ClassSchedule('Chemistry', 'Mr. Doe') # initializing
 
# sched.display_course() # prints Course: Chemistry, Instructor: Mr. Doe
# sched.course # prints 'Chemistry

#Protected Access Modifier

# class ClassSchedule:
#    def __init__(self, course, instructor):
#        self._course = course # protected
#        self._instructor = instructor # protected
 
#    def display_course(self):
#        print(f'Course: {self._course}, Instructor: {self._instructor}')
 
# sched = ClassSchedule('Biology', 'Ms. Smith')
# sched.display_course()
# print(sched._course)


#Private Access Modifier

class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    def drive(self):
        print("The " + self.__model + " car is driving")

    def stop(self):
        print("The car is stopping")

my_car = Car("Toyota", "Corolla")
my_car.drive()
print(my_car.__make)
print(my_car.__model)