# Python program to demonstrate use of class method and static method.
from datetime import date

class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter+=1

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year): # factory method - alternate way of creating object
        return cls(name, date.today().year - year)

    @classmethod
    def get_counter(cls):
        return cls.counter

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age): # utility method 
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
print(Person.get_counter())

