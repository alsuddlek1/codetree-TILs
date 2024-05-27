N = int(input())

def fact(n):
    # result = 0
    if n == 0:
        return 0
    # result += n
    return fact(n-1) + n


print(fact(N))