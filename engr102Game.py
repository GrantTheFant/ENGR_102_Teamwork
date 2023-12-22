# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clayton Dodgen (572)
#               Grant Gallun
#               Arman Mediratta
#               Micah Alummoottil
# Section:      472, 572
# Date:         11/29/23

import requests
from bs4 import BeautifulSoup
import numpy as np
import sys 
from termcolor import colored

instructionswordle = 'The instructions for how to play Wordle are as follows: You will be prompted to enter a word of your desired length in hopes of guessing the secret word, if a letter from your word is highlighted yellow, it means that letter is in the secret word but in the wrong position, if the letter is green that means it is in the right position, and if the letter is red that means it is not in the word. The number of guesses available to you is the same as the length of the word.'
instructionshangman = 'The instructions for how to play Hangman are as follows: This is a 2 player game. Player 1 will enter a word (at least 6 letters) for the other person to guess. Then, Player 2 will have 6 guesses to figure out the word, your guesses must be letters and not the full word.'
instructionsconnect = 'The instructions for how to play ConnectFour are as follows: This is a 2 player game. Player 1 and Player 2 will take turns inputting positions on a 7 x 6 grid of circles, once a player obtains 4 circles in a row in a horizontal, vertical, or diagonal line, the game is over and that player has won'



######################## HANGMAN GAME FUNCTIONS HERE ##################################
def hangmanfun():
    print(instructionshangman + '\n')
    secret = input("Enter the secret word: ")    
    if len(secret) < 6:
        while len(secret) < 6:
            secret = input("Please enter a valid word (6 letters or more): ") 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    original = secret
    hangman = [[" /----   "," /----   "," /----   "," /----   "," /----   "," /----   "," /----   ",],
               [" |       "," |   O   "," |   O   "," |   O   "," |   O   "," |   O   "," |   O   ",],
               [" |       "," |       "," |   |   "," |  /|   "," |  /|\\ "," |  /|\\ "," |  /|\\ ",],
               [" |       "," |       "," |       "," |       "," |       "," |  /    "," |  / \\  "],
               ["/ \\_____","/ \\_____","/ \\_____","/ \\_____","/ \\_____","/ \\_____","/ \\_____ "]]
    ogkey = set()
    key = set()
    letters = set()
    count = 0
    lives=6
    secret=secret.lower()
    #print(secret)
    secret = list(secret)
    empty=[]
    used = []
    for i in range(len(secret)):
        empty.append("_")
                 
    for i in secret:
        key.add(i)
        ogkey.add(i)

    def print_hangman(letter):
        for i in hangman:
            print(i[6-lives])
        for i in range(len(secret)):
            if secret[i]==letter:
                empty[i]=letter
        print(" ".join(empty))
        print("")


    guess = True
    print_hangman("")
    letter = (input("Guess a letter: ")).lower()
    while len(letter) != 1:
        letter = (input("Invalid guess. Please guess a letter: "))
    used.append(letter)
    if letter in key:
        key.remove(letter)
        count += 1
        print_hangman(letter)
        print(f'Used Letters: {", ".join(used)}')
    else:
        lives=lives-1
        print_hangman("")
        print(f"Wrong guess, you now have {lives} lives")
        count += 1

    while lives!=0 and key != letters:
        letter = (input("Guess another letter: ")).lower()
        while len(letter) != 1:
            letter = (input("Invalid guess. Please guess a letter: "))
        if letter not in used:
            used.append(letter)
        elif letter in used:
            print("you already guessed this letter")
            continue
        if letter in key:
            key.remove(letter)
            #print(key,set)
            print_hangman(letter)
            print(f'Used Letters: {", ".join(used)}')
        else:
            lives=lives-1
            print_hangman("")
            print(f'Used Letters: {", ".join(used)}')
            print(f"Wrong guess, you now have {lives} lives")
        count += 1

    #print(key==set)
    if key == letters:
        print(f'The secret word is: "{original}". You found it in {count} guess(es)!')
    else:
        print(f'The secret word is: "{original}". You had {count-6} correct guess(es)!')
    
    
    
        
    ending = input("Thanks for playing Hangman! Type \"main\" to go back to the main menu, \"exit\" to exit the program or, \"replay\" to play again: ")
    if ending == 'main':
        mainMenu()
    elif ending == 'replay':
        print('')
        hangmanfun() #REPLACE
    elif ending == 'exit':
        exit()
    else:
        ending = input('Invalid input, try again: ')
        while ending != 'main' and ending !=  'exit' and ending != 'replay':
            ending = input('Invalid input, try again: ')
        if ending == 'main':
            mainMenu()
        elif ending == 'replay':
            print('')
            hangmanfun() #REPLACE
        elif ending == 'exit':
            exit()


######################## CONNECT4 GAME FUNCTIONS HERE ##################################
#connect 4
board=[['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
       ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
       ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
       ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
       ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
       ['⚪','⚪','⚪','⚪','⚪','⚪','⚪']]


red= '🔴'
blue = '🔵'
empty= '⚪'

def reset():
    global board
    for i in range(len(board)):
        for k in range(len(board[i])):
            board[i][k]=empty

def printBoard(board):
    for i in range(len(board)):
        print(" ".join(board[i]))
        
    print(' 1  2  3  4  5  6  7\n')
        


def placepiece(move,turn):
    global board
    move=move-1
    hitpiece=False
    try:
        if move>6 or move<0:
            print("Please enter a valid column.(1-7)")
            return "Wrong"
    except:
        print("Please enter a valid integer.(1-7)")
    if board[0][move]!=empty:
        print("Column is full, please try another move.")
        return "Wrong"
    for height in range(7):
        if height>5 or board[height][move]==blue or board[height][move]==red:
            hitpiece==True
            #print("setTrue")
            break
    try:        
        if turn=='red':
            board[height-1][move]=red
        if turn == 'blue':
            board[height-1][move]=blue

        
    except:
        print("please input valid move")

def checkWin(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column]!=empty and (checkHorizontal(row, column) or checkVertical(row,column) or checkDiagonal(row,column)):
                if board[row][column]==red:
                    print("Red is the winner")
                    return True
                else:
                    print("Blue is the winner")
                    return True
    return False

def checkTie(board):
    for column in range(len(board[0])):
        if board[0][column]==empty:
            return False
    print("The game is a tie.")
    return True

def checkHorizontal(row,column):
    count=0
    for i in range(1,4):
        try:
            if board[row][column]!=board[row][column+i]:
                break
        except:
            break
        count+=1
        if count==3:
            return True
    count=0    
    for i in range(1,4):
        try:
            if (column-i)<0 or board[row][column]!=board[row][column-i]:
                break
        except:
            break
        count+=1
        if count==3:
            return True

def checkVertical(row,column):
    count=0
    for i in range(1,4):
        try:
            if board[row][column]!=board[row+i][column]:
                break
        except:
            break
        count+=1
        if count==3:
            return True
    count=0    
    for i in range(1,4):
        try:
            if (row-i)<0 or board[row][column]!=board[row-i][column]:
                break
        except:
            break
        count+=1
        if count==3:
            return True    
#     return

def checkDiagonal(row,column):    
    count=0
    for i in range(1,4):
        try:
            if board[row][column]!=board[row+i][column+i]:
                break
        except:
            break
        count+=1
        if count==3:
            return True
    count=0    
    for i in range(1,4):
        try:
            if (row-i)<0 or (column-i)<0 or board[row][column]!=board[row-i][column-i]:
                break
        except:
            break
        count+=1
        if count==3:
            return True       
    count=0    
    for i in range(1,4):
        try:
            if (column-i)<0 or board[row][column]!=board[row+i][column-i]:
                break
        except:
            break
        count+=1
        if count==3:
            return True  
        count=0    
    for i in range(1,4):
        try:
            if (row-i)<0 or board[row][column]!=board[row-i][column+i]:
                break
        except:
            break
        count+=1
        if count==3:
            return True    
        
def connect4fun():
    reset()
    turn='red'
    print(instructionsconnect + '\n')
    printBoard(board)
    while checkWin(board)==False and checkTie(board)==False:
        move=input(f"{turn} please input a move: ")
        while move.isdigit()==False:
            move=input(f"{turn} please input a valid move (1-7): ")
        if placepiece(int(move),turn)=="Wrong":
            if turn=='red':
                turn='blue'
            else:
                turn='red'  
        printBoard(board)
        if turn=='red':
            turn='blue'
        else:
            turn='red'
            
            
            
    ending = input("Thanks for playing Connect 4! Type \"main\" to go back to the main menu, \"exit\" to exit the program or, \"replay\" to play again: ")
    if ending == 'main':
        mainMenu()
    elif ending == 'replay':
        print('')
        connect4fun() #REPLACE
    elif ending == 'exit':
        exit()
    else:
        ending = input('Invalid input, try again: ')
        while ending != 'main' and ending !=  'exit' and ending != 'replay':
            ending = input('Invalid input, try again: ')
        if ending == 'main':
            mainMenu()
        elif ending == 'replay':
            print('')
            connect4fun() #REPLACE
        elif ending == 'exit':
            exit()



######################## WORDLE GAME FUNCTIONS HERE ##################################

def genWord(lenWord):
    res = requests.get('https://www.angelfire.com/extreme4/safer_sephiroth/EVERY_WORD_EVER.htm')
    soup = BeautifulSoup(res.text, 'html.parser').text.split('\n')
    filteredWords = []

    for index, i in enumerate(soup):
        if index > 12850:
            continue
        filteredWords.append(i.lower())

        sys.stdout.write("\rFetching words %i" % index)
        sys.stdout.flush()
    
    sys.stdout.write(f'\r{index} Words fetched!')

    np.random.shuffle(filteredWords)
    print('')

    for word in filteredWords:
        if len(word) == lenWord:
            return word
        
def constructWordData(secertWord):
    secertData = {}
    for letter in secertWord:
        try:
            secertData[letter] += 1
        except:
            secertData[letter] = 1
    return secertData

def wordFormater(secertWord, guess):
    wordData = {}
    secertData = constructWordData(secertWord)
    guessData = constructWordData(guess)
    for i in range(len(secertWord)):
        if secertWord[i] == guess[i]:
            wordData[f'{guess[i]}_{i}'] = 'green'
        elif guess[i] in secertWord and guess[i] != secertWord[i] and guessData[guess[i]] <= secertData[guess[i]]:
            wordData[f'{guess[i]}_{i}'] = 'yellow'
        else:
            wordData[f'{guess[i]}_{i}'] = 'red'
    return wordData

def isValidGuess(secertWord, guess):
    if secertWord == guess:
        return True
    else:
        return False

def wordlefun():
    print(instructionswordle + '\n')
    wordLen = input('Enter Word length: ')
    isValidInput = False

    while isValidInput == False:
        try:
            wordLen = int(wordLen)
            isValidInput = True
        except:
            wordLen = input('Invalid Length, Try Again: ')

    print(f'Word length set to {wordLen} you have {wordLen} trys, good luck!')

    wordToGuess = genWord(wordLen)
    numGuesses = 0
    foundWord = False

    while numGuesses < wordLen:
        currGuess = input('Enter guess: ')
        if len(currGuess) != wordLen:
            while len(currGuess) != wordLen:
                currGuess = input('Invalid guess. try again: ')

        numGuesses += 1
        guessData = wordFormater(wordToGuess, currGuess)
        foundWord = isValidGuess(wordToGuess, currGuess)
        for i in guessData:
            print(colored(i.split('_')[0], guessData[i], attrs=['blink']), end='')
        print('')
        if foundWord == True:
            break
    
    #BASE EXIT CODE
    
    #Type "exit" to go back to the main menu or "e" or exit the program or "replay" to play again: base print
    #MAKE SURE TO LOWERCASE
    
    if foundWord == False:
        ending = input(f'The word was {wordToGuess}. Type "main" to go back to the main menu or "exit" or exit the program or "replay" to play again: ').lower()
    else:
        ending = input(f'Congrats! It took you {numGuesses} to get the wordle! Type "main" to go back to the main menu or "exit" to exit the program or "replay" to play again: ').lower()

    if ending == 'main':
        mainMenu()
    elif ending == 'replay':
        print('')
        wordlefun() #REPLACE
    elif ending == 'exit':
        exit()
    else:
        ending = input('Invalid input, try again: ')
        while ending != 'main' and ending !=  'exit' and ending != 'replay':
            ending = input('Invalid input, try again: ')
        

######################## MAIN MENU FUNCTION ##################################

def mainMenu():
    gameinput = input('Please enter the name of the game you would like to play (Hangman, Wordle, ConnectFour), or enter "exit" to exit the program: ')
    gameinput = gameinput.lower()
    while True:
        if gameinput == 'wordle':
            print('')
            wordlefun()
            break
        if gameinput == 'hangman':
            print('')
            hangmanfun()
            break
        if gameinput == 'connectfour':
            print('')
            connect4fun()
            break
        if gameinput == 'exit':
            exit()
        if gameinput != 'wordle' and gameinput != 'connectfour' and gameinput != 'hangman':
            gameinput = input('Bad input, please enter the name of the game you would like to play (Hangman, Wordle, ConnectFour): ')
            gameinput = gameinput.lower()


#everything above is start of the file
#at end of game is everything below

######################## MAIN FUNCTIONS STARTS ##################################


gamereplay = ''
instructions = 'The 3 games we have available to play are Wordle, Hangman, and Connect 4.'
print(instructions + '\n')
    

mainMenu()