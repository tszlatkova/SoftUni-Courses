# Да се напише програма, която чете едно цяло число N, въведено от потребителя, и генерира всички възможни "специални"
# числа от 1111 до 9999. За да бъде “специално” едно число, то трябва да отговаря на следното условие:
# •	N да се дели на всяка една от неговите цифри без остатък.
# Пример: при N = 16, 2418 е специално число:
# •	16 / 2 = 8 без остатък
# •	16 / 4 = 4 без остатък
# •	16 / 1 = 16 без остатък
# •	16 / 8 = 2 без остатък
# Вход
# Входът се чете от конзолата и се състои от едно цяло число в интервала [1…600000]
# Изход
# На конзолата трябва да се отпечатат всички “специални” числа, разделени с интервал

n = int(input())
it_is_special = False

for number in range(1111, 10000):
    str_number = str(number)

    for index in range(len(str_number)):
        if int(str_number[index]) != 0 and n % int(str_number[index]) == 0:
            it_is_special = True
        else:
            it_is_special = False
            break

    if it_is_special:
        print(number, end = ' ')
