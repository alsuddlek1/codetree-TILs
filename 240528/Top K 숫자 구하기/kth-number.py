N, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
# print(data)
print(data[K-1])