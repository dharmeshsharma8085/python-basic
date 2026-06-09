print([1,2,3]) #  print only one row
print([4,5,6])
print([7,8,9]) # so if we want to print 3 diff list we have to print 3 times let debvelop function  that solve this problem

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    
r1=["","",""]
r2=["","",""]
r3=["","",""]
display(r1,r2,r3)
# now it' like a board of tic tac toe so let's test this also 
r2[1]="X"
display(r1,r2,r3)

# so like this we can play tic taxc toe just using display function i know it not
# perfect but at the end of this project or milestone there will be real game



# after display function there is input function

# result=int(input("Choose an any row:   "))
# result[1]="O"
# print(result)


# input function always take a vak=luews in form str there its is neccesasy for use to do type cast'
# oces input function is declare we can't overwrite it it will create probelm to complier



def user_choice():
    # Variable 
    # intial choice
    choice="Wrong"
    acceptable_range=range(0,11)
    within_range=False
    
    # Two codition should check
    # range and isdigit
    while choice.isdigit()==False or within_range==False:
        
        choice=input("Enter any nymber from (0 to 10)  :")
         #Digit check
        if choice.isdigit()==False:
            print("Sorry that is not a digit")
         #Range check
         
        else:
         
            if choice.isdigit()==True:
                if int(choice) in acceptable_range:
                 within_range=True
                 
                else:
                    print("Sorry you are out of range from ouer acceptable range 0 to 10")
                within_range=False
             
    return int(choice)
    
user_choice()

