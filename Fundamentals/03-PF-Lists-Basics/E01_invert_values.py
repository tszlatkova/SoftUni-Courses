# Write a program that receives a single string containing positive and negative numbers separated by a single
# space. Print a list containing the opposite of each number.

nums = list(map(int,input().split(' ')))

opposite_nums = []

for number in nums:
    opposite_nums.append(-number)

print(opposite_nums)