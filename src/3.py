import utils


num = 600851475143
result = 0
while num > 1:
    factor = utils.find_first_factor(num)
    num //= factor
    if utils.is_prime(factor) and factor > result:
        result = factor
print(result)
