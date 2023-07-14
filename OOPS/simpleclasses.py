#   PYTHON OBJECT ORIENTED PROGRAMMING

class Employee:
    def __init__(self,fname,lname,mail,pay):
        self.fname=fname
        self.lname =lname
        self.mail = mail
        self.pay = pay

    # METHOD CALLED FULL NAME
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

emp1 = Employee("Arun", "Kumar", "arunkuma@gmail.com",5000)
emp2 = Employee("Akash", "Kumar", "akash@cmial.com",7000)
""""
print(emp1)
print(emp2)


emp1.fname = "Aruin"
emp1.lname = "Kumar"
emp1.mail = "arunkumar@company.com"
emp1.pay = 6000


emp2.fname ="tESTER"
emp2.lname = "lname"
emp2.mail = "test@company.com"
emp2.pay = 10000
"""
print(emp1.fname)
print(emp2.fullname())