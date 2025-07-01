# Hand Gesture Rock-Paper-Scissors Game

This project implements a classic Rock-Paper-Scissors game that you can play against an AI using real-time hand gestures. It leverages computer vision techniques with OpenCV and `cvzone` to detect your hand movements and determine your chosen move (Rock, Paper, or Scissors).

## Features

* **Real-time Hand Gesture Recognition:** Detects your hand and determines your move based on the number of fingers extended:
    * **Rock:** All fingers down (fist).
    * **Paper:** All fingers up (open palm).
    * **Scissors:** Index and middle fingers up.
* **AI Opponent:** Plays against a random AI opponent.
* **Countdown Timer:** A 3-second countdown before each round's result is displayed, allowing players to prepare their move.
* **Score Tracking:** Keeps track of scores for both the AI and the player.
* **Visual Game Interface:** Overlays the live webcam feed onto a custom game background, displaying player and AI moves, countdown, and scores.
* **Easy Restart:** Quickly restart a new round by pressing a key.

## Prerequisites

* Python (3.x recommended).
* A webcam connected to your computer.
* **Game Assets:** Ensure you have the `Resources` folder containing `BG.png`, `1.png`, `2.png`, and `3.png` in the same directory as `main.py`.

## Installation

1.  **Clone or Download the Repository:**
    Get the project files to your local machine.

2.  **Install Required Libraries:**
    Open your terminal or command prompt, navigate to the project directory, and run the following commands:
    ```bash
    pip install opencv-python numpy cvzone
    ```
    * Ensure `HandTrackingModule.py` is in the same directory as `main.py` or accessible in your Python path.

## Usage

1.  **Run the Script:**
    Open your terminal or command prompt, navigate to the project directory, and execute:
    ```bash
    python main.py
    ```
2.  **Start the Game:**
    * A window will open displaying your webcam feed integrated into a game background.
    * Press the `S` key on your keyboard to start a new round.
3.  **Play a Round:**
    * After pressing `S`, a 3-second countdown will begin.
    * During the countdown, make your Rock, Paper, or Scissors hand gesture in front of the webcam.
    * Once the countdown ends, your detected move and the AI's random move will be displayed on screen.
    * The score will be updated on the scoreboard (AI's score on the left, Player's score on the right).
4.  **Continue/Restart:**
    * To play another round, simply press `S` again.
5.  **Exit:** Press the `Q` key on your keyboard to close the application window.

## How It Works

1.  **Webcam & Hand Tracking:**
    * The webcam captures live video frames.
    * `cvzone.HandDetector` detects a single hand in each frame.
2.  **Image Integration:**
    * The live webcam feed (scaled and cropped) is dynamically placed onto a pre-designed `BG.png` image to form the main game interface.
3.  **Game Logic & Timer:**
    * The game is driven by a `startGame` flag, toggled by the 'S' key.
    * A `timer` manages a 3-second countdown for each round.
    * Once the timer expires, `stateResult` is set to `True`, triggering the result display.
4.  **Player Move Detection:**
    * When the countdown finishes, the `detector.fingersUp(hand)` method is used to determine the number of extended fingers.
    * **0 fingers** (fist) is mapped to **Rock (1)**.
    * **5 fingers** (open palm) is mapped to **Paper (2)**.
    * **2 fingers** (index and middle) is mapped to **Scissors (3)**.
5.  **AI Move & Winner Determination:**
    * The AI's move is randomly generated (1, 2, or 3).
    * Standard Rock-Paper-Scissors rules are applied to compare the player's move against the AI's move, and scores are updated accordingly.
    * The AI's move is displayed using pre-loaded images (`1.png`, `2.png`, `3.png`).
6.  **Scoreboard:** The current scores for the AI and the player are continuously displayed on the background image.

## Customization

* **Camera Resolution:** Adjust `cap.set(3, 640)` and `cap.set(4, 480)` for different webcam resolutions.
* **Hand Detection Confidence:** Modify `detector = HandDetector(maxHands=1, detectionCon=0.8)` to fine-tune hand detection sensitivity.
* **Countdown Duration:** Change the `if timer > 3` condition to adjust the round countdown time.
* **Gesture Mapping:** If you want to change which finger count corresponds to Rock, Paper, or Scissors, modify the `if sum(fingers) == ...` conditions.
* **Game Assets:** Replace the images in the `Resources` folder (`BG.png`, `1.png`, `2.png`, `3.png`) with your own custom designs. Ensure your AI move images are named `1.png`, `2.png`, `3.png`.
* **Scoreboard Position:** Adjust the coordinates in `cv2.putText` for displaying scores to fit your `BG.png`.

## Troubleshooting

* **"Unable to capture camera image!":** Verify your webcam is connected, not being used by another application, and its drivers are up-to-date. Try restarting the script or your computer.
* **No hand detection:** Ensure good lighting conditions and that your hand is clearly visible to the camera. Adjust `detectionCon` if necessary.
* **Incorrect move detection:** Ensure your hand gestures are clear and distinct. Experiment with the `sum(fingers)` values if the detection is unreliable.
* **Image not loading:** Ensure all image files (`BG.png`, `1.png`, etc.) are correctly placed in the `Resources` folder relative to your script.
