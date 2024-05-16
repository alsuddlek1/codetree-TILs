N, M = map(int, input().split())

def GCD(n, m):
    result = 100
    sm_c = min(n,m)
    for i in range(sm_c, 0, -1):
        if n % i == 0 and m % i == 0:
            # if i <= result:
            #     result = i
            #     break
            print(i)
            break

GCD(N, M)