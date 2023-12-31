# Деси трябва да заведе котката си на ветеринар в клиниката "Happy Cat", но паркингът се заплаща.
# Напишете програма, която пресмята колко общо трябва да се плати за престоя на колата на Деси на паркинга,
# за да заведе котката си на ветеринар. Паркингът е различен от останалите и има разнообразен ценоразпис.
# За всеки четен ден и нечетен час, паркингът таксува 2.50 лева. Във всеки нечетен ден и четен час таксата е 1.25 лева,
# във всички останали случаи се заплаща 1 лев. Таксуването става на всеки изминал час от деня.
# Всеки един от изходите трябва да бъде закръглен до втория знак след десетичната запетая.
# Вход
# От конзолата се четат два реда:
# •	Брой дни – цяло число в интервала [1 … 5]
# •	Брой часове за всеки един от дните - цяло число в интервала [1 … 24]
# Изход:
# Да се отпечата на конзолата:
# •	За всеки изминал ден, общата сума, която трябва да се плати – "Day: {индексът на деня} – {общата сума за деня} leva"
# •	Когато програмата приключи - "Total: {общата сума за всички дни} leva"

total_days = int(input())
hours_per_day = int(input())

total_price = 0

for day in range(1, total_days + 1):

    price_per_day = 0

    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price_per_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price_per_day += 1.25
        else:
            price_per_day += 1.00

    print(f'Day: {day} - {price_per_day:.2f} leva')
    total_price += price_per_day

print(f'Total: {total_price:.2f} leva')