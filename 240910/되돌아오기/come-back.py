N = int(input())

dx = [0,0,1,-1] # 동서남붑
dy = [1,-1,0,0]
x,y = 0,0
cnt = 0
answer = -1

def move(dir_num, count):
    global x,y
    global cnt, answer

    for i in range(count):
        x,y = x+dx[dir_num], y+dy[dir_num]
        cnt += 1

        if x == 0 and y == 0:
            answer = cnt
            return True
    return False

for i in range(N):
    d, c = input().split()
    c = int(c)

    if d == "E":
        dir_num = 0
    elif d == "W":
        dir_num = 1
    elif d == "S":
        dir_num = 2
    else:
        dir_num = 3

    done = move(dir_num, c)

    if done:
        break

print(answer)