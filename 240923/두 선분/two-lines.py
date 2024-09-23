x1, x2, x3, x4 = map(int, input().split())
data = [0]*101
for i in range(x1, x2+1):
    data[i] = 1

result = 0

for j in range(x3, x4+1):
    if data[j] == 1:
        result += 1
        break
    
    
if result == 0:
    print("nonintersecting")
else:
    print("intersecting")