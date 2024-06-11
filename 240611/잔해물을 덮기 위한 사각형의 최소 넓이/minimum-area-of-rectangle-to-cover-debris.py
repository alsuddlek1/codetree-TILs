A_x1, A_y1, A_x2, A_y2 = map(int, input().split())
B_x1, B_y1, B_x2, B_y2 = map(int, input().split())

data = [[0]*2001 for _ in range(2001)]

A_x1 += 1000
A_y1 += 1000
A_x2 += 1000
A_y2 += 1000

B_x1 += 1000
B_y1 += 1000
B_x2 += 1000
B_y2 += 1000

def fill_data(x1, y1, x2, y2, types):
    for i in range(x1, x2):
        for j in range(y1, y2):
            if types == "A":
                data[i][j] = 1
            else:
                data[i][j] = 0

fill_data(A_x1, A_y1, A_x2, A_y2, "A")
fill_data(B_x1, B_y1, B_x2, B_y2, "B")

i_list = []
j_list = []

for i in range(2001):
    for j in range(2001):
        if data[i][j] == 1:
            i_list.append(i)
            j_list.append(j)

# print(i_list)
# print(j_list)
result = 0
if i_list and j_list:
    result = (max(j_list) - min(j_list)+1) * (max(i_list) - min(i_list)+1)

print(result)