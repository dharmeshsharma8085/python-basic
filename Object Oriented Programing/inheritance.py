class Animal(): #base class
    
    def __init__(self):
        print("Animal Class Is Created")
        
    def who_am_i(self):
        print("I am a Animal")
        
    def eat(self):
        print("I am Eating")
        
        
my_animal=Animal()
my_animal.who_am_i()
my_animal.eat()


class Dog(Animal): # dervied from base class
    
    def __init__(self):
        Animal.__init__(self) # init method if animal
        print("Dog Created")
    
    def who_am_i(self):
        print("I am a dog")    
mydog=Dog() # we can overide parent class method also

mydog.eat()  # derving from base class Animal
mydog.who_am_i()