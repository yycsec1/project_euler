import utils

count = 10001
result = 1
while count > 0:
    result += 1
    if utils.is_prime(result):
        count -= 1

print(result)
