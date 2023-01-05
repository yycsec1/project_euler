import math


def find_first_factor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i
    return number


def is_prime(number):
    number = int(math.sqrt(number)) + 2
    for i in range(2, number):
        if number % i == 0:
            return True
    return False