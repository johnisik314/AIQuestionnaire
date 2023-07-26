from Person import *
from JSON import *
import random
 
#person obj
p1 = Person("John",random.randint(0,70))
data = {"id":p1.id,"name": get_name(),"age": p1.age,"attributes": {"inc": p1.inc,"hob": p1.hob,"heal": p1.heal,"fam": p1.fam,"fri": p1.fri}}


writej(data)
#print(get(173))
#print (get_name())
