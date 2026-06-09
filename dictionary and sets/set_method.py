collection={1,2,3,4,"lucky","earth"}
collection.add("34")
print(collection)

collection1={1,2,3,4,"lucky","earth"}
collection1.remove("lucky")
print(collection1)

collection3={1,2,3,4,"lucky","earth"}
collection3.clear()
print(collection3)

collection2={1,2,3,4,"lucky","earth"}
print(collection2.pop())

set1={1,2,3,4,"lucky","earth"}
set2={1,3,5,"Dharmesh"}
print(set1.union(set2))#all value single time
print(len(set1.union(set2)))

collection5={1,2,3,4,5,6,7,8,"yoyo"}
set3={1,3,5,"Dharmesh"}#all commom value
print(collection5.intersection(set3))
