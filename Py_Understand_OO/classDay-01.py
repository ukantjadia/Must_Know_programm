"""
read: classDay-01.md

base: a application for a company in python for its employee 
"""

# It is easy to cerate a class in python 

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'
        
    def fullname(self):
        return ' {} {}'.format(self.first,self.last) # self is refering to all instances in a class

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

print(emp_1.fullname()) # calling a method using instance 
print(Employee.fullname(emp_1)) # calling a method using class name

print(f'{emp_1.email}\n{emp_2.email}')
