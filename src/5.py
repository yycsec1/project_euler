n = 0
not_found = True
while not_found:
    n += 20
    for i in range(2, 21):
        if n % i != 0:
            not_found = True
            break
        not_found = False
print(n)
