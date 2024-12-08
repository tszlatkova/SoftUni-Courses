from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        result = function()
        return [el for el in result if el.lower() in 'aoeiuy']

    return wrapper


# Test code

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
