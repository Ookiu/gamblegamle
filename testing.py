from CharacterLibary import Character
from CharacterLibary import Enemy
import json
import random
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

Character_Obtained = []
rarity3, rarity4, rarity5 = sort_rarity() #i need to store the result otherwise it wont work
Weightedlist=[rarity5,rarity4,rarity3]
prbability = [0.1,0.2,0.7]
selected_rarity_list = random.choices(Weightedlist, prbability)[0]
selected_character = random.choice(selected_rarity_list)
print(selected_character)