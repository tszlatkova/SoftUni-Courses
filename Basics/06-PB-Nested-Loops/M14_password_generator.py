# Да се напише програма, която чете две цели числа n и l, въведени от потребителя, и генерира по азбучен ред всички
# възможни  пароли, които се състоят от следните 5 символа:
# •	Символ 1: цифра от 1 до n.
# •	Символ 2: цифра от 1 до n.
# •	Символ 3: малка буква измежду първите l букви на латинската азбука.
# •	Символ 4: малка буква измежду първите l букви на латинската азбука.
# •	Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.
# Вход
# Входът се чете от конзолата и се състои от две цели числа n и l в интервала [1…9], по едно на ред.
# Изход
# На конзолата трябва да се отпечатат всички пароли по азбучен ред, разделени с интервал.

n = int(input())
l = int(input())

for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(97, 97 + l):
            for forth in range(97, 97 + l):
                for fifth in range(1, n + 1):
                    if fifth > first and fifth > second:
                        print(f'{first}{second}{chr(third)}{chr(forth)}{fifth}', end = ' ')