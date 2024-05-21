c1, c2 = map(int, input().split())

def inte(c1, c2):
    if c1 > c2:
        c1 = c1 + 25
    else:
        c1 =  c1 * 2
    return c1

print(inte(c1, c2), inte(c2, c1))