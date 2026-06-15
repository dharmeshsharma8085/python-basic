def add(n1,n2):
    return n1+n2

print(add(5,6))

number1=10
number2=input("enter second number") # remember this is a string
try:
    print(add(number1,number2)) #gives error int + str is not valid
except:
    print("gives error int + str is not valid please wirite right int or str") #due to error our following code will also stop
else:
    print("ADD went well")
    print(add(number1,number2))
finally:
    print("I always run wheather code is right or not I don't care")
#that's why we use exception handling