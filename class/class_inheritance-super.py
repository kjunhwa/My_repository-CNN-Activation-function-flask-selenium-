class Parent:
    
    def __init__(self, firstname):
        
        self.firstname = firstname
        
    def name(self):
        
        return self.firstname
    
class Baby(Parent):
    
    def __init__(self, firstname, lastname):
        
        #Parent.__init__(self, firstname)
        super().__init__(firstname)
        self.lastname = lastname
        
    
    def info(self):
        
        return "Baby name : " + self.name() + " " + str(self.lastname)
    
class BabyInfo(Parent):
    
    def __init__(self, firstname, age):
        
        #Parent.__init__(self, firstname)
        super().__init__(firstname)
        self.age = age
        
    def info(self):
        
        return "Baby age : " + str(self.age)
    
name_baby = Baby("Kim", "Junhwa")
age_baby = BabyInfo("Kim", 28)

print(name_baby.info())
print(age_baby.info())