# Exception handling tricky Ex

class Test1(Exception):
    pass

class Test2:
    def sample(self):
        try:
            raise Test1
        except Test1:
            print(1) #1 this will execute
        finally:
            print(2) #2 then this

            
try:
    Test2().sample() # From here
except Test1:
    print(3)
finally:
    print(4) #3 Lastly this one

# output-- 1 2 4
