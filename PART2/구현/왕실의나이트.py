#왕실의 나이트
# a = 97~ h=104
# 97 1 / 104 8 의 범위의 크기
# 두칸 이동 / 한칸 이동
# ++ +- -+ -- 
# 21 21 21 21
# 12 12 12 12

# 이따구로 짜면 안됨
# a, b = map(str, input())
# j, k = 2, 1
# if 104 >= ord(a) + 2 >= 97 and 8 >= int(b) + 1 >= 1:
#     c += 1
# if 104 >= ord(a) + 1 >= 97 and 8 >= int(b) + 2 >= 1:
#     c += 1
# if 104 >= ord(a) + 2 >= 97 and 8 >= int(b) - 1 >= 1:
#     c += 1
# if 104 >= ord(a) + 1 >= 97 and 8 >= int(b) - 2 >= 1:
#     c += 1
# if 104 >= ord(a) - 2 >= 97 and 8 >= int(b) + 1 >= 1:
#     c += 1
# if 104 >= ord(a) - 1 >= 97 and 8 >= int(b) + 2 >= 1:
#     c += 1
# if 104 >= ord(a) - 2 >= 97 and 8 >= int(b) - 1 >= 1:
#     c += 1
# if 104 >= ord(a) - 1 >= 97 and 8 >= int(b) - 2 >= 1:
#     c += 1
# print(c)

# 책
# 현재 나이트의 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1, -2), (1, -2), (2, -1)
         , (1, 2), (1, 2), (-1, 2), (-2, -1)]

result = 0
for step in steps:
    r = row + step[0]
    c = column + step[1]
    if 8 >= r >= 1 and 8>= c >= 1:
        result += 1
print(result)