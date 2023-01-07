import math


def find_first_factor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i
    return number


def is_prime(number):
    if number == 2:
        return True
    sq_root = int(math.sqrt(number)) + 2
    for i in range(2, sq_root):
        if number % i == 0:
            return False
    return True
