str="Code with dharmesh"
words=str.split()
result=[]
for word in words:
    rev=""
    for ch in word:
        rev=ch+rev
        result.append(rev)

final_str="".join(result)
print(final_str)
