import json

# File path to save the JSON data
def writej(data):
    # Load the existing JSON data
    with open("AIQuestionnaire\data.json") as file:
        jfile = json.load(file)
    # Append the new data to the existing JSON
    jfile.append(data)
    #write on json file
    with open("AIQuestionnaire\data.json","w") as file:
        json.dump(jfile,file, indent =4)

#
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
