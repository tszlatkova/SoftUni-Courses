# Счетоводителят на киноцентър "Тинтява 15" ви наема да напишете програма, която пресмята хонорарите за актьорите.
# Всяка продукция има бюджет за актьори. До команда "ACTION" ще получавате име на актьор и възнаграждението му.
# Ако името на актьора е по-дълго от 15 символа възнаграждението му ще е 20 % от останалия бюджет до момента.
# Ако бюджета в даден момент свърши, програмата трябва да прекъсне.
# Вход
# От конзолата първо се чете един ред:
# •	Бюджет за актьори - реално число в интервала [1000.0... 2 100 000.0]
# След това се четат многократно по един или два реда до команда "ACTION" или до изчерпване на бюджета:
# •	Име на актьор - текст
# Ако името на актьора съдържа по-малко или равно на 15 брой символи:
# o	Възнаграждение - реално число в интервала [250.0… 1 000 000.0]
# Изход
# На конзолата да се отпечата един ред:
# •	Ако бюджета е достатъчен :
#   "We are left with {останал бюджет} leva."
# •	Ако бюджета не е достатъчен:
# 	"We need {необходим бюджет} leva for our actors."
# Резултата да се форматира до втората цифра след десетичния знак!

budget = float(input())

input_line = input()
no_more_money = False

while input_line != 'ACTION':
    actor_name = input_line

    if len(actor_name) > 15:
        budget -= 0.20 * budget
    else:
        actor_payment = float(input())
        budget -= actor_payment

    if budget < 0:
        no_more_money = True
        break

    input_line = input()

if no_more_money:
    print(f'We need {abs(budget):.2f} leva for our actors.')
else:
    print(f'We are left with {budget:.2f} leva.')