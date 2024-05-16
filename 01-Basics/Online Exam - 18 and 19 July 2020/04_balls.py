# В кутия имаме неопределен брой топки с различни цветове, които ни носят различен брой точки. Задачата ни е да извадим
# Х бр. топки, които ще бъдат въведени от конзолата, като се има в предвид, че всеки различен цвят влияе на точките
# ни по следния начин:
# •	Ако топката е “red” точките ни се повишават с 5.
# •	Ако топката е “orange” точките ни се повишават с 10.
# •	Ако топката е “yellow” точките ни се повишават с 15.
# •	Ако топката е “white” точките ни се повишават с 20.
# •	Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.
# Ако топката е с какъвто и да е цвят, различен от по-горните, точките не се манипулират и програмата продължава
# да работи.
# Вход:
# 1.	От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
# 2.	След това се четат N на брой цветове.
# Изход:
# Отпечатват се следните редове:
# "Total points: {всичките събрани точки}"
# "Red balls: {броят червени топки}"
# "Orange balls: {броят оранжеви топки}"
# "Yellow balls: {броят жълти топки}"
# "White balls: {броят бели топки}"
# "Other colors picked: {броят на избраните топки извън зададените цветове}"
# "Divides from black balls: {броят на пътите, в които точките са били разделяни на 2}"

from math import floor
balls = int(input())

total_points = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_count = 0
other_count = 0

for _ in range(1, balls + 1):
    colour = input()

    if colour == 'red':
        total_points += 5
        red_count += 1
    elif colour == 'orange':
        total_points += 10
        orange_count += 1
    elif colour == 'yellow':
        total_points += 15
        yellow_count += 1
    elif colour == 'white':
        total_points += 20
        white_count += 1
    elif colour == 'black':
        total_points = floor(total_points / 2)
        black_count += 1
    else:
        other_count += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_count}")
print(f"Orange balls: {orange_count}")
print(f"Yellow balls: {yellow_count}")
print(f"White balls: {white_count}")
print(f"Other colors picked: {other_count}")
print(f"Divides from black balls: {black_count}")