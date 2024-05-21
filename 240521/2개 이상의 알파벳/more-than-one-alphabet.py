data = input()

def alphbet(data):
    string_list = []
    N = len(data)
    for i in range(N-1):
        if data[i] != data[i+1]:
            return "Yes"
    return "No"

print(alphbet(data))