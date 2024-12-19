def shift(arr):
    temp = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    
    return arr

# Run-Length Encoding -> 길이 구하기
def get_run_length_encoding(arr):
    length = 0
    run_len = []
    cnt = 1
    alpahbet = 1

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt += 1
            if cnt == 10:
                length += 1
        else:
            run_len.append(cnt)
            cnt = 1
            alpahbet += 1
    run_len.append(cnt)

    length += len(run_len) + alpahbet

    return length

# 변수 선언
arr = input()
arr_list = []
for i in arr:
    arr_list.append(i)

answer = 100
for i in range(len(arr)):
    encoding_len = get_run_length_encoding(arr_list)
    arr_list = shift(arr_list)
    answer = min(answer, encoding_len)

print(answer)