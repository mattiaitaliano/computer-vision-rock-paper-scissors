import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def get_user_choice():
    return input("Pick Rock, Paper or Scissor: ").capitalize()


def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    else:
        if computer_choice == "Rock":
            if user_choice == "Paper":
                return "You won!"
            else:
                return "You lost"
        elif computer_choice == "Paper":
            if user_choice == "Scissors":
                    return "You won!"
            else:
                    return "You lost"
        elif computer_choice == "Scissors":
            if user_choice == "Rock":
                    return "You won!"
            else:
                    return "You lost"   


def play():
    computer_choice = get_computer_choice()
    print(computer_choice)
    user_choice = get_user_choice()
    print(get_winner(computer_choice, user_choice))
    

play()