str=input("Enter any word :")
vowel="aeiouAeiou"
count=0
i=0
while i<len(str):
    if( str[i] in vowel):
        count+=1
    i+=1
    
print("Number of vowels are :",count)
    