# Create a class called take_skip. Upon initialization, it should receive a step (int)
# and a count (int). Implement the __iter__ and __next__ functions. The iterator should
# return the count numbers (starting from 0) with the given step. For more clarification,
# see the examples:


class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_count = 0
        self.current_number = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.current_count += 1
        if self.current_count <= self.count:
            self.current_number += self.step
            return self.current_number
        raise StopIteration


# Test code 1

numbers = take_skip(2, 6)
for number in numbers:
    print(number)


# Test code 2

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

# Easier solution is: num = self.current_count * self.step
