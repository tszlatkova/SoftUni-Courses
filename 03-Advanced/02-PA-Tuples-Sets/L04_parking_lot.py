# Write a program that:
# •	Records a car number for every car that enters the parking lot
# •	Removes a car number when the car leaves the parking lot

# On the first line, you will receive the number of commands - N. On the following N
# lines, you will receive the direction and car's number in the format: "{direction},
# {car_number}". The direction could only be "IN" or "OUT". Print the car numbers which
# are still in the parking lot. Keep in mind that all car numbers must be unique. If the
# parking lot is empty, print "Parking Lot is Empty".

# Note: The order in which we print the result does not matter.

number_commands = int(input())

parking = set()

for _ in range(number_commands):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        parking.add(car_number)
    elif direction == 'OUT':
        if car_number in parking:
            parking.remove(car_number)

if parking:
    print(*parking, sep='\n')
else:
    print('Parking Lot is Empty')


# Ines' solution with mapper

# def add_car(iterable, car):
#     iterable.add(car)
#
#
# def remove_car(iterable, car):
#     if car in iterable:
#         iterable.remove(car)
#
#
# n = int(input())
# parking = set()
#
# mapper = {"IN": add_car, "OUT": remove_car}
#
# for _ in range(n):
#     direction, car_number = input().split(", ")
#     mapper[direction](parking, car_number)
#
#
# if parking:
#     print(*parking, sep="\n")
# else:
#     print("Parking Lot is Empty")
