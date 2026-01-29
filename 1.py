import re
def palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
    return s == s[::-1]

s =  input()
print(palindrome(s))