import utils

result = 2
for n in range(3, 2_000_000):
    if utils.is_prime(n):
        result += n
print(result)
