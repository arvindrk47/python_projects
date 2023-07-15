import datetime



class Employees:
    num_of_emp =0
    raise_amt = 1.04

    def __init__(self, fname, lname,pay):
        self.fname =fname
        self.lname=lname
        self.mail=fname+'.'+'@cmp.com'
        self.pay=pay

        Employees.num_of_emp +=1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amt)


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

    @classmethod
    def from_string(cls, emp_str):
        fname,lname,pay=emp_str.split('-')
        return cls(fname,lname,pay) 
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    




emp1=Employees('Tom', 'Cruise', 90000)
emp2=Employees('Arjun', 'Kumar', 8989898)
'''
emp3 ='John-Doe-8999'
emp4='Chirs-hemsworth-0909099'
emp5='cpatin-ameria-989898'

fname,lname,pay=emp3.split('-')
fname,lname,pay=emp4.split('-')
fname,lname,pay=emp5.split('-')

newform=Employees.from_string(emp3)
Employees.set_raise_amt(1.5)
print(Employees.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

print(newform.lname)
'''

mydate = datetime.date(2022,7,9)
print(Employees.is_workday(mydate))