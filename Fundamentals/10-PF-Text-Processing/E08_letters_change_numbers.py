# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters. For the given string, you should perform different
# mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping
# track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers, it
# became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each
# string.
# Input
# •	The input comes from the console as a single line, holding a sequence of strings
# •	Strings are separated by one or more white spaces
# •	The input data will always be valid. There is no need to check it explicitly
# Output
# •	Print at the console a single number:
# o	The total sum of all processed numbers, formatted to the second decimal separator
# Constraints
# •	The count of the strings will be in the range [1 … 10]
# •	The numbers between the letters will be integers in the range [1 … 2 147 483 647]
# •	Time limit: 0.3 sec. Memory limit: 16 MB

import re

input_line = input()
input_strings = re.split(' +|\t', input_line) # remove all white spaces and the tabulation
total_sum = 0

for string in input_strings:
    if string != '':

        first_letter = string[0]
        number = int(string[1:len(string)-1])
        last_letter = string[-1]

        if first_letter.isupper():
            number /= ord(first_letter) % 64
        else:
            number *= ord(first_letter) % 96

        if last_letter.isupper():
            number -= ord(last_letter) % 64
        else:
            number += ord(last_letter) % 96

        total_sum += number

print(f'{total_sum:.2f}')
