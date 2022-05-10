# 시각
# 0시부터 n시 59분 59초까지의 모든 시각을 구하시오

n = int(input())
c = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                c += 1
print(c)