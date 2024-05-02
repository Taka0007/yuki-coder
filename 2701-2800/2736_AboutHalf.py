# Prob link : https://yukicoder.me/problems/no/2736
# Sub link : https://yukicoder.me/submissions/978510

# input
A,B = map(int,input().split())
# output
if A <= 2*B and B <= 2*A:
    print('Yes')
else:
    print('No')