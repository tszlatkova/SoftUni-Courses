# Напишете програма, която познава дали е топло или студено навън. От конзолата се чете един ред – текст,
# който подсказва какво е времето. При въвеждане на "sunny" трябва да се отпечата "It's warm outside!".
# Във всички останали случаи трябва да се отпечата "It's cold outside!".

text = str(input())

if text == 'sunny':
    print("It's warm outside!")
else:
    print("It's cold outside!")