# 問題リンク：https://yukicoder.me/problems/no/275
# 提出リンク：https://yukicoder.me/submissions/917706

N = int(input())
A = list(map(int,input().split()))
A.sort()

if N%2!=0:
    ans = A[N//2]
else:
    ans = (A[(N//2)-1] + A[N//2])/2
print(ans)