# Multiple Inheritance Ex

class Parent1:
    def __init__(self):
        self.num=100

class Parent2():
    def mtd(self):
        print(self.num)
        
class Sample(Parent1,Parent2): # or (Parent2,Parent1) order doesn't matter here
    pass

Sample().mtd() # 100
