"""
read: classDay-01.md

base: a application for a company in python for its employee 
"""

class Employee:
    raise_amt = 1.04 # this is the class variable
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'
        
    def fullname(self):
        return ' {} {}'.format(self.first,self.last) # self is refering to all instances in a class

    # @classmetho   d
    def amt_rais(self):
        self.pay = int(self.raise_amt*self.pay)


    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt = amt 

    @classmethod
    def edit(cls,user_str):
        first,last,pay = user_str.split('-')
        return cls(first, last, pay)


class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    

    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def dis_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())



emp_1 = Developer('Ukant','Jadia',30000,'pt')
emp_2 = Developer('Rohit','Jadia',40000,'java') # Employee objects and class

mang_1 = Manager('sue', 'lott', 3000, [emp_1])

mang_1.add_emp(emp_2)
print(mang_1.dis_emp())
# user_input = "Rohit-Rao-302990"
# emp_3 = Employee.edit(user_input)
# print(emp_2.email)
# print(emp_2.pro_langj)
