# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic. You want to
# play it all day long! So cancel all other arrangements and create your party!
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for
# your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by
# a single space in the following format:
# "{hero name} {HP} {MP}"
# -	HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. You will be receiving different
# commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
# •	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200.
# (the MP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100),
# HP is increased to 100 (the HP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"

# Input
# •	On the first line of the standard input, you will receive an integer n.
# •	On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a
# space in the following format.
# •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.

# Output
# •	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2
# spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"

# Constraints
# •	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective
# limits.
# •	The HP/MP amounts in the commands will never be negative.
# •	The hero names in the commands will always be valid members of your party. No need to check that explicitly.

heroes_number = int(input())
heroes_information = {}

for _ in range(heroes_number):
    hero_name, HP, MP = input().split(' ')
    heroes_information[hero_name] = {'HP': int(HP), 'MP': int(MP)}

while True:
    command = input()

    if command == 'End':
        break

    command = command.split(' - ')
    action = command[0]
    hero = command[1]

    if action == 'CastSpell':
        MP_needed = int(command[2])
        spell_name = command[3]

        if heroes_information[hero]['MP'] >= MP_needed:
            heroes_information[hero]['MP'] -= MP_needed
            mana_points_left = heroes_information[hero]['MP']
            print(f"{hero} has successfully cast {spell_name} and now has {mana_points_left} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]
        heroes_information[hero]['HP'] -= damage

        if heroes_information[hero]['HP'] > 0:
            current_HP = heroes_information[hero]['HP']
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_HP} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del(heroes_information[hero])

    elif action == 'Recharge':
        amount = int(command[2])

        if heroes_information[hero]['MP'] + amount > 200:
            amount = 200 - heroes_information[hero]['MP']

        heroes_information[hero]['MP'] += amount
        print(f"{hero} recharged for {amount} MP!")

    elif action == 'Heal':
        amount = int(command[2])

        if heroes_information[hero]['HP'] + amount > 100:
            amount = 100 - heroes_information[hero]['HP']

        heroes_information[hero]['HP'] += amount
        print(f"{hero} healed for {amount} HP!")

for hero in heroes_information.keys():
    current_HP = heroes_information[hero]['HP']
    current_MP = heroes_information[hero]['MP']
    print(f"{hero}\n HP: {current_HP}\n MP: {current_MP}")
