def dekomposisi_crout(A, b):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    # Faktorisasi matriks A menjadi L dan U
    for i in range(n):
        L[i][i] = 1.0
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    # Forward substitution
    t = [0.0] * n
    for i in range(n):
        t[i] = b[i] - sum(L[i][j] * t[j] for j in range(i))

    # Backward substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (t[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return x

# Contoh penggunaan
A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
b = [1, 0, 1]
solusi = dekomposisi_crout(A, b)
print("Solusi SPL:")
for i, x_i in enumerate(solusi):
    print(f"x_{i+1} =", x_i)
