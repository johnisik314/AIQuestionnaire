import random
import json
from JSON import *

class Person:
    def __init__(self,name,age):
            self.name = getRandomName()
            self.id = nextUserID()
            self.age = random.randint(0,90)
            self.attributes()

    #initilize random stats
    def attributes(self):
          self.inc = random.randint(0,10)
          self.hob = random.randint(0,10)
          self.heal = random.randint(0,10)
          self.fam = random.randint(0,10)
          self.fri = random.randint(0,10)
          
          
    #return personal info
    def __str__(self): 
        return f"\nName: {self.name}, Age:{self.age}\nIncome:{self.inc} Hobby:{self.hob} Health:{self.heal} Friends:{self.fri} Family:{self.fam}"

    #printout stats
    def stats(self):
        print("\n===Current stats===")
        print(f"   Income: {self.inc}")
        print(f"   Hobby: {self.hob}")
        print(f"   Health: {self.heal}")
        print(f"   Family: {self.fam}")
        print(f"   Friends: {self.fri}")
        print("===             ===")

    #increase stats
    def stat_increase(self,type,incr):
        match type:
            case "Health":
                self.heal += incr
            case "Family":
                self.fam+= incr
            case "Hobby":
                self.hob += incr
            case "Friendship":
                self.fri += incr
            case "Income":
                self.inc +=incr


    #save the person to database
    def save(self):
        data = {"id":self.id,"name": self.name,"age": self.age,"attributes": {"inc": self.inc,"hob": self.hob,"heal": self.heal,"fam": self.fam,"fri": self.fri}}
        writej(data,"data.json")

    #let person pick quest from 3 random quest add it to "personalQs.json"
    def RandomQuest(self):
        with open('quests.json', 'r') as f:
            quests = json.load(f)

        random_quests = random.sample(quests, 3)

        print("\nChoose one of the following quests:")
        for i, quest in enumerate(random_quests, 1):
            print(f"{i}. {quest['quest']} ({quest['type']})")

        while True:
            user_choice = input("Enter the number of your chosen quest (1, 2, or 3): ")
            if user_choice in ['1', '2', '3']:
                chosen_quest = random_quests[int(user_choice) - 1]
                print(f"You have chosen: {chosen_quest['quest']}")
                print(f"Quest type: {chosen_quest['type']}")
                quest["id"]=nextQuestID()
                writej(quest,"personalQs.json")
                break
            else:
                print("Invalid input. Please enter a valid number (1, 2, or 3).")

    #increase stats/ put quest into "completeQs.json" / erase quest from "personalQs.json"
    def fin_quest(self,quest_id):

        #get the quest
        data = get("personalQs.json",quest_id)

        #stat increases
        print(f"\n===Completed Quest===")
        print(data["quest"])
        print("\n=== Stat Increases ===")
        for item in data["type"]:
            print("   ",item,data["type"][item])
            self.stat_increase(item,data["type"][item])
        print("===               ===")

        #addthe quest to coplete quest list
        writej(data,"completeQs.json")
        
        #erase from quest list
        eraseJ("personalQs.json",quest_id)

        