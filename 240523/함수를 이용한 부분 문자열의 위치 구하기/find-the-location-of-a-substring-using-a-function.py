_list = input()
part = input()

def in_arr(_list, part):
    N = len(_list)
    M = len(part)
    
    for i in range(N-M+1):
        cnt = M
        result = -1
        for j in range(M):
            if _list[i+j] == part[j]:
                cnt -= 1
        if cnt == 0:
            result = i
            break
    return result

print(in_arr(_list, part))