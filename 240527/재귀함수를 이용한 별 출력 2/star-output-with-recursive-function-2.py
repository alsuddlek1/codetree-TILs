N = int(input())

def start(n):
    if n == 0:
        return

    print("* " * n)
    start(n-1)
    print("* " * n)

start(N)