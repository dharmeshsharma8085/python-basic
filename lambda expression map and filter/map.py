def square(num):
    return num**2

my_nums=[1,2,3,4,5,6,7,8,9]
 # if i want tp print all square of number so we hav to use for loop but now we introduce map functio
 
for item in map(square,my_nums):
    print(item)
    
list(map(square,my_nums))
