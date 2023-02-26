"""
read: classDay-01.md

base: a application for a company in python for its employee 
"""

# It is easy to cerate a class in python 

class Employee:
    raise_amt = 0 # this is the class variable

    def __init__(self,first,last,pay): # this will auto initialize instance var for each obj/instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'
        
    def fullname(self):
        return ' {} {}'.format(self.first,self.last) # self is refering to all instances in a class
    
    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt = amt 

    @classmethod
    def edit(cls,user_str):
        first,last,pay = user_str.split('-')
        return cls(first, last, pay)
    
    # static method
    @staticmethod
    def workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# day-01: class object/instance
emp_1 = Employee('Ukant','Jadia',30000)
emp_2 = Employee('Rohit','Jadia',40000) # Employee objects and class

## day-02: class variable accessed
# Employee.raise_amt = 1.10
# emp_1.raise_amt = 2.04
# print(Employee.raise_amt) # accessing class var by class name
# print(emp_1.raise_amt) # accessing class var by instance

## day-03 class method
emp_1.set_raise_amt(2.001)
# print(emp_1.raise_amt) # accessing class var by instance
Employee.set_raise_amt(4.01)
# print(Employee.raise_amt) # accessing class var by class name

## que: let say user entring the data with hypen at the place of the ,or space
user_input = "Rohit-Rao-302990"
emp_3 = Employee.edit(user_input)
print(emp_3.email)

## regular method
import datetime
my_date = datetime.date(2023,2,24)
print(Employee.workday(my_date))