# Да се напише програма, която чете цяло число, въведено от потребителя, и печата дали е четно или нечетно.
# Ако е четно отпечатайте "even", ако е нечетно "odd".

number = int(input())

if number % 2 == 0:
    print('even')
else:
    print('odd')