# 출처: https://blackon29.tistory.com/63 [BlackSwon:티스토리]

def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    return new

list_2d = [['b', 'a', 0],
           ['c', 0, 0],
           [0, 0, 0]]
for i in rotate_2d(list_2d):
    print(i)