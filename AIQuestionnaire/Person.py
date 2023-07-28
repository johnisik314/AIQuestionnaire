import random
import json
from JSON import *

class Person:
    def __init__(self,name,age):
            self.name = get_name()
            self.id = next_id()
            self.age = random.randint(0,90)
            self.attributes()

    #initilize random stats
    def attributes(self):
          self.inc = random.randint(0,10)
          self.hob = random.randint(0,10)
          self.heal = random.randint(0,10)
          self.fam = random.randint(0,10)
          self.fri = random.randint(0,10)
          
          
    #returrn essential info
    def __str__(self): 
        return f"Name: {self.name}, Age:{self.age}\nIncome:{self.inc} Hobby:{self.hob} Health:{self.heal} Friends:{self.fri} Family:{self.fam}"

    #print stats
    def stats(self):
        print(f"Income: {self.inc}")
        print(f"Hobby: {self.hob}")
        print(f"Heal: {self.heal}")
        print(f"Family: {self.fam}")
        print(f"Friends: {self.fri}")

    
    #save the person to database
    def save(self):
        data = {"id":self.id,"name": self.name,"age": self.age,"attributes": {"inc": self.inc,"hob": self.hob,"heal": self.heal,"fam": self.fam,"fri": self.fri}}
        writej(data)

    #let person pick quest from 3 random quest
    def getRandom(self):
        with open('quests.json', 'r') as f:
            quests = json.load(f)

        random_quests = random.sample(quests, 3)

        print("Choose one of the following quests:")
        for i, quest in enumerate(random_quests, 1):
            print(f"{i}. {quest['quest']} ({quest['type']})")

        while True:
            user_choice = input("Enter the number of your chosen quest (1, 2, or 3): ")
            if user_choice in ['1', '2', '3']:
                chosen_quest = random_quests[int(user_choice) - 1]
                print(f"You have chosen: {chosen_quest['quest']}")
                print(f"Quest type: {chosen_quest['type']}")
                break
            else:
                print("Invalid input. Please enter a valid number (1, 2, or 3).")

        