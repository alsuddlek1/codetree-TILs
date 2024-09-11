N = int(input())
data = input()

res = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if data[i] == "C" and data[j] == "O" and data[k] == "W":
                res += 1
print(res)