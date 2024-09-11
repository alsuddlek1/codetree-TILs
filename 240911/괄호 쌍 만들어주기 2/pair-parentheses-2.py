arr = input()
n = len(arr)

res = 0
for i in range(n-1):
    if arr[i] == "(" and arr[i+1] == "(":
        for j in range(i+2, n-1):
            if arr[j] == ")" and arr[j+1] == ")":
                res += 1
print(res)