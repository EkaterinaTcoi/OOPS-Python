class employee:
    def __init__(self,firstname,lastname,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + self.lastname + "." + "@kite.com"
    
    def giveRaise (self, salary):
        self.salary = salary
        
class developer (employee):
    def __init__ (self,firstname, lastname, salary, programming_languages):
        super(). __init__ (firstname, lastname,salary) 
        self.prog_lagns = programming_languages 
   
    def addLanguages (self, lang):
        self.prog_langs += [lang]
        
employee1 = employee("Jon","Smith",80000)
print(employee1.salary)

employee1 = giveRaise(100000)
print(employee1.salary)

dev1 = developer ("Joe", "Mantana", 100000, ["Python", "C"])
print(dev1.salary)

dev1.giveRaise (125000)
print(dev1.salary)

dev1.addLanguages("Java")
print(dev1.prog_langs)




