#https://vjudge.net/contest/638850#problem/A

N, M = map(int, input().split())

reachable = set()
reachable.add(1)

paths = []
for i in range(M):
    u, v = map(int, input().split())
    paths.append((u, v))

for u, v in paths:
    if u in reachable:
        reachable.add(v)
    elif v in reachable:
        reachable.add(u)

not_accessible = []
for attraction in range(2, N + 1):
    if attraction not in reachable:
        not_accessible.append(attraction)

if not_accessible:
    print(" ".join(map(str, not_accessible)))
else:
    print("Connected")
