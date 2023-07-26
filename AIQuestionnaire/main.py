from Person import Person
import random
import json


# File path to save the JSON data


for i in range(4,random.randint(0,10)):

    p1 = Person("John",random.randint(0,70))
    data = {
        "name": "John",
        "age": 30,
        "attributes": {
            "str": p1.str,
            "dex": p1.dex,
            "int": p1.int
        }
    }

    
    
    # Load the existing JSON data
    with open("AIQuestionnaire\data.json") as file:
        old_data = json.load(file)

    # Append the new data to the existing JSON
    print (data)
    data = old_data + data
    print (data)
    # Write the updated JSON back to the file
    with open("AIQuestionnaire\data.json") as file:
        json.dump(data, file)


print("Data saved as JSON.")