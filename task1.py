""" 1. Напишите функцию для транспонирования матрицы """


def transpose_matrix(matrix):
    num_rows = len(matrix)
    if num_rows > 0:
        num_cols = len(matrix[0])
    else:
        num_cols = 0

    transposed_matrix = []  # Пустой список для транспонированной матрицы

    for _ in range(num_cols):
        row = [0] * num_rows  # Создаем строку с num_rows элементами, инициализированными значением 0
        transposed_matrix.append(row)

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


matrix = [[1, 2, 4], [31, 17, 15]]
print(matrix)
print(transpose_matrix(matrix))
