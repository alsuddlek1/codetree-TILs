N, M = map(int, input().split())

def GCD(n, m):
    result = 100
    sm_c = min(n,m)
    la_c = max(n, m)
    for i in range(sm_c, 0, -1):
        if sm_c % i == 0 and la_c % i == 0:
            if i <= result:
                result = i
                break
    print(result)

GCD(N, M)