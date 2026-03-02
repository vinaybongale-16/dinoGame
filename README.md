**Chrome Dino Bot using PyAutoGUI & Gradio**

A simple automation bot that plays the Chrome Dino Game automatically using pyautogui.
The bot is controlled using a clean Gradio UI with Start and Stop buttons.

Features:-
•Simple Gradio-based UI
•Automatic obstacle detection using pixel color
•Simulates space key press to jump
•Uses threading for smooth execution

Requirements:-
Make sure Python is installed (Python 3.8+ recommended).

Install the required libraries:
pip install pyautogui gradio


▶ How to Run:-
1. Download or clone this repository.
2. Open terminal in the project folder.
3. Run the script:
        python app.py
4. A localhost link will appear in the terminal.
5. Open the link in your browser.
6. Click Start Bot.
7. Switch to the Chrome Dino game.
8. The dinosaur will start jumping automatically.


⚙ Setup Before Running:-
1. Disconnect your internet connection (to enable offline mode).
2. Open Google Chrome.
3. Search for anything (example: abc).
4. The Chrome Dino offline game will appear.
5. Keep the Dino game visible on screen.
6. Now start the bot from the Gradio UI.


Important Notes:-
You may need to adjust the pixel coordinates:
x, y = 764, 243
Use pyautogui.position() to find the correct screen coordinates.
Make sure the Dino game window is visible and not minimized.

Technologies Used:-
•Python
•PyAutoGUI
•Gradio
•Threading
