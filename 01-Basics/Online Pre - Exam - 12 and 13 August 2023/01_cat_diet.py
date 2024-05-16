# За да са здрави котките, храненето им трябва да следва определена диета. Напишете програма, която изчислява
# котешкото процентно разпределение на макроелементите в храната за един ден и пресмята колко средно калории
# дава един грам от тази храна. Макроелементите са: мазнини, протеини и въглехидрати.
# Разполагате с общия брой калории, които котката трябва да приеме за един ден.
# Известно е, че:
# •	1 грам мазнини = 9 калории
# •	1 грам протеини = 4 калории
# •	1 грам въглехидрати = 4 калории
# За да разберете колко калории дава един грам храна на котката, ще трябва да направите изчисления с реалното
# тегло на храната, тъй като тя съдържа вода. Трябва да се изчислят грамовете на мазнините, протеините и въглехидратите.
# Тяхната сума дава общото тегло на храната и от него трябва да извадим процентите вода.
# Вход:
# От конзолата се прочитат 5 реда:
# •	Процент на мазнините - цяло число в интервала [0…100]
# •	Процент на протеините - цяло число в интервала [0…100]
# •	Процент на въглехидратите - цяло число в интервала [0…100]
# •	Общ брой калории - цяло число в интервала [1000…15000]
# •	Процент на съдържанието на вода - цяло число в интервала [0…100]
# Пояснение: Когато правим подобни изчисления с проценти има голям шанс резултатът да не е цяло число!

fats_percentage = int(input())
protein_percentage = int(input())
carbs_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())

total_gr_fats = (fats_percentage / 100 * total_calories) / 9
total_gr_protein = (protein_percentage / 100 * total_calories) / 4
total_gr_carbs = (carbs_percentage / 100 * total_calories) / 4

food_gr = total_gr_carbs + total_gr_fats + total_gr_protein
calories_per_gram = total_calories / food_gr

not_water = (100 - water_percentage) / 100 * calories_per_gram

print(f'{not_water:.4f}')