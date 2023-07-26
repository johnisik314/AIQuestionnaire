import random
class Person:
    def __init__(self,id,name,age):
            self.name = name
            self.id = id
            self.age = random.randint(0,90)
            self.attributes()

    def attributes(self):
          self.str = random.randint(0,25)
          self.dex = random.randint(0,25)
          self.int = random.randint(0,25)
    
    def __str__(self): 
        return f"Name: {self.name}, Age:{self.age}\nSTR:{self.str} DEX:{self.dex} INT:{self.int}"
