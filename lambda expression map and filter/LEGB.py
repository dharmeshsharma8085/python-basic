name="This is a global string" # global
def greet():
    name="Dharmesh"  # enclose
    
    def hello():
        name="I am local"
        print("hello",name) # local
    
        print(hello())