N = int(input())
MAX = 10*10

##
dx = [0, 0, 1, -1] # 동서남북
dy = [1, -1, 0, 0]

x, y = 0, 0
elapsed_time = 0
ans = -1

#
def move(move_dir, dist):
    global x, y
    global ans, elapsed_time
    
    for _ in range(dist):
        x, y = x + dx[move_dir], y + dy[move_dir]
        
        elapsed_time += 1

        if x == 0 and y == 0:
            ans = elapsed_time
            return True
    
    return False

##
for _ in range(N):
    c_dir, dist = tuple(input().split())
    dist = int(dist)
    
    # 각 방향에 맞는 번호를 붙여줍니다.
    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    # 주어진 방향대로 dist 만큼 위치를 이동해봅니다.
    done = move(move_dir, dist)

    # 시작 위치에 도달했다면, 종료합니다.
    if done:
        break

print(ans)