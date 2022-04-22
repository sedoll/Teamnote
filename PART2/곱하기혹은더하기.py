#숫자0~9로만 이루어진 문자열 s가 주어졌을 때
#왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
#숫자 사이에 x 혹은 + 연산자를 넣어
#만들어질 수 있는 가장 큰 수를 구하는 프로그램
#단 연산은 왼쪽에서 오른쪽으로 순서대로 진행
import time
start = time.time()  # 시작 시간 저장

# 내가 쓴 코드
# s = input()
# s = "02984"
# result = int(s[0])
# for i in range(1, len(s)):
#     if s[i] == "0" or s[i] == "1":
#         result += int(s[i])
#     else:
#         if s[i-1] == "0":
#             result += int(s[i])
#         else:
#             result *= int(s[i])
# print(result)
# print("time : {:.15f}".format(time.time() - start))

# 책
s = "02984"
result = int(s[0])
for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)