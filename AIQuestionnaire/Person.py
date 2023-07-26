import random
from JSON import *

class Person:
    def __init__(self,name,age):
            self.name = name
            self.id = next_id()
            self.age = random.randint(0,90)
            self.attributes()

    def attributes(self):
          self.inc = random.randint(0,10)
          self.hob = random.randint(0,10)
          self.heal = random.randint(0,10)
          self.fam = random.randint(0,10)
          self.fri = random.randint(0,10)
          
          
    
    def __str__(self): 
        return f"Name: {self.name}, Age:{self.age}\nIncome:{self.inc} Hobby:{self.hob} Health:{self.heal} Friends:{self.fri} Family:{self.fam}"
