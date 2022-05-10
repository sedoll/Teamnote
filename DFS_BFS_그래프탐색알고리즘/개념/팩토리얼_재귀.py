#팩토리얼

def fn(v):
    if v <= 1:
        return 1
    return v * fn(v-1)
print(fn(5))