## a~b 사이에 3,6,9
## 숫자가 3의 배수

c1, c2 = map(int, input().split())

def count_num(c1, c2):
    in_cnt = []
    for i in range(c1, c2+1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 or i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
            in_cnt.append(i)
        elif i % 3 == 0:
            in_cnt.append(i)
    return in_cnt

print(len(count_num(c1, c2)))

# def three_multiple(c1, c2):
#     multi_cnt = []
#     for i in range(c1, c2+1):
#         if i % 3 == 0:
#             multi_cnt.append(i)
#     return multi_cnt


# cnt_list = []
# for i in count_num(c1, c2):
#     cnt_list.append(i)
#     for j in three_multiple(c1, c2):
#         cnt_list.append(j)

# result = set(cnt_list)
# print(len(result))