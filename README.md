# Computer Vision RPS

Play rock, paper, scissors against your computer with your webcam!

<img src="https://blog.eduonix.com/wp-content/uploads/2019/10/CVT1.jpeg" alt="Image Alt Text" width="300" height="200">

## Model and how to use it

Thanks to https://teachablemachine.withgoogle.com/ I teached how to recognize 4 different images: Rock, Paper, Scissors and Nothing.

This will be usefull to let the webcam recognize the sign I'll do to interact with the program and let the computer be aware if it is Rock, Paper, Scissors or Nothing and store it as an input. Thanks to this, I'll be able to run the game and play it through my webcam.

In fact, after I store this input into variables, I can run the program as if I got it by digit them from keybord as we usually do in classic software.

# Set up

I've set up this code by installing its own virtual environment and, into it, installed the three packages needed as tensorflow, ipykernel and opencv-python.
Once installed them, I've also imported the machine learning model explained before and started to code the main structure of the game.

# Game Structure

As I've set up everything, I've started to code the main parts of the game's structure:

Firstly, I've assigned "Rock", "Paper", "Scissors" to the CHOICES's list and I've defined a function to let the computer randomly chosse a value.

```
from random import choice

CHOICES = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return choice(CHOICES)
```

After that, i did the same for the user by defining a function where it gets the choice from keyboard input.

```
def get_user_choice():
    return input("Pick Rock, Paper or Scissors: ").capitalize()
```

ps: I've added the capitalize() function in order to be sure that user_choice are strictly equal the the CHOICES's words.

Lately I've structured a get_winner() function with two parameters (computer_choice, user_choice) and within which there are some if/else statement to check if it's a tie or, if not, choose the winner by following the Rock, Paper, Scissor's rules.

```
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
```

Lastly, I've created a play() function where call the previous two functions to get choice and put them into get_winner() parameters in order to determine the winner.

```
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(get_winner(computer_choice, user_choice))
```
