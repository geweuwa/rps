import random
history = []
class user_turn:
    def rps_check():
        check = False
        user_input = input("r, p, or s? ")
        
        if user_input == "r":
            check = True
        elif user_input == "R":
            check = True
        elif user_input == "p":
            check = True
        elif user_input == "P":
            check = True
        elif user_input == "s":
            check = True
        elif user_input == "S":
            check = True

        if check == True:
            history.append(user_input)
        elif check != True:
            print()
    