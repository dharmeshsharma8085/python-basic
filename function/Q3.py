def sum_digit(n):
    total=0
    while n<=0:
        digit=n%10
        total+=digit
        n=n//10
        return total


print(sum_digit(3456))