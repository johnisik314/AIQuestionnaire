from Person import Person
import random
import json


# File path to save the JSON data


for i in range(4,random.randint(0,10)):

    p1 = Person("John",random.randint(0,70))
    data = {"name": "Kaith","age": 30,"attributes": {"str": p1.str,"dex": p1.dex,"int": p1.int}}
    print (data)
    # Load the existing JSON data
    with open("AIQuestionnaire\data.json") as file:
        jfile = json.load(file)
        print (jfile)

    # Append the new data to the existing JSON
    jfile.append(data)
    
    with open("AIQuestionnaire\data.json","w") as file:
       json.dump(jfile,file, indent =4)
       print (jfile)


print("Data saved as JSON.")