import cv2
from keras.models import load_model
import numpy as np
import time
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
starting_time = int(time.time())
computer_wins = 0
user_wins = 0

def get_prediction(prediction):
    if prediction[0][0] > 0.8:
        return "Rock"
    elif prediction[0][1] > 0.8:
        return "Paper"
    elif prediction[0][2] > 0.8:
        return "Scissors"
    else:
        return "Nothing"
    
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

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

while True:
    if computer_wins == 3 or user_wins == 3:
        break
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
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
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


