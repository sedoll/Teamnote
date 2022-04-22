# 어떠한 수 n이 1이 되게 만들어라
# 1. n-=1
# 2. n/=k, 근데 이건 나누어 떨어질 때만 사용 가능하다
import time
start = time.time()  # 시작 시간 저장

cnt = 0

def one(n, k):
    global cnt
    while n > 1:
        if n % k == 0:
            n/=k
        else:
            n-=1
        cnt += 1
    print(cnt)

# n, k  = map(int, input().split())
one(30, 3)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
