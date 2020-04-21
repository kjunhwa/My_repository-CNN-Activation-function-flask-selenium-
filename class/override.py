class Parent:
    
    def __init__(self, firstname):
        self.firstname = firstname
        
    def __str__(self):
        return self.firstname
        
        
class Baby(Parent):
    
    def __init__(self, firstname, lastname):
        
        super().__init__(firstname)
        self.lastname = lastname
        
    def __str__(self):
        return "Baby name : " + super().__str__() + str(self.lastname)
    
name_baby = Baby("Kim", "Junhwa")
print(name_baby)