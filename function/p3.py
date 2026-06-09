# # def fact(n):
# #     for item in range(1,n+1 ):
# #         print(n)
# #         n*=1

# #         fact(5)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    return fact


cal_fact(45)