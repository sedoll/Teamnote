#상하좌우

n = int(input())
x, y = 1, 1
end_x, end_y = n, n

plans = input().split()
for i in plans:
    if i == 'L':
        if y > 1:
            y -= 1
    elif i == 'R':
        if y < n:
            y += 1
    elif i == 'U':
        if x > 1:
            x -= 1
    else:
        if x < n:
            x += 1
print(x, y)
