fruits={
    "seasonal":{
        "mango","Grapes","orange"
},
"non_seasonal":{
    "Apple","Bannaa"
},
    
}
print(len(list(fruits.keys()))) 
print(len(fruits.values()))
print(fruits.get("seasonal"))
#print(fruits("seasonal")) this 2 give same output

info={
"name":"Dharmesh", 
"Surname":"Sharma",
"Rollno":"24EBKAI050"
 }
print(list(info.items()))
info.update({"city":"jaipur","age":"19","name":"lucky"})# apart from new memory we can also update old memory also
#print(pairs{0}) display at given index
print(info[2])
 # we can use other method by using vs studio only