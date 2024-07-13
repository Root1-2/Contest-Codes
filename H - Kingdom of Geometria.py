#https://vjudge.net/contest/638850#problem/H

def max_2x2_squares(bases):
    results = []
    for B in bases:
        max_squares = (B * B) // 4
        results.append(max_squares)
    return results

T = int(input().strip())
bases = []
for _ in range(T):
    B = int(input().strip())
    bases.append(B)
    results = max_2x2_squares(bases)

for result in results:
    print(result)
