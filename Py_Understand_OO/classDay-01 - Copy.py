"""
read: classDay-01.md

base: a application for a company in python for its employee 
"""

# It is easy to cerate a class in python 

class Employee:
    raise_amt = 1.04 # this is the class variable

    def __init__(self,first,last,pay): # this will auto initialize instance var for each obj/instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'
        
    def fullname(self):
        return ' {} {}'.format(self.first,self.last) # self is refering to all instances in a class

# day-01: class object/instance
emp_1 = Employee('Ukant','Jadia',30000)
emp_2 = Employee('Rohit','Jadia',40000) # Employee objects and class

# day-02: class variable accessed
Employee.raise_amt = 1.10
emp_1.raise_amt = 2.04
print(Employee.raise_amt) # accessing class var by class name
print(emp_1.raise_amt) # accessing class var by instance
