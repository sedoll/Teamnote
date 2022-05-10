# 시간이 주어졌을 때 3이 들어간 모든 시간을 구하시오

h = int(input())
m = 60
s = 60
cnt = 0
for i in range(h+1): # n시 59분 59초 까지 이므로 h+1
    for j in range(m):
        for k in range(s):
            result = str(i)+str(j)+str(k) # 시, 분, 초를 문자열로 만들어서 더함
            if '3' in result: # 문자열 안에 3이 들어 있는 지 확인
                cnt += 1 # 카운트
print(cnt) # 출력