data = input()

def palindrome(data):
    reversed_data = data[::-1]
    if data == reversed_data:
        return "Yes"
    else:
        return "No"

print(palindrome(data))