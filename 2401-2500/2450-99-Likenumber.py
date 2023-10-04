# 問題リンク: https://yukicoder.me/problems/no/2450
# 提出リンク: https://yukicoder.me/submissions/917757

N = int(input())
check_str = '9' * len(str(N))

if check_str == str(N):
    ans = 'Yes'
else:
    ans = 'No'
print(ans)