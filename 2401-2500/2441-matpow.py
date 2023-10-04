# 問題リンク: https://yukicoder.me/problems/no/2441
# 提出リンク: https://yukicoder.me/submissions/917766

import numpy as np

def dot(A1, A2, N):
    # N: 行列のサイズ
    A = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                A[i][j] = (A[i][j] + (A1[i][k] * A2[k][j]))
    return A

def pow_mat(A, K, N):
    # A: 累乗する行列, k: 累乗数, n: 行列Aのサイズ
    P = np.eye(N, dtype=int)
    while K:
        if K & 1:
            P = dot(P, A, N)
        A = dot(A, A, N)
        K >>= 1
    return P
    
a,b = map(int,input().split())
c,d = map(int,input().split())

mat = np.array([[a, b], [c, d]], dtype=int)
ans_matrix = pow_mat(mat, 3, 2)

for row in ans_matrix:
    print(" ".join(map(str, row)))