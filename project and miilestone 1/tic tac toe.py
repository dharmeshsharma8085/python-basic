game_list=["","","",
           "","","",
           "","",""]
def display_game_list(game_list):
    print("\n")
    print(f" {game_list[0] or ' '} | {game_list[1] or ' '} | {game_list[2] or ' '} ")
    print("---|---|---")
    print(f" {game_list[3] or ' '} | {game_list[4] or ' '} | {game_list[5] or ' '} ")
    print("---|---|---")
    print(f" {game_list[6] or ' '} | {game_list[7] or ' '} | {game_list[8] or ' '} ")
    print("\n")
    
def player_choice(game_list):
    choice="wrong"
    while choice not in ["1","2","3","4","5","6","7",'8','9']:
        choice=input("choose a postion (1-9)  : ")
        if choice not in ["1","2","3","4","5","6","7",'8','9']:
            print("Invalid choice:  ")
    return int(choice)-1


def place_marker(game_list,turn,position):
    game_list[position]=turn





def win_check(game_list,turn):
    return(
        (game_list[0]==game_list[1]==game_list[2]==turn) or
        (game_list[3]==game_list[4]==game_list[5]==turn) or
        (game_list[6]==game_list[7]==game_list[8]==turn) or
        (game_list[0]==game_list[3]==game_list[6]==turn) or
        (game_list[1]==game_list[4]==game_list[7]==turn) or
        (game_list[2]==game_list[5]==game_list[8]==turn) or
        (game_list[0]==game_list[4]==game_list[8]==turn) or
        (game_list[2]==game_list[4]==game_list[6]==turn)      
        
    )
    
def space_check(game_list,position):
    return game_list[position]==""

def full_board_check(game_list):
    return""not in game_list



# main game-----
player1="X"
player2="O"
turn=player1
game_on=True
print("Welcome to Tic Tac Toe")
while game_on:
    display_game_list(game_list)
    print(f"player{turn}'s turn")
    
    position=player_choice(game_list)
    if space_check(game_list,position):
        place_marker(game_list,turn,position)
        
        if win_check(game_list,turn):
            display_game_list(game_list)
            print(f"player{turn}'s won the game")
            game_on=False
        
        else:
            if full_board_check(game_list):
                display_game_list(game_list)
                print("Match draw")
                break
        
            else:
                turn=player2 if turn ==player1 else player1
                
                
    else:
        print("postion alredy fixed Try again")
        