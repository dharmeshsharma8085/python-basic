class dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+ " Say booooo !"
    
class cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+ " Say mewwww!"
    
kuta=dog("kuta")
bili=cat("billi")

print(kuta.speak())
print(bili.speak())


for pet in [ kuta,bili]:
    print(type(pet))
    print(pet.speak())
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(kuta)