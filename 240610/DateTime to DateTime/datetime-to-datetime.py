# 11일 11시 11분 -> a일 b시 c분
day, hour, minute = 11, 11, 11
a, b, c = map(int, input().split())


if a <= day and b <= hour and c < minute:
    print(-1)

else:
    result = 0
    while True:
        if day == a and hour == b and minute == c:
            break

        result += 1
        minute += 1
        

        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0
                day += 1

    print(result)