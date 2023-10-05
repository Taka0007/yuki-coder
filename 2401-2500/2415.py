# 問題リンク: https://yukicoder.me/problems/no/2415
# 提出リンク: https://yukicoder.me/submissions/917907

A = int(input())
B = int(input())

if A%2==0 or B%2==0:
    ans = 'Even'
else:
    ans = 'Odd'
    
print(ans)