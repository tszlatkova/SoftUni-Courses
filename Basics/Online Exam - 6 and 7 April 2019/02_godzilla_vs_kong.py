# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете
# програма, която да изчисли, дали предвидените средства са достатъчни за снимането на филма. За снимките  ще бъдат
# нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.

budget = float(input())
stuntmen = int(input())
clothes_price_per_stuntman = float(input())

set_price = budget * 0.10

clothes_total = 0

if stuntmen > 150:
    clothes_total = stuntmen * clothes_price_per_stuntman * 0.90
else:
    clothes_total = stuntmen * clothes_price_per_stuntman

total_price = set_price + clothes_total

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')