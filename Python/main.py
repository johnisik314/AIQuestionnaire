from Person import *
from JSON import *
import random
 
print("yoo")
p1 = Person("John",random.randint(0,70))

print(p1) #out personal info
p1.save() #save the person in database

p1.RandomQuest() #random 3 quest

p1.fin_quest(currentQuestID()) # complete a quest
p1.stats() #print stats

#test