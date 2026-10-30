# Inheritance Example

class Parent:
    def __init__(self,num):
        self.num=num
    
class Child(Parent):
    pass

parent=Parent(200)
child=Child(100)

print(child.num) # 100
print(parent.num) # 200
