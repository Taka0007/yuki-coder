# Prob link: https://yukicoder.me/problems/no/1622
# Submission link: https://yukicoder.me/submissions/922163

# 半径rの円に内接する三角形の面積の最大値を求める関数
def quadrature(r):
    ans = 3*( (3)**0.5 )*(r**2) / 4
    return ans

t = int(input())
for _ in range(t):
    r = int(input())
    print(quadrature(r))