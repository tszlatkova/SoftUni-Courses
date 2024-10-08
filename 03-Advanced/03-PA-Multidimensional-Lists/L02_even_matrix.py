# Write a program that receives a matrix of numbers and prints a new one only with the
# even numbers. Use nested comprehension for that problem.
# On the first line, you will receive the rows of the matrix. On the next rows, you will
# get elements for each column separated with a comma and a space ", ".

matrix_even = []
rows = int(input())

for _ in range(rows):
    matrix_even.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

print(matrix_even)
