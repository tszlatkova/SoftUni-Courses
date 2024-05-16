# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса.
# Академията ще ви даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка.
# Точките, които актьора получава се формират от: дължината на името на оценяващия умножено по точките, които дава
# делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор
# е получил номинация.
# Вход
# •	Име на актьора - текст
# •	Точки от академията - реално число в интервала [2.0... 450.5]
# •	Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# o	Име на оценяващия - текст
# o	Точки от оценяващия - реално число в интервала [1.0... 50.0]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако точките са над 1250.5:
# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
# •	Ако точките не са достатъчни:
# 	"Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!

actor_name = input()
points_academy = float(input())
judges = int(input())

total_points_actor = points_academy

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())
    total_points_judge = len(judge_name) * judge_points / 2
    total_points_actor += total_points_judge
    if total_points_actor > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points_actor:.1f}!')
        break

else:
    diff = 1250.5 - total_points_actor
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')

# if total_points_actor <= 1250.5:
#     diff = 1250.5 - total_points_actor
#     print(f'Sorry, {actor_name} you need {diff:.1f} more!')