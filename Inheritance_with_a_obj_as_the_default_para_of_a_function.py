# Inheritance with a child type object as the default parameter of a function.

class Parent:
    def mtd(self):
        print("Parent")
        
class Child(Parent):
    def mtd(self):
        print("Child")
        
def change(o=Child()): # Child class object as the default parameter
    o.mtd()

    
change() # Child
change(Parent()) # Parent
change(Child()) # Child
 
