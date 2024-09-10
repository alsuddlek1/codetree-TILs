data = input()

x,y = 0,0 # 시작
dx = [0, 1, 0, -1] # 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dir_num = 0 # 북쪽을 향한 상태에서 시작
answer = 0

for i in data:
    if i == "F":
        x, y = x + dx[dir_num], y + dy[dir_num]
        if x == 0 and y == 0:
            break
        
    elif i == "R":
        dir_num += 1
        if dir_num == 4:
            dir_num = 0
    elif i == 'L':
        dir_num -= 1
        if dir_num == -1:
            dir_num = 3
    answer += 1

print(answer+1)