#https://vjudge.net/problem/CodeForces-1324D

import bisect
n = int(input())
if not (2 <= n <= 200000):
    sys.exit()
A = list(map(int, input().split()))
if len(A) != n or any(not (1 <= x <= 1000000000) for x in A):
    sys.exit()
B = list(map(int, input().split()))
if len(B) != n or any(not (1 <= x <= 1000000000) for x in B):
    sys.exit()

D = [A[i] - B[i] for i in range(n)]

D.sort()

count = 0
j = n - 1

for i in range(n):
    if D[i] > 0:
        count += n - i - 1
    else:
        j = bisect.bisect_right(D, -D[i], i + 1)
        count += n - j

print(count)
