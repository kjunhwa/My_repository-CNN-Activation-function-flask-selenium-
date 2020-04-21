class UndefinedValue(Exception):
    
    def __str__(self):
        return "Not Defined"
    
vehicle = input("Choose one vehicle in the example : Car, train")

try:
    if vehicle not in ["car", "train"]:
        raise UndefinedValue
except UndefinedValue as e:
    print(e)