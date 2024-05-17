N = int(input())

def total_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    total = total // 10
    return total

print(total_sum(N))