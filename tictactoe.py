import time
#Indroduction to the game
print("Hello there \nWelcome to TIC-TAC-TOE")
time.sleep(1)
#Request for tutorial
def tutorial():
    tutorial_list = ["=>This game is restricted to 2 players only", 
    "=>There are two characters used to play this game 'X' and 'O'",
    "=>Whoever chooses 'X' would go first", 
    "=>A board would be printed out every time a player makes a move", 
    "=>Numbers 1-9 would be used to determine postions on the board", 
    "=>The first player to get '3' of their characters to either horizontally, vertically or diagonally WINS!", 
    "=>Goodluck and remember to have fun"]
    for item in tutorial_list:
        print(item)
        time.sleep(5)

#countdown to begin game
def countdown():
    t = 3
    while t > 0:
        print(t)
        time.sleep(1)
        t -=1
    return "Lets Go!!!"

def begin_game():
    start = 'no'
    if start == 'y':
        print(countdown())
    elif start == 'n':
        print('Closing Game')
    while start != 'y' or start !='n':
        start = input("Begin Game?(y/n)")
        start = start.lower()

#Different boards
    #Tutorial Decision Input
def preset():
    new = 'none'
    new = new.lower()
    while new != 'y':
        new = input('Do you wish to go through the tutorial?(y/n): ')
    else:
        print(tutorial())
    print(begin_game())

print(preset())

