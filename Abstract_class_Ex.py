# Abstract class with Multilevel Inheritance

from abc import ABC,abstractmethod


class Parent(ABC):
    @abstractmethod
    def sample(self): pass
    
    
class Child(Parent):
    pass


class GrandChild(Child): 
    def sample(self): pass

    
class GreatGrandChild(GrandChild):
    pass


g=GrandChild()
print(g.sample()) # None, because sample() in GrandChild has no body.
