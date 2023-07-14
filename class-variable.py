#OOPS 
# CLASS 
class Employees:
    numofemp = 1

    #class variable
    raise_amount = 1.4
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname =lname
        self.mail=fname + '.'+'@company.com'
        self.pay=pay
        self.numofemp += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)




emp1 = Employees('Tom', 'Cruise', 6000)

'''print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
'''
print(emp1.__dict__)
print(Employees.__dict__)
print(Employees.numofemp)