import json
import random
import os
##  EDIT DATABASES ##

# add quest or user info to DBs
def writej(data,path):
    # Load the existing JSON data
    with open(path) as file:
        jfile = json.load(file)
    # Append the new data to the existing JSON
    jfile.append(data)
    #write on json file
    with open(path,"w") as file:
        json.dump(jfile,file, indent =4)

# erase quest or user info from DBs using id
def eraseJ(path,id):
    with open(path,"r") as file:
        jfile = json.load(file)

    for item in jfile:
        if item.get("id") == id:
            jfile.remove(item)
            break

    with open(path,"w") as file:
        json.dump(jfile,file,indent=4)

# get quest or user info from DBs using id
def get(path,id):
    with open(path) as file:
        jfile = json.load(file)
        #print(jfile)  # Print the contents of the loaded JSON data
        for item in jfile:
            if item["id"] == id:
                # Convert the dictionary to a string and return it
                return item

    # If the id is not found, return None or an error message
    return "No data found for the given id: {}".format(id)

def getDB():
    path ="data.json"
    if os.path.exists(path):
        with open("data.json") as file:
            jfile = json.load(file)
        return jfile
    else:
        # If the id is not found, return None or an error message
        return "No data found at path: {path}"

## COUNTERS FOR IDs

#return current user ID (latest: "userCounter.json")
def currentUserID():
    file_path = "userCounter.json"
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    return data[0]['counter']

#return counter for people + increment "userCounter.json"
def nextUserID():
    path = "userCounter.json"
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.load(file)

        counter = data[0]['counter']
        counter = counter + 1

        # Update the counter value in the data
        data[0]['counter'] = counter

        # Write the updated JSON data back to the file
        with open(path, 'w') as file:
            json.dump(data, file)

        return counter
    else:
        print(f"File not found: {path}")

#return current quest ID (latest: "questCounter.json")
def currentQuestID():
    file_path = "questCounter.json"
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    return data[0]['counter']

#return next quest id + increment "questCounter.json" 
def nextQuestID():
    file_path = "questCounter.json"
    
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    counter = data[0]['counter']
    counter = counter + 1

    # Update the counter value in the data
    data[0]['counter'] = counter

    # Write the updated JSON data back to the file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

    return counter


## RANDOM GENERATORS

#return random name
def getRandomName():
    with open("randNames.json", 'r') as json_file:
        data = json.load(json_file)
        return random.choice(data)

    