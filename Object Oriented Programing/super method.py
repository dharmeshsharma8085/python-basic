class car:
    def __init__(self,type):
        self.type=type
        #yaha hum nai kuch type nhidiya isliye jub object cretae karegai tho
        # error ayega bolega type is not defined
    
    @staticmethod
    def start():
        print("Car is Started")
        
    @staticmethod
    def stop():
        print("Car is stoped")
        
class toytaCar(car):
    def __init__(self,name,type):
        super().__init__(type) # to acess method of parent class
        self.name=name
        super().start()
        super().stop()
car1=toytaCar("Supra","Disel")
print(car1.type)