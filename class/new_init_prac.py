class Circle:
    
    def __new__(self):
        print("Circle's __new__ method call")
        return Circle
    
    def __init__(self, radius):
        self.radius = radius
        print("Circle's __init__ method call")
        
        
c = Circle()

print(c)