from turn import *

user_input = user_turn.rps_check()

#first round only, random choice

t1 = random.randint(1,2)
if t1 == 1:
    bot_choice = "s"
elif t1 == 2:
    bot_choice = "r"

def win_cond():
        if user_input == "r" and bot_choice == "s":
            print("You win!")
        elif user_input == "r" and bot_choice == "r":
            print("Tie.")
        elif user_input == "r" and bot_choice == "p":
            print("You lose.")

win_cond()