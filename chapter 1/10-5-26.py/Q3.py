str="hello"
str_lower=str.lower()
vowel="a","e","i","o","u"
count=0
for  i in str_lower:
    if i in vowel:
        count+=1


print(count)