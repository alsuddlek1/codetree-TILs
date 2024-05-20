M, D = map(int, input().split())

def day(M, D):
    month = 12
    if M <= 12:
        day = 31
        if M == 2:
            day = 28
        if M <= 6 and M % 2 == 0 and M != 2:
            day = 30
        if M > 6 and M % 2 == 1:
            day = 30
        if D <= day:
            return "Yes"
    return "No"

print(day(M, D))