#https://vjudge.net/problem/AtCoder-abc210_b

import sys

N = input().strip()
S = input().strip()

if len(S) != int(N):
    sys.exit()

for char in S:
    if char != '0' and char != '1':
        sys.exit()

bad = S.find('1')
if bad % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")
