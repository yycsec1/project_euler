result = 0
for i in range(1, 1000):
    if i % 3 == 0:
        result += i
        continue
    if i % 5 == 0:
        result += i
print(result)
