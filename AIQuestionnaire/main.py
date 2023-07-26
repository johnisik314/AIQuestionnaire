from Person import Person
from JSON import *
import random


#person obj
p1 = Person("John",random.randint(0,70))
data = {"name": "Kaith","age": p1.age,"attributes": {"str": p1.str,"dex": p1.dex,"int": p1.int}}



writej(data)

print("Data saved as JSON.")