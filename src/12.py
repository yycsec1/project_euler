from utils import sum_of_n, factors

i = 1
not_found = True
while not_found:
    triangle_number = sum_of_n(i)
    if len(factors(triangle_number)) > 500:
        not_found = False
        print(triangle_number)
    i += 1
