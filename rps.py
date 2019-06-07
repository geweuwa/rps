from turn import *
round = 0

#determine win, loss, or draw.

def win_cond():
    if user_input == "r" and bot_choice == "s":
        print("Your oppenent chose scissors. You win!")
    elif user_input == "r" and bot_choice == "r":
        print("Your opponent chose rock. Tie.")
    elif user_input == "r" and bot_choice == "p":
        print("Your opponent chose paper. You lose.")
    elif user_input == "s" and bot_choice == "p":
        print("Your oppenent chose paper. You win!")
    elif user_input == "s" and bot_choice == "s":
        print("Your opponent chose scissors. Tie.")
    elif user_input == "s" and bot_choice == "r":
        print("Your opponent chose rock. You lose.")
    elif user_input == "p" and bot_choice == "r":
        print("Your oppenent chose rock. You win!")
    elif user_input == "p" and bot_choice == "p":
        print("Your oppenent chose paper. Tie.")
    elif user_input == "p" and bot_choice == "s":
        print("Your opponent chose scissors. You lose.")


user_init = input("""
To play - type 'play'
To quit - type 'quit'

What would you like to do? """)

while user_init != "quit":

    if user_init == "play":
        user_input = user_turn.rps_check()
        round += 1

        t1 = random.randint(1,2)
        if t1 == 1:
            bot_choice = "s"
        elif t1 == 2:
            bot_choice = "r"

        win_cond()
        user_init = input("""
To play - type 'play'
To quit - type 'quit'

What would you like to do? """)

s = "r" in history
print(history)
print(round)
print(history.count("r"))