def is_palindrome(str):
    str = str.lower().replace(" ","")
    return str==str[::-1]

check  = is_palindrome(str(input("Enter a String to check : ")))
if check ==True:
    print("Enter String a palindrome String")
else:
    print("Enter String is not a palindrome String")