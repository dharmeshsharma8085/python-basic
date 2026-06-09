class car:
    @staticmethod
    def start():
        print("Car is started")
        
    @staticmethod
    def stop():
        print("Car is stopped")    
        
    @staticmethod
    def color():
        print("Car is black in color")
        
class Toyta_car(car):
    def __init__(self,name):
        self.name=name
        
    

car1=Toyta_car("forturner")
print(car1.name,car1.start(),car1.stop(),car1.color())