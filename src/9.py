maximum = 1000
break_a, break_b = False, False
for a in range(1, maximum - 1):
    for b in range(a + 1, maximum - a + 1):
        for c in range(b + 1, maximum - a - b + 1):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print(a * b * c)
                break_a, break_b = True, True
                break
        if break_b:
            break
    if break_a:
        break
