# ProbLink : https://yukicoder.me/problems/no/2400
A,B = map(int,input().split())
C,D = map(int,input().split())

N = A*C - B*D
M = A*D + B*C

print(N,M,sep=" ")
