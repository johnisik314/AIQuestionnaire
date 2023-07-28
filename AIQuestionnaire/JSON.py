import json
import random

# append json/people database, add person
def writej(data):
    # Load the existing JSON data
    with open("AIQuestionnaire\data.json") as file:
        jfile = json.load(file)
    # Append the new data to the existing JSON
    jfile.append(data)
    #write on json file
    with open("AIQuestionnaire\data.json","w") as file:
        json.dump(jfile,file, indent =4)

# get user info with ID from databse
def get(id):
    with open("AIQuestionnaire\data.json") as file:
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
    file_path = "AIQuestionnaire\counter.json"
    
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

#return random name
def get_name():
    file_path = "AIQuestionnaire\listNames.json"
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return random.choice(data)

    