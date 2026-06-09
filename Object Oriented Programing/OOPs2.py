class Dog():
    #Class Object Attribute
    #Same for Any Instance Of Class
    species="Mammal" #,common for all class
    def __init__(self,mybreed,name,):
        self.breed=mybreed
       
        self.name=name

        
    #Opeeration/Action function assign inside the class is called method 
    def bark(self,number):
        print("Boooooo!!!!! my name is {} and number is {}".format(self.name,number))
        
my_dog=Dog("Adivasi","Abhishek")
print(my_dog)
print(type(my_dog))

print(my_dog.breed,my_dog.name,my_dog.species) #pass assign attributes

my_dog.bark(10)


class Circle():
    #Class object attribute
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*self.pi
        # pi is a class attribute there self.pi==Cirlce.pi
        
    #method
    def get_circumfrence(self):
        return self.radius*self.pi*2
    
my_circle=Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumfrence())
print(my_circle.area)
