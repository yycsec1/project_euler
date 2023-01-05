i = 1
j = 2
result = 2
while i + j < 4_000_000:
    i, j = j, i + j
    if j % 2 == 0:
        result += j
print(result)
