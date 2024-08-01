# Write a program that receives a text on the first line and times (to repeat the text)
# that must be an integer. If the user passes a non-integer type for the times variable,
# handle the exception and print a message

# "Variable times must be an integer".

text_to_repeat = input()

try:
    times = int(input())
    print(text_to_repeat*times)
except ValueError:
    print('Variable times must be an integer')
