data = list(map(int, input().split()))

## 6명을 3명씩 총 2팀
# 두 팀의 총합 차이 최소화

# 0. 최대값
min_int = 1000000
cnt_list = []

# 0. data의 총합
sum_data = 0
for i in range(6):
    sum_data += data[i]

com_sum = sum_data
# print(sum_data)
# data의 총 합에서 숫자 세개 빼기
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            com_sum = sum_data
            com_sum -= data[i]
            com_sum -= data[j]
            com_sum -= data[k]
            # print(com_sum)
            cnt_list.append(abs(sum_data-com_sum-com_sum))

print(min(cnt_list))

# data의 총 합에서 뺀 수와 빠진 수 비교