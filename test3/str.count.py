str="programming"
i=0
dict={}
while i<len(str):
    ch=str[i]
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
        
    i+=1

print(dict)
    