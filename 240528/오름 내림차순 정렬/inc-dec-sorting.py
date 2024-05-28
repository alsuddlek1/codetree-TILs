N = int(input())
data = list(map(int, input().split()))

data.sort()
print(*data)

reverse_data = data
reverse_data.sort(reverse=True)
print(*reverse_data)