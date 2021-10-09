# import time
# #Indroduction to the game
# print("Hello there \nWelcome to TIC-TAC-TOE")
# time.sleep(1)
# #list of numbers
# num_list = [1,2,3,4,5,6,7,8,9]
# print(num_list)
# #Request for tutorial
# def tutorial():
#     tutorial_list = ["=>This game is restricted to 2 players only", 
#     "=>There are two characters used to play this game 'X' and 'O'",
#     "=>Whoever chooses 'X' would go first", 
#     "=>A board would be printed out every time a player makes a move", 
#     "=>Numbers 1-9 would be used to determine postions on the board", 
#     "=>The first player to get '3' of their characters to either horizontally, vertically or diagonally WINS!", 
#     "=>Goodluck and REMEMBER TO HAVE FUN"]
#     for item in tutorial_list:
#         print(item)
#         time.sleep(5)

# #countdown to begin game
# def countdown():
#     t = 3
#     while t > 0:
#         print(t)
#         time.sleep(1)
#         t -=1
#     return "Lets Go!!!"

# def begin_game():
#     start = 'no'
#     if start == 'y':
#         print(countdown())
#     elif start == 'n':
#         print('Closing Game')
#     while start != 'y' or start !='n':
#         start = input("Begin Game?(y/n)")
#         start = start.lower()


boardlist = [" " for i in range(10)]
boardlist[0] = "nil"
def board(boardlist): 
    print(f"\n  {boardlist[1]}  |  {boardlist[2]}  |  {boardlist[3]}  ")
    print("-----|-----|-----")
    print(f"  {boardlist[4]}  |  {boardlist[5]}  |  {boardlist[6]}  ")
    print("-----|-----|-----")
    print(f"  {boardlist[7]}  |  {boardlist[8]}  |  {boardlist[9]}  ")

def insertLetter(pos, letter):
    board[pos] = letter

def freeSpace(pos):
    return boardlist[pos] == " "

def isBoardFull():
    return " " not in boardlist

def playerMove():
    a = True
    while a:
        position = input("Enter the position to place an 'X' (1-9): ")
        try:
            position = int(position)
            if position in range(1,10):
                if freeSpace(position):
                    insertLetter(position, 'X')
                    a = False
                else:
                    print("Sorry, this spot is occupied!")
            else:
                print("Enter a number between 1-9!")

        except:
            print("Enter a number!")

def computerMove():
    possiblePositions = []
    for i, letter in enumerate(boardlist):
        if letter == " ":
            possiblePositions.append(i)

    moves = ['X', 'O']
    for _ in moves:
        for i in possiblePositions:
            sampleBoard = boardlist[:]
            sampleBoard[i] = _
            if checkWin(sampleBoard, _):
                move = i
                return move

            


            
# function to check who won the game
def checkWin(bod, let):
    return (bod[1] == let and bod[2] == let and bod[3] == let) or (bod[4] == let and bod[5] == let and bod[6] == let) or (bod[7] == let and bod[8] == let and bod[9] == let) or (bod[1] == let and bod[4] == let and bod[7] == let) or (bod[2] == let and bod[5] == let and bod[8] == let) or (bod[3] == let and bod[6] == let and bod[9] == let) or (bod[1] == let and bod[5] == let and bod[9] == let) or (bod[3] == let and bod[5] == let and bod[7] == let)

def m():
    game = 3
    charCount = 1
    while game > 0:
        if charCount % 2 ==  0:
            char = 'O'
        else: 
            char = 'X'
        print(char)
        charCount += 1
        game -= 1

def preset():
    new = 'none'
    new = new.lower()
    while new != 'y':
        new = input('Do you wish to go through the tutorial?(y/n): ')
    return tutorial()
    print(begin_game())


def main():
    board()

    while not isBoardFull():
        if checkWin(boardlist, 'X'):
            print("X won!")
            break
        else:
            computerMove()
            board()
        
        if checkWin(boardlist, 'O'):
            print("O won!")
            break
        else:
            playerMove()
            board()


        

    else:
        print("Tie game")
        


#function to print the score board
def scoreboard(score_board):
    print("------------------------------")
    print("          SCOREBOARD          ")
    print("------------------------------")

    players = [score_board.keys()]
    for i in range(2):
        print(f"   {players[i]},    {score_board[players[i]]}")

    print("------------------------------")
        