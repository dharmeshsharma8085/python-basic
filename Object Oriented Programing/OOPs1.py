mylist=[1,2,3]
myset=set()
print(type(myset))
class Sample(): # use camle casing
    pass

my_sample=Sample()
print(type(my_sample))
# Simplest class we can create possibly now let 
# add some parameter and atributes

class Dog():
    
    def __init__(self,mybreed,name,spots):
        self.mybreed=mybreed
        # self represent instance of class we can use any keyword instead if self
        #self.my_Attributes=mybreed
        #Attributes 
        #We take in the argument
        #Assign it using self.attribute_name
        # attribute==para
        #self.breed==method jo hum nai khud banaya
        # hai fir usko humnai apne attribute sai 
        # equal kar diya hai
        self.name=name
        self.spots=spots
        print("These is a contructor")
        
my_dog=Dog(mybreed="Adivasi",name="Abhishek",spots="Yes")
print(my_dog)
print(type(my_dog))

print(my_dog.breed,my_dog.name,my_dog.spots) #pass assign attributes

my_dog1=Dog(mybreed="Adivasi",name="Abhi",spots="Yes")
print(my_dog1)
print(my_dog1.mybreed,my_dog1.name,my_dog1.spots)