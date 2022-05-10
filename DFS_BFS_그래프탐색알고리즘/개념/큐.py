# 큐 자료구조
# 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조
# 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화
# 왼 쪽에서 들어오고 오른 쪽에서 나감

from collections import deque as d

# 큐 구현을 위해 데크 라이브러리 사용
q = d()

# 삽입
q.append(5)
q.append(2)
q.append(3)
q.append(7)
q.popleft()
q.append(1)
q.append(4)
q.popleft()

print(q) # 먼저 들어 온 순서대로 출력
q.reverse() # 역순으로 바꾸기
print(q)