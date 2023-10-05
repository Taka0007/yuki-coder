# 問題リンク: https://yukicoder.me/problems/no/1883
# 提出リンク: https://yukicoder.me/submissions/917800

S = input()

a = int(S[0])
b = int(S[1])
c = int(S[2])

num = [a,b,c]
num.sort()

ans = num[2] - num[0]
print(ans)