#WAP to check if a list contain a palindrome of element(hint: use copy() method)
# marks=[12,15,17,15,12]
# marks.reverse()
# print(marks)

# #lst.copy()
grade=[1,2,3,2,1]
copy_list=grade.copy()
copy_list.reverse()
if(copy_list==grade):
    print("palindrome")
else:
    print("not palindrome")