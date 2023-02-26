"""
read: classDay-01.md

base: a application for a company in python for its employee 
"""

# It is easy to cerate a class in python 

class Employee:
    raise_amt = 1.04 # this is the class variable
    def __init__(self,first,last,pay):
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

emp_1 = Employee('Ukant','Jadia',30000)
emp_2 = Employee('Rohit','Jadia',40000) # Employee objects and class

## to check that they both are unique print them
# print(f'{emp_1}\n{emp_2}')


## Instance variable 
## this is manually without using class
## It will be unique to each instance of a class
# emp_1.first = 'Ukant'
# emp_1.last = 'Jadia'
# emp_1.email = 'Ukant.Jadia@company.com'
# emp_1.pay = 300000


# print(emp_1.fullname()) # calling a method using instance 
# print(Employee.fullname(emp_1)) # calling a method using class name

# print(f'{emp_1.email}\n{emp_2.email}')

# print(Employee.raise_amt) # accessing class var by class name
# print(emp_1.raise_amt) # accessing class var by instance
## displaying the namespace of class and instance
print(Employee.__dict__)
print(emp_1.__dict__)

Employee.raise_amt = 1.10
emp_1.raise_amt = 2.04
print(Employee.raise_amt) # accessing class var by class name
print(emp_1.raise_amt) # accessing class var by instance

user_input = "Rohit-Rao-302990"
emp_3 = Employee.edit(user_input)
print(emp_3.email)
