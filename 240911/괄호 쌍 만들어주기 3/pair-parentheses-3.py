data = input()
res = 0

for i in range(len(data)):
    if data[i] == "(":
        for j in range(i+1, len(data)):
            if data[j] == ")":
                res += 1

print(res)