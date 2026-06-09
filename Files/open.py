f=open("demo.txt","r")
#default mode = read only
data=f.readline()
print(data)
print(type(data))
f.close( )