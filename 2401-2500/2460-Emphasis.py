# 問題リンク: https://yukicoder.me/problems/no/2460
# 提出リンク: https://yukicoder.me/submissions/917777

S     = input()
left  = S.find('#')
right = S.rfind('#')

ans = S[left+1:right]
print(ans)