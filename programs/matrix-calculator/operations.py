def addition(matrixA, matrixB):
    newMatrix = []

    if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        #  las filas son iguales     y      las columnas son iguales
        rows = len(matrixA)
        columns = len(matrixA[0])

        for i in range(rows):
            newMatrix.append([0] * columns)

        for i in range(rows):
            for j in range(columns):
                suma = matrixA[i][j] + matrixB[i][j]
                newMatrix[i][j] = suma

    else:
        newMatrix = [[0]]

    return newMatrix

def subtraction(matrixA, matrixB):
    newMatrix = []

    if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        #  las filas son iguales     y      las columnas son iguales
        rows = len(matrixA)
        columns = len(matrixA[0])

        for i in range(rows):
            newMatrix.append([0] * columns)

        for i in range(rows):
            for j in range(columns):
                suma = matrixA[i][j] + matrixB[i][j]
                newMatrix[i][j] = suma

    else:
        newMatrix = [[0]]

    return newMatrix