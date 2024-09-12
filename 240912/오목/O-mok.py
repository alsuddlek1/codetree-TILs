matrix = list(list(map(int, input().split())) for _ in range(19))

dx = [0, 1, 1, 1]
dy = [1, 0, -1, 1]

def winner(matrix):
    for i in range(19):
        for j in range(19):
            if matrix[i][j] != 0:
                focus = matrix[i][j]

                for dir_num in range(4):
                    points = []
                    cnt = 1
                    nx, ny = i + dx[dir_num], j + dy[dir_num]
                    while 0 <= nx < 19 and 0 <= ny < 19 and matrix[nx][ny] == focus:
                        cnt += 1
                        points.append((nx, ny))
                        if cnt == 5:
                            print(focus)
                            print(points[1][0]+1, points[1][1]+1)
                            return
                        nx += dx[dir_num]
                        ny += dy[dir_num]
    print(0)
    return

winner(matrix)