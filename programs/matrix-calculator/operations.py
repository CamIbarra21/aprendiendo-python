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
                result = matrixA[i][j] + matrixB[i][j]
                newMatrix[i][j] = result

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
                result = matrixA[i][j] - matrixB[i][j]
                newMatrix[i][j] = result

    else:
        newMatrix = [[0]]

    return newMatrix

def multiplication(matrixA, matrixB):
    newMatrix = []

    if len(matrixA[0]) == len(matrixB):
        #  las filas son iguales     y      las columnas son iguales
        factor = len(matrixA[0])
        rows = len(matrixA)
        columns = len(matrixB[0])

        #print(f'Filas = {rows}\nColumnas: {columns}')

        for i in range(rows):
            newMatrix.append([0] * columns)

        for i in range(rows):
            for j in range(columns):
                result = 0
                for k in range(factor):
                    result += (matrixA[i][k] * matrixB[k][j])
                newMatrix[i][j] = result

    else:
        newMatrix = [[0]]

    return newMatrix