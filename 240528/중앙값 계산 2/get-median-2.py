n = int(input())
data = list(map(int, input().split()))

result = []
for i in range(1, n+1):
    mid_data = []
    if i % 2 != 0:
        mid_data = data[:i]
        mid_data.sort()
        result.append(mid_data[i//2])
print(*result)




# result = []
# for i in range(1, n+1):
#     mid_data = []
#     if i % 2 != 0:
#         mid_data = data[:i+1]
#         # result.append(data[:i+1][(i+1)//2])
#         mid_data.sort()
#         result.append(mid_data[(i+1)//2])
        
# print(*result)