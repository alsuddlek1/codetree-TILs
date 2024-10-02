## push_back
## pop_back
## size : 출력
## get k : 출력

N = int(input())
data = [0]

for i in range(N):
    input_value = input().split()
    if input_value[0] == "size":
        print(len(data)-1)
    elif input_value[0] == "pop_back":
        data.pop()
    elif input_value[0] == "push_back":
        k = int(input_value[1])
        data.append(k)
        # print(data)
    elif input_value[0] == "get":
        k = int(input_value[1])
        print(data[k])