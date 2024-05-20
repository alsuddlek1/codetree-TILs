## y // 100 == 0 and y // 400 != 0 => 평년
## y // 4 == 0 => 윤년
## 윤년 : true 평년 : false

y = int(input())

def year(y):
    if y % 100 == 0 and y % 400 != 0:
        return "false"
    if y % 4 == 0:
        return "true"
    else:
        return "false"

print(year(y))