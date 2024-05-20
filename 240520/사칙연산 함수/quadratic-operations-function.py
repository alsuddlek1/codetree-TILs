a,o,c = input().split()
a = int(a)
c = int(c)

def o_judg(o):
    if o == "/":
        return int(a / c)
    if o == '*':
        return a * c
    if o == '+':
        return a + c
    if o == '-':
        return a - c
    else:
        return False

if o_judg(o):
    print(f'{a} {o} {c} = {o_judg(o)}')
else:
    print("False")