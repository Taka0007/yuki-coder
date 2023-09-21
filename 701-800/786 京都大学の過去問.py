# 問題リンク：https://yukicoder.me/problems/no/786

N   = int(input())
ans = [0]*(N+1)
ans[0] = 1
ans[1] = 2

for i in range(2,N):
	ans[i] = ans[i-1]+ans[i-2]
	
print(ans[N-1])
