from CharacterLibary import Actions
import json
#filename is for character "CharacterList.json" and enemy is "enemyList.json"
with open("CharacterList.json",'r') as f:
    character_stats = json.load(f)
with open("enemyList.json",'r') as f:
    enemies = json.load(f)

#making a file for player 
with open("Playerinfo.json", 'a+') as f:
    player_info = f.read()

print(player_info)    
Actions.attack(Jax,wolf)