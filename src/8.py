import math

window = 13
result = 0
n = ''.join([line.strip() for line in open("./../input/8.txt")])
for i in range(0, len(n)-window+1):
    p = math.prod(map(int, n[i:i+window]))
    result = max(result, p)
print(result)
