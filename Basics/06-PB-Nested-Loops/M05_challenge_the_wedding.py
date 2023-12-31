# Провокирани от сватбата си, Михаела и Иван решават да предоставят нова услуга на клиенти на ресторанта си,
# а именно вечеря за запознанства - "Предизвикай Сватбата". Напишете програма, която отпечатва всички възможни срещи на
# клиентите на ресторанта. При настаняване всеки мъж и всяка жена получават талончета с поредни номера стартирайки от 1.
# Ако бъдат заети всички маси, програмата трябва да приключи. Всяка маса има две места.
# Вход
# От конзолата се четат точно 3 числа, всяко на отделен ред:
# •	Броя клиенти мъже - цяло число в интервала [1...100]
# •	Броя клиенти жени - цяло число в интервала [1...100]
# •	Максималният брой маси - цяло число в интервала [1...100]
# Изход
# На конзолата се принтират на един ред, разделени с интервал всички срещи в следният формат:
# •	({№ клиент} <-> {№ клиент}) ({№ клиент} <-> {№ клиент}) ...

men = int(input())
women = int(input())
tables = int(input())

taken_tables = 0
all_tables_taken = False

for x in range(1, men + 1):
    for y in range(1, women + 1):
        taken_tables += 1

        print(f'({x} <-> {y})', end = ' ')

        if taken_tables == tables:
            all_tables_taken = True
            break

    if all_tables_taken:
        break