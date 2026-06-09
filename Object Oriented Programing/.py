# lst=[1,2,3,4,56]
# lst1=lst.reverse()
# if lst==lst1:
#     print("It is a palindrome")
# else:
#     print("Not palindrome")
n=1234
num=n
result=0
while num>0:
    l_d=num%10
    result=(result*10) + l_d
    num/=10
    
if n==result:
    print(" number is palindorme",n)
else:
    print("Number is not palindrome",n)