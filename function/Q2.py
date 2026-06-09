def print_nums(n):
    if n <=1:
     return "Not prime"
    for i in range(2,n):
       if n%i==0:
          return"Not prime"
       
       
       return"prime"
    
    print(print_nums(34))