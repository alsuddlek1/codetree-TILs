N, M = map(int, input().split())

def measure(cnt):
    measures = []
    for i in range(1, cnt+1):
        if cnt % i == 0:
            measures.append(i)
    return measures

def LCM(n, m):
    measure_list = []
    result = 1
    for i in range(len(measure(n))):
        for j in range(len(measure(m))):
            if measure(n)[i] == measure(m)[j]:
                measure_list.append(measure(n)[i])
    for i in range(len(measure_list)):
        result = result * measure_list[i]
    print(result)

LCM(N, M)