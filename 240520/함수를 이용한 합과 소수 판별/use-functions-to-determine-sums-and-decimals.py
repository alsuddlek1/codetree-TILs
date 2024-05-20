a, b = map(int, input().split())

def prime(c):
    for i in range(2, c):
        if c % i == 0:
            return False
    return True

def even(c):
    cnt = c // 10 + c % 10
    if cnt % 2 == 0:
        return True

result = 0
for i in range(a, b+1):
    if prime(i) and even(i):
        result += 1

print(result)