import json
import random

# append json/people database, add person
def writej(data,path):
    # Load the existing JSON data
    with open(path) as file:
        jfile = json.load(file)
    # Append the new data to the existing JSON
    jfile.append(data)
    #write on json file
    with open(path,"w") as file:
        json.dump(jfile,file, indent =4)

def eraseJ(path,id):
    with open(path,"r") as file:
        jfile = json.load(file)

    for item in jfile:
        if item.get("id") == id:
            jfile.remove(item)
            break

    with open(path,"w") as file:
        json.dump(jfile,file,indent=4)

    
# get user info with ID from databse quest or person
def get(path,id):
    with open(path) as file:
        jfile = json.load(file)
        #print(jfile)  # Print the contents of the loaded JSON data
        for item in jfile:
            if item["id"] == id:
                # Convert the dictionary to a string and return it
                return str(item)

    # If the id is not found, return None or an error message
    return "No data found for the given id: {}".format(id)

#return counter, then increment it for person ID in databse
def next_id():
    file_path = "counter.json"
    
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

def next_Qid():
    file_path = "quest_count.json"
    
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    counter = data[0]['count']
    counter = counter + 1

    # Update the counter value in the data
    data[0]['count'] = counter

    # Write the updated JSON data back to the file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

    return counter

#return random name
def get_name():
    with open("listNames.json", 'r') as json_file:
        data = json.load(json_file)
        return random.choice(data)

    