import random

health = 0
strength = 0
dex = 0
intelligence = 0
name = input("Select a name for your character: ")

print("""
Races:
1. Humans:
    - Medium health
    - Medium strength
    - Medium dexterity
    - Medium intelligence
2. Elves:
    - Low health
    - Low strength
    - High dexterity
    - High intelligence
3. Dwarves:
    - High health
    - High strength
    - Low dexterity
    - Low intelligence
""")
player_race = int(input("What race do you want to play as?: "))
if player_race == 1:
    health = 3 + random.randint(-1, 1)
    strength = 3 + random.randint(-1, 1)
    dex = 3 + random.randint(-1, 1)
    intelligence = 3 + random.randint(-1, 1)
    player_race = "Human"
elif player_race == 2:
    health = 1 + random.randint(-1, 1)
    strength = 1 + random.randint(-1, 1)
    dex = 5 + random.randint(-1, 1)
    intelligence = 5 + random.randint(-1, 1)
    player_race = "Elf"
elif player_race == 3:
    health = 5 + random.randint(-1, 1)
    strength = 5 + random.randint(-1, 1)
    dex = 1 + random.randint(-1, 1)
    intelligence = 1 + random.randint(-1, 1)
    player_race = "Dwarf"

print(f"""
Character stats:
Health: {health}
Strength: {strength}
Dexterity: {dex}
Intelligence: {intelligence}""")

print("""
Classes:
1. Rogue
    - bonus to health
2. Warrior
    - bonus to strength
3. Ranger
    - bonus to dexterity
4. Wizard
    - bonus to intelligence
""")
player_class = int(input("What class do you want to play as?: "))
if player_class == 1:
    health += random.randint(1, 3)
    player_class = "Rogue"
elif player_class == 2:
    strength += random.randint(1, 3)
    player_class = "Warrior"
elif player_class == 3:
    dex += random.randint(1, 3)
    player_class = "Ranger"
elif player_class == 4:
    intelligence += random.randint(1, 3)
    player_class = "Wizard"

print(f"""
Your character:

Name: {name}      
Race: {player_race}
Class: {player_class}
Health: {health}
Strength: {strength}
Dexterity: {dex}
Intelligence: {intelligence}

Have fun on your adventures!""")