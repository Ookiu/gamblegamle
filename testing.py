from CharacterLibary import Character
from CharacterLibary import Enemy
from CharacterLibary import Actions
import json

print("Character and enemy maker initialized.")
selection = input(f"Select Character or Enemy.\n")
if selection == "Character":
    print("Selected Character")
elif selection =="Enemy":
    print("Select Enemy")
else:
    print(f"Not an avilable option, please select Character or Enemy.\n *your input is case sensitive*")

