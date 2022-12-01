import random

CHOICES = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    choice = random.choice(CHOICES)
    return choice


def get_user_choice():
    choice = input("Pick Rock, Paper or Scissor: ")
    return choice
