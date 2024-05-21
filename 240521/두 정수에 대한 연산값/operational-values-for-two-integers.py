c1, c2 = map(int, input().split())

def inte(c1, c2):
    large = max(c1, c2) + 25
    small = min(c1, c2) * 2
    print(small, large)

inte(c1, c2)