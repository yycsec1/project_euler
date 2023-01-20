import math


# (2*n)!/(n!)^2
def answer(number):
    return int(math.factorial(2 * number) / (math.factorial(number) ** 2))


print(answer(20))
