from Person import Person
from JSON import *
import random
 
#person obj
p1 = Person(next_id(),"John",random.randint(0,70))
data = {"id":p1.id,"name": "Kaith","age": p1.age,"attributes": {"str": p1.str,"dex": p1.dex,"int": p1.int}}


#add Person into DB
#writej(data)

writej(data)
print(get(8))