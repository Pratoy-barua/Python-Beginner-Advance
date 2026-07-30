list = [1, "abc", "abc", 1]
rev = list[::-1]
if list == rev:
    print("Palindrome")
else:
    print("Not Palindrome")