# 問題リンク：https://yukicoder.me/problems/no/16
# 提出リンク：https://yukicoder.me/submissions/915851
x,n = map(int,input().split())
a   = list(map(int,input().split()))
ans = 0
mod = 1000003

for i in range(n):
    ans += pow(x,a[i],mod)
    ans %= mod
print(ans)