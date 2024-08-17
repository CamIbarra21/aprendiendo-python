def printMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            if j == 0:
                print(f'[\t{matrix[i][j]}', end="\t")
            elif j < columns - 1:
                print(matrix[i][j], end="\t")
            else:
                print(matrix[i][j], end="\t]\n")
