class person:
    name="ano" # class attribute ,global
    
    def change_name(self,name):
        self.name=name
        
        # this is not class attribute ,local
        # let change class attribute instead of instance attribute
        person.name=name # ano change to rahul thiis is class method
        self.__class__.name="Ankit"  # another method
        
    @classmethod
    def change_name(cls,name):
        cls.name=name # this decorator directly change the class
        #attribute and give better function
        
p1=person()
p1.change_name("rahul")
print(p1.name)
print(person.name)


