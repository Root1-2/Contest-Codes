#https://vjudge.net/problem/CodeChef-FLOW006

K = int(input())

result = []

for _ in range(K):
    N = input().strip()
    eachResult = sum(int(digit) for digit in N)
    result.append(eachResult)

for result in result:
    print(result)
