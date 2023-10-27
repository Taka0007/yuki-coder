# Problem: https://yukicoder.me/problems/no/2515
# Submission: https://yukicoder.me/submissions/923035

X_1,Y_1,X_2,Y_2,X_3 = map(int,input().split())

if Y_1==Y_2:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)