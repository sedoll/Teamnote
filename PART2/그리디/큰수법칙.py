#큰수법칙

n, m, k = map(int, input().split())
list_a = list(map(int, input().split()))
list_a.sort(reverse=True)
result = 0
for i in range(1, m+1):
    if i % k != 0:
        result += list_a[0] # 첫번째로 큰 수
    else:
        result += list_a[1] # 두번째로 큰 수
print(result)