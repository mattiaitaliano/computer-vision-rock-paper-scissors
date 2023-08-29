# Computer Vision RPS: Play Rock, Paper, Scissors with Your Webcam

Play rock, paper, scissors against your computer using your webcam. 

<img src="https://blog.eduonix.com/wp-content/uploads/2019/10/CVT1.jpeg" alt="Image Alt Text" width="300">

## Overview

This Python program uses computer vision and machine learning to recognize hand signs for rock, paper, and scissors, allowing you to play the game in a interactive way.

## Model and How to Use It

The project uses a Keras model ([teachlabmachine](https://teachablemachine.withgoogle.com/ )) trained to recognize four different hand signs: Rock, Paper, Scissors, and Nothing. The webcam captures the hand sign you make, and the program recognizes it as one of the four categories. This input is then stored in variables, allowing the game to proceed.

## Set Up

1. Create a virtual environment.
2. Install the required packages:
- TensorFlow
- OpenCV-Python
3. Import the Keras model.

## Code Structure

### Importing Libraries and Loading Model

```
import cv2
from keras.models import load_model
import numpy as np
import time
import random

model = load_model('keras_model.h5')
```

### Initializing Variables

```
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
starting_time = int(time.time())
computer_wins = 0
user_wins = 0
Get Prediction Function
python
Copy code
def get_prediction(prediction):
    if prediction[0][0] > 0.8:
        return "Rock"
    elif prediction[0][1] > 0.8:
        return "Paper"
    elif prediction[0][2] > 0.8:
        return "Scissors"
    else:
        return "Nothing"
```

### Computer's Choice Function

```
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])
```

### Winner Determination Function

```
def get_winner(computer_choice, user_choice):
    global computer_wins, user_wins
    if computer_choice == user_choice:
        print('It is a tie!')
    elif computer_choice == 'Rock' and user_choice == 'Paper':
        print('You won!')
        user_wins += 1
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        print('You won!')
        user_wins += 1
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        print('You won!')
        user_wins += 1
    else:
        print('You lost')
        computer_wins += 1
```

### Main Loop

```
while True:
    if computer_wins == 3 or user_wins == 3:
        break
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    current_time = int(time.time())
    if current_time == starting_time+5:
        computer_choice = get_computer_choice()
        user_choice = get_prediction(prediction)
        get_winner(computer_choice, user_choice)
        print(computer_wins,user_wins)
        starting_time = int(time.time())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("END.")
cap.release()
cv2.destroyAllWindows()
```

## How to Play

1. Run the program.
2. Make a hand sign in front of the webcam.
3. The computer will make its choice, and the winner will be announced.
