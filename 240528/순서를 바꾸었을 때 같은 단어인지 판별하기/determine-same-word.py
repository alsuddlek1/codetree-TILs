a = list(input())
b = list(input())

a.sort()
b.sort()

if len(a) != len(b):
    print("No")
else:
    if a == b:
        print("Yes")
    else:
        print("No")