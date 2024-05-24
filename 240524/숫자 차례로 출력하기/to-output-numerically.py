def print_num(n):
    result = []
    for i in range(1, n+1):
        result.append(i)
    # print(result)
    for j in result:
        print(j, end= " ")
    print()

def print_num_revers(n):
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    print_num(n)

    for j in result:
        print(j, end=" ")

N = int(input())

print_num_revers(N)