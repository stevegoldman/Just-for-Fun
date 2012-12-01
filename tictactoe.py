

 
def available_moves(game):
    return [square for (square,value) in enumerate(game) if not(value in ["X","O"])]

def moves_left(game):
    return len(available_moves(game))

def opponent(player):
    if player=="X":
        return "O"
    if player=="O":
        return "X"
    raise Exception("Error in opponent method")

def get_X_move(game):
    am=available_moves(game)
    move=int(input("Choose X's move from %s: "%str(am)))
    if move in am:
        return move
    else:
        return get_X_move(game)

def print_game(game):
    print()
    for row in range(3):
        print(game[row*3:row*3+3])
    print()

def best_move(game,player):
    if moves_left(game)==1:
        return available_moves(game)[0]
    best=available_moves(game)[0]
    for s in available_moves(game):
        new_game=game[:]
        new_game[s]=player
        o=outcome(new_game,player)
        
        if o==player:
            return s
        if o=="D":
            best=s
    return best

def outcome(game,player):
      
    if win(game,"X"):
        return "X"
    if win(game,"O"):
        return "O"
    if moves_left(game)==0:
        return "D"
    new_game=game[:]
    next_player=opponent(player)
    new_game[best_move(new_game,next_player)]=next_player
    return outcome(new_game,next_player)


def win(game,player):
    winners=[[0,1,2],[3,4,5],[6,7,8],
             [0,3,6],[1,4,7],[2,5,8],
             [0,4,8],[2,4,6]]

    for positions in winners:
        if len([p for p in positions if game[p]==player])==3:
            return True
    return False


def play():
    
    game=[str(i) for i in range(9)]
    player="X"
    winner=None
    print_game(game)
    while moves_left(game)>0:
        if player=="X":
            game[get_X_move(game)]="X"
            if win(game,"X"):
                winner=("X","computer")
                break
        else:
            game[best_move(game,"O")]="O"
            if win(game,"O"):
                winner=("O","human")
                break
        print("%s's move:"%player)
        print_game(game)
        player=opponent(player)
        
        
    if winner:
        print("%s wins, you stupid %s"%winner)
    else:
        print("It's a draw")
        
    print_game(game)    


if __name__=='__main__':
    play()
