# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете програма,
# която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато постигне целта си
# да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла
# "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла
# докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише:
# "{разликата между стъпките} more steps to reach goal."

input_line = input()

total_steps = 0
goal_reach = False

while input_line != 'Going home':
    steps = int(input_line)
    total_steps += steps

    if total_steps >= 10000:
        goal_reach = True
        break

    input_line = input()

else:
    final_steps = int(input())
    total_steps += final_steps

    if total_steps >= 10000:
        goal_reach = True

diff = abs(total_steps - 10000)
if goal_reach:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')