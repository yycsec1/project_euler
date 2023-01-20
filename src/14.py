from functools import cache


@cache
def collatz_sequence(number):
    if number == 1:
        return [1]
    elif number % 2 == 0:
        return [number] + collatz_sequence(number // 2)
    else:
        return [number] + collatz_sequence(3 * number + 1)


max_len = 0
max_val = 0
for i in range(1, 1_000_000):
    length = len(collatz_sequence(i))
    if length > max_len:
        max_len = length
        max_val = i
print(max_val)
