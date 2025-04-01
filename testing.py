import random
import json
def sort_rarity(filename="CharacterList.json"):
        rarity5 = []
        rarity4 = []
        rarity3 = []
        try:
            with open(filename, 'r') as file:
                existing_characters = json.load(file)
        except FileNotFoundError:
            return "Error: File not found."
        except json.JSONDecodeError:
            return "Error: Invalid JSON format."
        for character in existing_characters:
            rarity = character['rarity']
            name = character['name']
            if rarity == 5:
                rarity5.append({"name": name, "rarity": rarity})
            elif rarity == 4:
                rarity4.append({"name": name, "rarity": rarity})
            else:
                rarity3.append({"name": name, "rarity": rarity})
        rarity3 = sorted(rarity3, key=lambda x: x["name"])
        rarity4 = sorted(rarity4, key=lambda x: x["name"])
        rarity5 = sorted(rarity5, key=lambda x: x["name"])
        return rarity3, rarity4, rarity5

def pulling():
    rarity3, rarity4, rarity5 = sort_rarity() #i need to store the result otherwise it wont work
    Weightedlist=[rarity5,rarity4,rarity3]
    probability = [0.1,0.2,0.7]
    selected_rarity_list = random.choices(Weightedlist, probability)[0]
    selected_character = random.choice(selected_rarity_list)
    print(selected_character)
    Character_Obtained.append(selected_character)
    #saveing the results
    return selected_character

def save():
    try:
        with open("Character_Obtained.json",'r+') as f:
            file=json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        file = []
    existing_names = {char["name"] for char in file}
    characters = [char for char in Character_Obtained if char["name"] not in existing_names]
    currency = sum(10 for char in Character_Obtained if char["name"] in existing_names)
    print(f"Currency : {currency}")
    #save non dupes.
    for char in characters:
        file.append({"name": char["name"], "rarity": char["rarity"]})
    with open("Character_Obtained.json",'w') as f:
            json.dump(file,f,indent=4)
Character_Obtained=[]

for int in range(10):
    pulling()
    save()