def main():
    x=[]
    o=[]

    Win_condition = win(x,o)
    Current_turn = False

    while Win_condition == False:
        ##Print the board 
        print_bord(x,o)

        ##Determine whose turn it is 
        
        Current_turn = turn(Current_turn)
        ##Ask if that player for an input 
        Choose_tile(Current_turn,x,o)
        
        ##Calculate the wind condition
        Win_condition =win(x,o,Current_turn)
        

    else:
        ##Victory message
        print(f'{Current_turn} has wone the game!!!')
        pass

def turn(Current_turn):
    if Current_turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    return turn
    
def Choose_tile(Current_turn,x,o):
    tile = input(f'{Current_turn}\'s turn to choose a square (1-9):')
    while tile.isnumeric() == False:
        print(f'{tile} is not a valid answer try again')
        tile = input(f'{Current_turn}\'s turn to choose a square (1-9):')

    if Current_turn == 'x':
        x.append(int(tile))
    else:
        o.append(int(tile))



def print_bord(x,o):
    tiles ={
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9'
    }

    for _ in x:
        tiles[_]='X'

    for _ in o:
        tiles[_]='O'
    
    print(f'''
    {tiles[1]}|{tiles[2]}|{tiles[3]}
    -+-+-
    {tiles[4]}|{tiles[5]}|{tiles[6]}
    -+-+-
    {tiles[7]}|{tiles[8]}|{tiles[9]}
    
    ''')
    pass 

def win(x,o,Current_turn):
    Win_condition = False
    wins={
        'r1':[1,2,3],
        'r2':[4,5,6],
        'r3':[7,8,9],

        'c1':[1,4,7],
        'c2':[2,5,8],
        'c3':[3,6,9],

        'x1':[1,5,9],
        'x2':[3,5,7]
    }

    if Current_turn == 'x':
        Current_array = x
    else:
        Current_array = o

    for _ in wins:
        t1 = lambda _: _[1] in Current_array
        t2 = lambda _: _[2] in Current_array
        t3 = lambda _: _[3] in Current_array
        if t1 and t2 and t3 == True:
            Win_condition = True
            break
    return Win_condition

if __name__ =='__main__':
    main()