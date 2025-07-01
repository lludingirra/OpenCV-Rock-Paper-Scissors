import time # Import the time module for managing game timing.
import random # Import the random module for generating AI's move.
import cv2 # Import the OpenCV library for image and video processing.
import cvzone # Import cvzone for helper functions like image overlay and hand detection.
from cvzone.HandTrackingModule import HandDetector # Import HandDetector for hand detection and tracking.

# --- Webcam Initialization ---
cap = cv2.VideoCapture(0) # Initialize video capture from the default webcam (index 0).
cap.set(3, 640) # Set the width of the captured video frame to 640 pixels.
cap.set(4, 480) # Set the height of the captured video frame to 480 pixels.

# --- Hand Detector Initialization ---
detector = HandDetector(maxHands=1) # Initialize HandDetector to detect a maximum of one hand.

# --- Game State Variables ---
timer = 0 # Countdown timer before displaying results.
stateResult = False # Flag to control when to display game results.
startGame = False # Flag to indicate if the game has started.
initialTime = None # Stores the time when a round begins.
scores = [0, 0] # Stores scores: [AI_score, Player_score].

# --- Main Game Loop ---
while True:
    # Load the background image for the game interface.
    # This image should be in a 'Resources' folder.
    imgBG = cv2.imread("Resources/BG.png")
    
    success, img = cap.read() # Read a frame from the webcam.
    
    # Scale and crop the webcam image to fit into the game's background.
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480] # Crop to specific columns to fit the player's view.
    
    # Detect hands in the scaled webcam image.
    hands, img = detector.findHands(imgScaled)
    
    if startGame: # Only proceed with game logic if 's' key has been pressed to start.
        
        if not stateResult: # If results are not yet displayed (during countdown phase).
            timer = time.time() - initialTime # Calculate elapsed time since round started.
            # Display the countdown timer on the background image.
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (0, 0, 255), 4)
            
            if timer > 3: # After 3 seconds countdown.
                stateResult = True # Set flag to display results.
                timer = 0 # Reset timer for next round.
                
                if hands: # If a hand is detected when the timer runs out.
                    playerMove = None # Initialize player's move.
                    hand = hands[0] # Get the first detected hand.
                    fingers = detector.fingersUp(hand) # Get the status of each finger (up/down).
                    
                    # Determine player's move based on finger count.
                    if sum(fingers) == 0: # All fingers down (fist) -> Rock.
                        playerMove = 1
                        
                    if sum(fingers) == 5: # All fingers up (open palm) -> Paper.
                        playerMove = 2
                        
                    if sum(fingers) == 2: # Index and middle fingers up -> Scissors.
                        playerMove = 3
                        
                    # AI's random move.
                    randomNumber = random.randint(1, 3) # 1: Rock, 2: Paper, 3: Scissors.
                    # Load AI's move image.
                    imgAI = cv2.imread(f"Resources/{randomNumber}.png", cv2.IMREAD_UNCHANGED)
                    # Overlay AI's move image onto the background.
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                        
                    # --- Determine Winner and Update Scores ---
                    # Player wins conditions (Rock vs Scissors, Paper vs Rock, Scissors vs Paper).
                    if (playerMove == 1 and randomNumber == 3) or \
                       (playerMove == 2 and randomNumber == 1) or \
                       (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1 # Increment player's score.
                            
                    # AI wins conditions (Scissors vs Rock, Rock vs Paper, Paper vs Scissors).
                    if (playerMove == 3 and randomNumber == 1) or \
                       (playerMove == 1 and randomNumber == 2) or \
                       (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1 # Increment AI's score.
                        
    # Overlay the scaled webcam image (player's view) onto the designated area of the background.
    # The coordinates (234:654, 795:1195) are fixed positions on the BG.
    imgBG[234:654, 795:1195] = imgScaled
    
    if stateResult: # If results are being displayed.
        # Ensure AI's move image is displayed continuously until next round.
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    # Display AI's score on the background image.
    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    # Display player's score on the background image.
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("Image", imgBG) # Display the final game image.
    key = cv2.waitKey(1) # Wait for 1ms for a key press.
    
    if key == ord('s'): # If 's' key is pressed, start a new round.
        startGame = True # Set game start flag.
        initialTime = time.time() # Record start time for countdown.
        stateResult = False # Reset result display flag.
        
    elif key == ord('q'): # If 'q' key is pressed, break the loop and exit the game.
        break

# Release webcam resources and close all OpenCV windows.
cap.release()
cv2.destroyAllWindows()