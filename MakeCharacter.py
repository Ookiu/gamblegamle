from CharacterLibary import Character
from CharacterLibary import Enemy
from CharacterLibary import Actions
import json
#filename is "CharacterList.json" and "enemyList.json"

wolf = Enemy("wolf",2000,50)
Jax = Character("Jax",1000,100)
Saber = Character("Saber",2000,20)
Skull = Character("Skull",800,200)

Jax.assign_rarity(5)
Saber.assign_rarity(4)
Skull.assign_rarity(3)

Character.SaveCharacter(Jax,"CharacterList.json")
Character.SaveCharacter(Saber,"CharacterList.json")
Character.SaveCharacter(Skull,"CharacterList.json")