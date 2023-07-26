import json


# File path to save the JSON data

def writej(data):
    # Load the existing JSON data
    with open("AIQuestionnaire\data.json") as file:
        jfile = json.load(file)
        print (data)
    # Append the new data to the existing JSON
    jfile.append(data)
    #write on json file
    with open("AIQuestionnaire\data.json","w") as file:
        json.dump(jfile,file, indent =4)
        print (data)