def ask_for_int():
    while True:
        try:
            result= int(input("Enter a number"))
        except:
            print("Sorry we ask for integer")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try and except block  ")
    
print(ask_for_int())