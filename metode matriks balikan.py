def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiplication(matrix1, matrix2):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in transpose(matrix2)] for X_row in matrix1]

def matrix_inverse(matrix):
    n = len(matrix)
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        factor = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= factor
            identity[i][j] /= factor
        for k in range(i+1, n):
            factor = matrix[k][i]
            for j in range(n):
                matrix[k][j] -= factor * matrix[i][j]
                identity[k][j] -= factor * identity[i][j]
    
    for i in range(n-1, -1, -1):
        for k in range(i-1, -1, -1):
            factor = matrix[k][i]
            for j in range(n):
                matrix[k][j] -= factor * matrix[i][j]
                identity[k][j] -= factor * identity[i][j]

    return identity

def solve_linear_equations(A, b):
    A_inv = matrix_inverse(A)
    x = matrix_multiplication(A_inv, [[elem] for elem in b])
    return [elem[0] for elem in x]

# Masukkan koefisien matriks A dan vektor b
A = [[2, 1, -1],
     [1, 1, -1],
     [-1, -1, 2]]

b = [1, 1, -2]

# Hitung solusi x
x = solve_linear_equations(A, b)

print("Solusi x dari sistem persamaan linear:")
print(x)
