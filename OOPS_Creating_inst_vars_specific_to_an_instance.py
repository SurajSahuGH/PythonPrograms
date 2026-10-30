# An alternate way of creating instance variables(attributes) for a specific instance(object)

class A:
    count=0
    
    def __init__(self):
        self.__x = 100
        
obj1 = A()
obj1.__x = 200 # Creating an inst var rather than modifying pvt inst var with the same name 

print(obj1.__x) # 100, This is an instance variable created outside of the class specifically for 'obj1' instance
             

print(obj1._A__x) # 200, This is the pvt instance variable which created inside the class
                  # so both _A__x and __x are different instance var

obj1.y = 20 # Again another inst var specific to obj1 instance

print(obj1.y)

print(dir(obj1), len(dir(obj1))) # So obj1 has (count, _A__x, __x, y) one static & three inst vars

obj2 = A()
print(dir(obj2), len(dir(obj2))) # while obj2 has only (count, _A__x) one static & one inst vars
