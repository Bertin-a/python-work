def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for item in matrix[row]:
            print('{:d} '.format(item), end='')
        print('$', end='')
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()