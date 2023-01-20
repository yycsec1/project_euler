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


def sum_of_n(number):
    return int(number * (number + 1) / 2)


def factors(number):
    num_factors = set()
    root = math.sqrt(number)
    for i in range(1, int(root) + 1):
        if number % i == 0:
            num_factors.add(i)
            num_factors.add(number // i)
    return num_factors
