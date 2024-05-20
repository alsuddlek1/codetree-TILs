a,b = map(int, input().split())

def perfect_num(a,b):
    result = 0
    for i in range(a, b+1):
        judg = 0
        if i // 2 != 0:
            judg += 1
        if i % 10 != 5:
            judg += 1
        if i % 3 == 0 and i % 9 != 0:
            judg += 1
        
        if judg == 3:
            result += 1
    return result

print(perfect_num(a,b))