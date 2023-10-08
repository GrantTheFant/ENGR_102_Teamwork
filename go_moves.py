# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clayton Dodgen (572)
#               Grant Gallun
#               Arman Mediratta
#               Micah Alummoottil
# Section:      472, 572
# Assignment:   Lab 7: go_moves.py
# Date:         21 9 2023


# initalizing all variables
goboard = [[], [], [], [], [], [], [], [], []]
empty_piece = "."
whitepiece = "o"
blackpiece = "O"
isWhite = False

# initalizes board
for i in range(9):
    for k in range(9):
        goboard[i].append(empty_piece)


# prints current board
def printBoard():
    for i in goboard:
        row = str.join(" ", i)
        print(row)


# Checks if location is true, and if it is an actual location
def is_Val_True(location):
    l_split = location.split(" ")
    if len(l_split) != 2 or (
        l_split[0].isdigit() == False or l_split[1].isdigit() == False
    ):
        return False
    xVal = int(location.split(" ")[0])
    yVal = int(location.split(" ")[1])
    if (xVal > 9 or xVal < 1) or (yVal > 9 or yVal < 0):
        return False
    return True


# places the pieces for the board
def placePiece(movex, movey):
    global isWhite
    # checks if move is out of index or if another piece is present
    if (
        movex > 9
        or movey > 9
        or goboard[9 - movex][movey - 1] == whitepiece
        or goboard[9 - movex][movey - 1] == blackpiece
    ):
        print("Piece already present")
        return False
    # Checks who's turn it is and places a piece at the position according to player color
    if isWhite:
        goboard[9 - movex][movey - 1] = whitepiece
        isWhite = False
    elif not isWhite:
        goboard[9 - movex][movey - 1] = blackpiece
        isWhite = True
    printBoard()


location = ""
# Asks the user for inputs until the user inputs stop to stop program
while location != "stop":
    location = input(
        "Input a location for your piece enter for location (x y) | Or type 'stop' to stop: "
    )
    if location == "stop":
        break
    res = is_Val_True(location)
    if res == False:
        while res == False:
            # Lets user know their input was invalid and prompts them for a proper move
            location = input(
                "Please input a valid location for your piece (x y) | Or type 'stop' to stop: "
            )
            res = is_Val_True(location)
    xVal = int(location.split(" ")[0])
    yVal = int(location.split(" ")[1])
    placePiece(yVal, xVal)
