import utils


num = 600851475143
result = 0
while num > 1:
    factor = utils.find_first_factor(num)
    num //= factor
    result = max(result, factor)
print(result)
