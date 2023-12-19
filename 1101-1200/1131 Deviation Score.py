# Problem Link: https://yukicoder.me/problems/no/1131
# Submission  : https://yukicoder.me/submissions/939183

# input
N = int(input())
points = list(map(int,input().split()))
point_mean = sum(points)/N
ans_list = []

# Calculation
for i in range(N):
    ans_list.append(int(50 - (point_mean - points[i]) / 2))

# Output
print(*ans_list,sep='\n')