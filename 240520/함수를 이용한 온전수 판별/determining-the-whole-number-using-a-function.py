a,b = map(int, input().split())

def perfect_num(i):
    if i % 2 == 0:
        return False
    if i % 10 == 5:
        return False
    if i % 3 == 0 and i % 9 != 0:
        return False
    return True

result = 0
for i in range(a, b+1):
    # print(perfect_num(i), i)
    if perfect_num(i):
        result += 1

print(result)



# def perfect_num(a,b):
#     result = 0
#     for i in range(a, b+1):
#         judg = 0
#         if i // 2 == 0:
#             return False
#         if i % 10 == 5:
#             return False
#         if i % 3 != 0 and i % 9 == 0:
#             return False
        
#         result += 1
#     return result

# print(perfect_num(a,b))