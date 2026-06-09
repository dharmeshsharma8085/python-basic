# jub tak condition true hpogi tub tak loop chalega
i=1
while i<=5:
    print("Dharmesh",i)
    i+=1
    print("loop ended")

    #print number from 1 to 100
    i=1
    while i<=100:
        print(i)
        i+=1
        
#print number from 100 to 1
i=100
while i>=1:#this is a stoping condition
    print(i)
    i-=1
    
#print a multipliction table of number n
n=int(input("enter any value of n:"))
i=1
while i<=10:
    print(n*i)
    i+=1

#print square till 10
i=1
while i<=10:
    print(i*i)
    i+=1

# tuple or list example
nums=(1,4,9,16,25,36,49,64,81,100,)
i=0 #intilization
while i<len(nums):
    print(nums[i])
    i+=1
#tarvere each tuples or list element one by one

nums=(1,4,9,16,25,36,49,64,81,100,)
x=int(input("enter number"))
i=0 #intilization
while i<len(nums):
    if(nums[i]==x):
        print("element found",i)
    else:
        print("finding.....")
    i+=1