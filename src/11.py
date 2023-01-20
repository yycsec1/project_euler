result = 0
input_matrix = []
with open("./../input/11.txt") as f:
    for line in f:
        line = line.strip()
        input_matrix.append(list(map(int, line.split(' '))))

# check down
for x in range(0, len(input_matrix[0])):
    for y in range(0, len(input_matrix) - 4):
        result = max(result,
                     input_matrix[y][x] *
                     input_matrix[y + 1][x] *
                     input_matrix[y + 2][x] *
                     input_matrix[y + 3][x])


for x in range(0, len(input_matrix[0]) - 4):
    # check side
    for y in range(0, len(input_matrix)):
        result = max(result,
                     input_matrix[y][x] *
                     input_matrix[y][x + 1] *
                     input_matrix[y][x + 2] *
                     input_matrix[y][x + 3])

    # check diagonal
    for y in range(0, len(input_matrix) - 4):
        result = max(result,
                     input_matrix[y][x] *
                     input_matrix[y + 1][x + 1] *
                     input_matrix[y + 2][x + 2] *
                     input_matrix[y + 3][x + 3])

    # check reverse diagonal
    for y in range(3, len(input_matrix)):
        result = max(result,
                     input_matrix[y][x] *
                     input_matrix[y - 1][x + 1] *
                     input_matrix[y - 2][x + 2] *
                     input_matrix[y - 3][x + 3])
print(result)
