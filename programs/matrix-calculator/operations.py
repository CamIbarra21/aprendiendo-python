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
        #  columnas de la matriz A = filas de la matriz B
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

def determinant(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    if rows != columns:
        return 'ERROR'

    if rows < 2:
        return 0
    
    if rows == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    
    factor = 1
    result = 0 

    for j in range(columns):
        coefficient = matrix[0][j]

        newMatrix = []
        for i in range(rows - 1):
            newMatrix.append([0] * (columns - 1))
        #print(newMatrix)

        rowNM = 0
        for i in range(1, rows):
            columNM = 0
            for k in range(columns):
                if k != j:
                    #print(f'R:{rowNM}   C:{columNM}')
                    newMatrix[rowNM][columNM] = matrix[i][k]
                    columNM += 1
            rowNM += 1

        result += (factor * coefficient * determinant(newMatrix))
        factor *= -1
            
    return result

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    newMatrix = []
    for i in range(columns):
        newMatrix.append([0] * rows)

    for i in range(rows):
        for j in range(columns):
            newMatrix[j][i] = matrix[i][j]
    
    return newMatrix

def inverse(matrix): #Todavia en proceso
    rows = len(matrix)
    columns = len(matrix[0])

    newMatrix = []
    for i in range(rows):
        newMatrix.append([0] * columns)
    
