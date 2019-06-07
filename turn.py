import random
history = []


class user_turn:
    def rps_check():
        check = False
        user_input = input("r, p, or s? ")
        
        if user_input == "r":
            check = True
            history.append(user_input)
            return "r"
        elif user_input == "R":
            check = True
            history.append(user_input)
            return "r"
        elif user_input == "p":
            check = True
            history.append(user_input)
            return "p"
        elif user_input == "P":
            check = True
            history.append(user_input)
            return "p"
        elif user_input == "s":
            check = True
            history.append(user_input)
            return "s"
        elif user_input == "S":
            check = True
            history.append(user_input)
            return "s"

    