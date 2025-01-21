import random

# Dice Options using list() and range()
diceOptions = list(range(1, 7))

#Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# Inputs combat strength hero
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input ! Combat strenght should be between 1 and 6.")
    combatStrength = 1 #Default value for invalid input

#Input combat strength for monster
mCombatStrength = int(input("Enter monster's combat strength (1-6): "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input ! Monster Combat strenght should be between 1 and 6.")
    mCombatStrength = 1 #Default value for invalid input

    

# # Battle
# for j in range(1, 21, 2):
#     heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
#     heroTotal, monsterTotal = combatStrength + heroRoll, mCombatStrength + monsterRoll
#     print(f"Round {j}: Hero({weapons[heroRoll - 1]})={heroTotal}, Monster({weapons[monsterRoll - 1]})={monsterTotal}.", 
#           "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
#     if j == 11:
#         print("Battle Truce declared. Game Over!")
#         break