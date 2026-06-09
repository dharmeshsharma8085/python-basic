# i=1
# while i<=5:
#     print(i)
#     i+=1



#recusrive function
def shown(n):
    if(n==0):# condition to return beause we dont want to print till infinite
        return
    print(n)
    shown(n-1)


shown(345)