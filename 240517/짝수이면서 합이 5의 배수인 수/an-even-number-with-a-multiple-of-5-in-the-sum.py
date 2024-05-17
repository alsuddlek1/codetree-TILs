N = int(input())

def is_masic_num(n):
    if n % 2 == 0 :
        cnt = (n // 10) + (n % 10)
        if cnt % 5 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

print(is_masic_num(N))