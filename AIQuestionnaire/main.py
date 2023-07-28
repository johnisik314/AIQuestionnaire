from Person import *
from JSON import *
import random
 
#person obj
p1 = Person("John",random.randint(0,70))

print(p1)
p1.save() #save the person in database

p1.stats() #print stats
#p1.getRandom() #random 3 quest

#p1.stats()
p1.done_quest(15)
p1.stats()

