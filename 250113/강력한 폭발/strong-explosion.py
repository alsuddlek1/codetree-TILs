n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 0. grid 내 폭탄 파악
def boom_count():
    boom_cnt = 0
    boom_location = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                boom_cnt += 1
                boom_location.append((i,j))
    return boom_cnt, boom_location

m, boom_location = boom_count() # m : grid 내 폭탄의 개수, boom_location : 폭탄 위치
booms = []

# 3. 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 2. 백트래킹에 맞추어 grid 내 폭탄에 1,2,3 대입 -> 폭탄 개수 확인
def explosion(booms):
    data_boom_cnt = 0
    data = [[0 for _ in range(n)] for _ in range(n)]
    # 2-1. data[boom_location] 에 booms[i] 대입
    for i in range(len(booms)):
        x = boom_location[i][0]
        data[boom_location[i][0]][boom_location[i][1]] = booms[i]

    # 2-2. 대입한 후 1,2,3 에 맞추어 boom_grid 생성
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                for k in range(1, 3):
                    if in_range(i+k, j) and data[i+k][j] == 0:
                        data[i+k][j] = -1
                    if in_range(i-k, j) and data[i-k][j] == 0:
                        data[i-k][j] = -1
            elif data[i][j] == 2:
                dxs = [-1, 1, 0, 0]
                dys = [0, 0, -1, 1]
                for dx, dy in zip(dxs, dys):
                    nx = i + dx
                    ny = j + dy
                    if in_range(nx, ny) and data[nx][ny] == 0:
                        data[nx][ny] = -1
            elif data[i][j] == 3:
                dxs = [-1, -1, 1, 1]
                dys = [-1, 1, -1, 1]
                for dx, dy in zip(dxs, dys):
                    nx = i + dx
                    ny = j + dy
                    if in_range(nx, ny) and data[nx][ny] == 0:
                        data[nx][ny] = -1
    
    # 2-3. boom_grid에서 -1(폭발 했을 때) 개수 출력
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                data_boom_cnt += 1
    
    return data_boom_cnt
    



# 1. grid 내 폭탄 개수(m)자리 수에 따른 순열 백트래킹

def back(curr_num):
    global result
    
    if curr_num == m+1:
        ## 초토화 함수 호출 : booms 리스트 전송
        result = max(explosion(booms), result)
        return

    for i in range(1, 4):
        booms.append(i)
        back(curr_num+1)
        booms.pop()

    return

back(1)


print(result)