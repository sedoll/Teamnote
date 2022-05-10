#스택 구현 예제
# 스택은 위에서 아래로 쌓는 형식이다
# 그리고 push pop 은 맨 위에서 하기에
# 맨 나중에 들어온게 나간다.

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 7 제거
stack.append(1)
stack.append(4)
stack.pop() # 4 제거

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력