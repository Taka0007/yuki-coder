# 参考サイト:https://gist.github.com/edy555/5d950665e8b5f12f89bbf22ebf534043
# 問題URL:https://yukicoder.me/problems/no/1235

import numpy as np

LOWER_THRESHOLD=1.0e-6
UPPER_BOUND=1.0e+4
INFTY=400
def zeta_r(s):
    if s == 1:
        return np.NaN
    a = [0.5/(1-2**(1-s))]
    b = [a[0]]
    for n in range(1,INFTY):
        for k in range(n):
            a[k] = 0.5*a[k]*n/(n-k)
        a.append(-(float(n)/(n+1))**s * a[-1] / n)
        b.append(sum(a))
        if abs(b[-1]) < LOWER_THRESHOLD:
             break
        if abs(b[-1]) > UPPER_BOUND:
             break            
    return sum(b)
    
N = int(input())
print(zeta_r(N))
