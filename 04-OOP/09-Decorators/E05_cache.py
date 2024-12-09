# Create a decorator called cache. It should store all the returned values of the
# recursive function fibonacci. You are provided with the code. You need to create a
# dictionary called log that will store all the n's (keys) and the returned results
# (values) and attach that dictionary to the fibonacci function as a variable called log,
# so when you call it, it returns that dictionary. For more clarification, see the
# examples.

def cache(func):

    def wrapper(n):
        if not wrapper.log.get(n):
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Test code 1

fibonacci(3)
print(fibonacci.log)  # {1: 1, 0: 0, 2: 1, 3: 2}

# Test code 2

fibonacci(4)
print(fibonacci.log)  # {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
