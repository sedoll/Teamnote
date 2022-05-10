# a와 b라는 수가 있을 때 더이상 나머지가 없이 나누어 질때까지 나눈다.
# a> b 일때

def gcd(a, b):
    if a % b == 0: 
        return b
    else:
        return gcd(b, a%b)
print(gcd(117, 27))