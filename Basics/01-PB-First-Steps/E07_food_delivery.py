# EXAM

# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.

# Вход
# От конзолата се четат 3 реда:
# •	Брой пилешки менюта – цяло число в интервала [0 … 99]
# •	Брой менюта с риба – цяло число в интервала [0 … 99]
# •	Брой вегетариански менюта – цяло число в интервала [0 … 99]

# Изход
# Да се отпечата на конзолата един ред:  "{цена на поръчката}"


number_chicken = int(input())
number_fish = int(input())
number_vegetarian = int(input())

chicken_price = number_chicken*10.35
fish_price = number_fish*12.40
vegeterian_price = number_vegetarian*8.15
menues_price = chicken_price + fish_price + vegeterian_price
dessert_price = 0.2*menues_price
delivery = 2.50

total = menues_price + dessert_price + delivery

print(total)
