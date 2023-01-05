result = 0
for i in range(111, 1000):
    for j in range(111, 1000):
        product = i * j
        if str(product) == str(product)[::-1] and product > result:
            result = product
print(result)