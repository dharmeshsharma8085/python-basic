# check string is palindrome or not
str=input("Enter any word:")
str1=str[::-1]
if(str==str1):
    print("String is palindrome")
else:
    print("string is not palindrome")