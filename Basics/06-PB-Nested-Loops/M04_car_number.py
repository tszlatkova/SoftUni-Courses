# Поздравления, поради вашите задълбочени знания в сферата на програмирането МВР реши да наеме точно вас за създаването
# на новата им система за генериране на специални автомобилни номера. Всеки един специален автомобилен номер се състой
# от четири числа. Условията, които разграничават специалните от обикновените номера са следните:
# •	Ако номерът започва с четна цифра, то той трябва да завършва на нечетна цифра и обратното – ако започва с нечетна,
# завършва на четна
# •	Първата цифра от номера е по-голяма от последната
# •	Сумата от втората и третата цифра трябва да е четно число
# Входа се състой от две числа - начало и край на интервал, между които трябва да се генерира всяко едно число от
# номера.
# Вход
# 1.	Първи ред - едноцифрено число - началото на интервала – цяло число в интервала [1…9]
# 2.	Втори ред - едноцифрено число - края на интервала – цяло число в интервала [1…9]
# Изход
# На конзолата трябва да се отпечатат всички специални номера, разделени с интервал.

start_interval = int(input())
end_interval = int(input())

for w in range(start_interval, end_interval + 1):
    for x in range(start_interval, end_interval + 1):
        for y in range(start_interval, end_interval + 1):
            for z in range(start_interval, end_interval + 1):
                if w > z:
                    if (x + y) % 2 == 0:
                        if (w % 2 == 0 and z % 2 != 0) or (w % 2 != 0 and z % 2 == 0):
                            print(f'{w}{x}{y}{z}', end = ' ')