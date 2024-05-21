a, b= map(int, input().split())

def inte(c1, c2):
    if c1 > c2:
        c1 = c1 * 2
    else:
        c1 = c1 + 10
    return c1

print(inte(a, b), inte(b,a))