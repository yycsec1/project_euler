total_sum = 0
with open("./../input/13.txt") as f:
    for line in f:
        total_sum += int(line.strip())
print(str(total_sum)[:10])
