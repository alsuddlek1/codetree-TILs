def print_str(n):
    if n == 0:
        return

    print_str(n-1)
    print("HelloWorld")

N = int(input())
print_str(N)