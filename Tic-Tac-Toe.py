def main():
    x=[]
    o=[]

    Win_condition = win(x,o)

    while Win_condition == False:
        ##Print the board 
        print_bord(x,o)

        ##Determine whose turn it is 
        ##Ask if that player for an input 
        ##Calculate the wind condition
        Win_condition = win(x,o)
        ##print_bord(x,o)

    else:
        ##Victory message
        pass

def turn(player):

    pass

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

def win(x,o):
    Win_condition = False

    
    return Win_condition

if __name__ =='__main__':
    main()