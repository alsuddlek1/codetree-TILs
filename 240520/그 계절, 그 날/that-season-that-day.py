Y, M, D = map(int, input().split())

def season_date(Y, M, D):
    if M >= 3 and M <= 5:
        if M % 2 == 0:
            if D >= 1 and D <= 30:
                print("Spring")
            else:
                print(-1)
        else:
            if D >= 1 and D <= 31:
                print("Spring")
            else:
                print(-1)
    elif M >= 6 and M <= 8:
        if M == 6:
            if D >= 1 and D <= 30:
                print("Summer")
            else:
                print(-1)
        else:
            if D >= 1 and D <= 31:
                print("Summer")
            else:
                print(-1)
    elif M >= 9 and M <= 11:
        if M == 10:
            if D >= 1 and D <= 31:
                print("Fall")
            else:
                print(-1)
        else:
            if D >= 1 and D <= 30:
                print("Fall")
            else:
                print(-1)
    elif M == 12:
        if D >= 1 and D <= 31:
            print("Winter")
        else:
            print(-1)
    elif M == 1:
        if D >= 1 and D <= 31:
            print("Winter")
        else:
            print(-1)
    elif M == 2:
        if ((Y % 4 == 0) and (Y % 100 != 0)) or (Y % 400 == 0):
            if D >= 1 and D <= 29:
                print("Winter")
            else:
                print(-1)
        else:
            if D >= 1 and D <= 28:
                print("Winter")
            else:
                print(-1)
    else:
        print(-1)

season_date(Y, M, D)