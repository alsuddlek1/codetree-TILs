def num_square(n):
    data = [[0]*n for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(n):
           data[i][j] += cnt
           cnt += 1
           if cnt == 10:
            cnt = 1
    for i in data:        
        for j in i:    
            print(j, end=' ')
        print()

N = int(input())

num_square(N)