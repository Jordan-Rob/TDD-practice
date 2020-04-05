
def add(a, b):
    total = a + b
    return total


def subtract(a, b):
    if b > a:
        raise ValueError(
            'you cant subtract from a larger number!, we dont want negatives')
    diff = a - b
    return diff


def divide(a, b):
    division = (a/b)
    return division


def multiply(a, b):
    product = a * b
    return product


def greater(a, b):
    larger = a > b
    return larger
