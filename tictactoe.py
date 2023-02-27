
# from tkinter import TRUE
def sum(a, b, c):
    return a + b + c 

def printBoard(xState, zState):
    # pass
    # print(f"{xState[0]?'X':(zState[0]?'O')} | 1 | 2")
    # it will not run so we should type python next //1 if 1 else 0 //exit()
    zero = 'X' if xState[0] else('O' if zState[0] else 0)
    one = 'X' if xState[1] else('O' if zState[1] else 1)
    two = 'X' if xState[2] else('O' if zState[2] else 2)
    three = 'X' if xState[3] else('O' if zState[3] else 3)
    four = 'X' if xState[4] else('O' if zState[4] else 4)
    five = 'X' if xState[5] else('O' if zState[5] else 5)
    six = 'X' if xState[6] else('O' if zState[6] else 6)
    seven = 'X' if xState[7] else('O' if zState[7] else 7)
    eight = 'X' if xState[8] else('O' if zState[8] else 8)
    # print(f"{'X' if xState[0] else('O' if zState[0] else 0)} | 1 | 2")
    # print(f"0| 1 | 2 ")
    #himanshu
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    # print(f"3| 4 | 5 ")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    # print(f"6| 7 | 8 ")
    print(f"{six} | {seven} | {eight} ")

def CheckWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [0, 4, 8], [2, 4, 6], [1, 4, 7], [2, 5, 8]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("1st player :himanshu won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("2nd player :himzo won the match")
            return 0
    # print("match draw")
    return -1        
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x and 0 for O
    print("welcome to tic tac toe")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("1st player X's chance")
            value = int(input("please enter a value"))
            xState[value] = 1
        else:
            print("2nd player O's chance")
            value = int(input("please enter a value"))
            zState[value] = 1
        cwin = CheckWin(xState, zState)
        if(cwin != -1):
            print("match over")
            break
        turn = 1 - turn
        # chance = not(chance)  #not(0)=True  not(1)=False
        # turn%turn 
        # break
# for exit press ctrl+c 