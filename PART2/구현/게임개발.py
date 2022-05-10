#게임 개발

#맵 생성 값
x, y = map(int, input().split())

# #시작 좌표 + 방향 0 북, 1 동, 2 남, 3 서
# px, py = map(int, input().split())

d = [[0]*y for _ in range(x)]
print(list(d))