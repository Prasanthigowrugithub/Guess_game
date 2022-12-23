import random
Easy_level=random.randint(1,10)
Medium_level=random.randint(1,20)
Hard_level=random.randint(1,30)
login="Prashu00@gmail.com"
password="Prashu00"
player='Prashu'
login_ID=input("Enter the mail:")
pass_word=input("Enter the password:")
print(login_ID.upper(),"Cool! create the player name")
print("Note The player name appears to all players")
player_name=input("Enter the player name:")
print(player_name.upper(),"Super! Go for the game")
print("Select the level")

s="""
1.Easy
2.Medium
3.Hard
4.Exit
"""
print(s)

option=int(input("Enter the choice:"))
if option==1:
    guess=int(input("Guess the easy level number between 1 to 10:"))
while Easy_level!="guess":
    if guess<Easy_level:
        print("You are too low!")
        guess=int(input("Guess the easy level number between 1 to 10:"))
    elif guess>Easy_level:
        print("You are too high!")
        guess=int(input("Guess the easy level number between 1 to 10:"))
    else:
        print("Nice job! your guess is correct")
        print("Easy level is completed")
        break
    

option=int(input("Enter the choice:"))
if option==2:
    guess=int(input("Guess the medium level number between 1 to 20:"))
while Medium_level!="guess":
    if guess<Medium_level:
        print("You are too low!")
        guess=int(input("Guess the medium level number between 1 to 20:"))
    elif guess>Medium_level:
        print("You are too high!")
        guess=int(input("Guess the medium level number between 1 to 20:"))
    else:
        print("Great job! your guess is correct")
        print("Medium level is completed")
        break

option=int(input("Enter the choice:"))
if option==3:
    guess=int(input("Guess the hard level number between 1 to 30:"))
while Hard_level!="guess":
    if guess<Hard_level:
        print("You are too low!")
        guess=int(input("Guess the hard level number between 1 to 30:"))
    elif guess>Hard_level:
        print("You are too high!")
        guess=int(input("Guess the hard level number between 1 to 30:"))
    else:
        print("Amazing! you guess is correct")
        print("Hard level is completed")
        break

option=int(input("Enter the choice:"))
if option==4:
    print("Today's streak is completed")
    exit()
