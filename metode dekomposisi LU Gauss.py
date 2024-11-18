def lu_decomposition(A):
    """
    Menghitung dekomposisi LU untuk matriks A.
    Asumsi: A adalah matriks persegi dan memiliki dekomposisi LU yang unik.
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    # Inisialisasi matriks L dengan diagonal 1
    for i in range(n):
        L[i][i] = 1.0

    # Proses dekomposisi
    for k in range(n):
        U[k][k] = A[k][k]
        for j in range(k + 1, n):
            L[j][k] = A[j][k] / U[k][k]
            U[k][j] = A[k][j]
            for i in range(k + 1, n):
                A[i][j] -= L[i][k] * U[k][j]

    return L, U

def solve_lu(L, U, b):
    """
    Menyelesaikan SPL Ax = b menggunakan dekomposisi LU.
    """
    n = len(L)
    y = [0.0] * n
    x = [0.0] * n

    # Forward substitution (Ly = b)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    # Backward substitution (Ux = y)
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

# Contoh penggunaan
A = [[2, -1, 0],
     [-1, 2, -1],
     [0, -1, 2]]
b = [1, 2, 3]

L, U = lu_decomposition(A)
x = solve_lu(L, U, b)

print("Matriks L:")
for row in L:
    print(row)

print("\nMatriks U:")
for row in U:
    print(row)

print("\nSolusi SPL:")
print("x =", x)
