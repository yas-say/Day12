#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from mylogo import logo
from replit import clear
from random import randint

print(logo)
# input()
# clear()

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_num = randint(1,100)
#print(chosen_num)
chosen_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if chosen_level == "easy":
  turn = 10
elif chosen_level == "hard":
  turn = 5

# flag = 0
# while turn > 0:
#   print(f"You have {turn} attempts remaining to guess the number.")
#   guessNum = int(input("Make a guess: "))
#   if guessNum == chosen_num:
#     print(f"You got it! The answert was {chosen_num}")
#     turn = 0
#     flag = 1
#   else:
#     if guessNum < chosen_num:
#       print("Too low.")
#       if(turn > 1):
#         print("Guess again.")
#     elif guessNum > chosen_num:
#       print("Too High.")
#       if(turn > 1):
#         print("Guess again.")
#     turn -= 1

# if flag == 0:
#   print("You've run out of guesses, you lose.")

def guess_the_num():
  count = turn
  while count > 0:
    print(f"You have {count} attempts remaining to guess the number.")
    guessNum = int(input("Make a guess: "))
    if guessNum == chosen_num:
      print(f"You got it! The answert was {chosen_num}")
      return
    else:
      if guessNum < chosen_num:
        print("Too low.")
        if(count > 1):
          print("Guess again.")
      elif guessNum > chosen_num:
        print("Too High.")
        if(count > 1):
          print("Guess again.")
      count -= 1
  print("You've run out of guesses, you lose.")


guess_the_num()