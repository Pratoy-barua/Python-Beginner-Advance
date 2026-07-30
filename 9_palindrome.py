list = [1, "abc", "abc", 1]
rev = list.copy() #list copy korlam, jate original list ta change na hoy
rev.reverse()
if list == rev:
    print("Palindrome")
else:
    print("Not Palindrome")