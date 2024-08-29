N = int(input())

dy = [1, -1, 0, 0] # 동,서,남,북
dx = [0, 0, -1, 1] # E, W, S, N

x, y = 0, 0 # 초기값

for i in range(N):
    v, d = input().split()
    d = int(d)
    # dir = 0
    if v == "E":
        v = 0
    elif v == "W":
        v = 1
    elif v == "S":
        v = 2
    elif v == "N":
        v = 3
    
    x, y = x+(dx[v]*d), y+(dy[v]*d)

print(y, x)