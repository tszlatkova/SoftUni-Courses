# Да се напише програма, която чете число n, въведено от потребителя, и печата четните степени на 2 ≤ 2^n:
# 2^0, 2^2, 2^4, 2^6, …, 2^n.

n = int(input())

for i in range(n + 1):
    if i % 2 == 0:
        print(2 ** i)