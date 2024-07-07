# We think the process of making honey is amazing! Let's learn more about how bees make
# honey.
# Worker bees collect nectar. When a worker-bee has found enough nectar, she returns to t
# he hive to drop off the load and pass the nectar to waiting bees so they can really
# start the honey-making process.
# You will receive 3 sequences:
# •	a sequence of integers, representing working bees
# •	a sequence of integers, representing nectar
# •	a sequence of symbols – "+", "-", "*", or "/", representing the honey-making process.
# Your task is to check if the bee has collected enough nectar to return to the hive and
# keep track of the total honey waiting for bees made with the collected nectar.
# Step one: check if a bee has collected enough nectar. You should take the first bee and
# try to match it with the last nectar:
# •	If the nectar value is more or equal to the value of the bee, it is considered
# collected, and the bee returns to the hive to drop off the load (step two).
# •	If the nectar value is less than the value of the bee, you should remove the nectar
# and try to match the bee with the next nectar's value until the bee collects enough
# nectar.
# Step two: When a bee successfully collects nectar, she returns to the hive, and you
# should calculate the honey made. Take the first symbol in the sequence of symbols
# ("+", "-", "*" or "/") and make the corresponding calculation:
# "{matched_bee} {symbol} {matched_nectar}"
# The result represents the honey that is made from the passed nectar. The calculation
# should always return the absolute value of the result. After the calculation, remove
# the bee, the nectar, and the symbol.
# •	If the symbol is "/" and the nectar’s value is 0 (zero), skip the calculation and
# remove the bee, the nectar, and the symbol.
# Stop making honey when you are out of bees or nectar.
# Input
# •	On the first line, you will be given the values of bees - integers, separated by a
# single space
# •	On the second line, you will be given the nectar's values - integers, separated by a
# single space
# •	On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a
# single space
# Output
# •	On the first line - print the total honey made:
# o	"Total honey made: {total honey}"
# •	On the next two lines print the bees or the nectar that are left, if there are any,
# otherwise skip the line:
# o	"Bees left: {bee1}, {bee2}, … {beeN}"
# o	"Nectar left: {nectar1}, {nectar2}, … {nectarN}"
# Constraints
# •	All the bee's values will be integers in the range [0, 150]
# •	Nectar's values will be integers in the range [0, 150]
# •	There always will be enough symbols in the sequence of symbols

import operator
from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

total_honey = 0

while nectar and bees:
    if nectar[-1] >= bees[0]:
        bee_to_return = bees.popleft()
        collected_nectar = nectar.pop()
        action = symbols.popleft()

        if action == '/' and collected_nectar == 0:
            continue
        else:
            total_honey += abs(operation[action](bee_to_return, collected_nectar))
    else:
        nectar.pop()
        continue

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
