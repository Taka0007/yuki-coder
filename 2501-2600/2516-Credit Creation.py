# Problem: https://yukicoder.me/problems/no/2516
# Submission: https://yukicoder.me/submissions/923098

N = int(input())
R = float(input())
ans = 0
now = 100

for i in range(N):
    ans += now
    now *= (1-R)
print(ans)