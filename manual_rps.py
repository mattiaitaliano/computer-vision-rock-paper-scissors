import random

CHOICES = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(CHOICES)


def get_user_choice():
    return input("Pick Rock, Paper or Scissor: ").capitalize()


def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    else:
        if computer_choice == CHOICES[0]:
            if user_choice == CHOICES[1]:
                return "You won!"
            else:
                return "You lost"
        elif computer_choice == CHOICES[1]:
            if user_choice == CHOICES[2]:
                    return "You won!"
            else:
                    return "You lost"
        else:
            if user_choice == CHOICES[0]:
                    return "You won!"
            else:
                    return "You lost"   


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(get_winner(computer_choice, user_choice))
    

play()