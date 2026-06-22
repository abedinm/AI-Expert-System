def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:                  # rule: cols of A must equal rows of B
        raise ValueError(f"Cannot multiply {rows_A}x{cols_A} by {rows_B}x{cols_B}")

    result = [[0] * cols_B for _ in range(rows_A)]   # zero matrix: rows_A x cols_B

    for i in range(rows_A):          # each row of A
        for j in range(cols_B):      # each column of B
            for k in range(cols_A):  # shared dimension (dot product)
                result[i][j] += A[i][k] * B[k][j]
    return result


def print_matrix(M):
    for row in M:
        print(row)


if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6]]
    B = [[7, 8],
         [9, 10],
         [11, 12]]

    print("Matrix A:")
    print_matrix(A)
    print("Matrix B:")
    print_matrix(B)
    print("A x B:")
    print_matrix(multiply_matrices(A, B))
