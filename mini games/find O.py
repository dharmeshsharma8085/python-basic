Game=['','O','']
from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result=shuffle_list(Game)
print(result)

def player_guess():
    guess=""
    while guess not in ["0","1","2"]:
     guess=input('Pick a number from 0 to 2:')
#input always give value in string there fore we use int data type below
    return int(guess)

myindex=player_guess()
print(myindex)

def check_guess(mylist,guess):
    if mylist[guess]=="O":
        print("Wowwww you won a prize")
    else:
        print("Better luck next time")
        print(mylist)

#Intial list then shuffle the guess than check guess
#Intial list
mylist=['','O','']
#Shuffle list
mixedup_list=shuffle_list(mylist)
#User guess
guess=player_guess()
#check guess
check_guess(mixedup_list,guess)