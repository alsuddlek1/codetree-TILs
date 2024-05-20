n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def sequnence(n1, n2, A, B):
    for i in range(n1-n2+1):
        # print(A[i:i+n2])
        if A[i:i+n2] == B:
            return "Yes"
    return "No"

print(sequnence(n1, n2, A, B))