# 5월 4일(월) -> 5월 3일(일)
m1, d1, m2, d2 = map(int, input().split())

days = [0, 'Sun', "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 2

# 1이 2보다 이후
if m1 > m2 or (m1 == m2 and d1 > d2):

    while True:
        if m1 == m2 and d1 == d2:
            break

        d1 -= 1
        day -= 1

        if day == 0:
            day = 7
        
        if d1 == 0:
            m1 -= 1
            d1 = months[m1]

# 1이 2보다 이전
else:
    while True:
        if m1 == m2 and d1 == d2:
            break

        d1 += 1
        day += 1

        if day == 7:
            day = 1
        
        if d1 == months[m1]:
            m1 += 1
            d1 = 0

print(days[day])