n, m = map(int, input().split())
A = list(map(int, input().split()))

def ex_sum(n, m, A):
    for i in range(m):
        a1, a2 = map(int, input().split())
        result = 0

        for i in range(a1-1, a2):
            result += A[i]

        print(result)

ex_sum(n,m,A)