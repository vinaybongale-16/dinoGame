import pyautogui
import time
import threading
import gradio as gr

running = False

def dino_bot():
    global running
    time.sleep(5)  # Time to switch to Chrome

    while running:
        x, y = 764, 243
        pixel_color = pyautogui.pixel(x, y)

        if pixel_color != (255, 255, 255):
            pyautogui.press("space")

def start_bot():
    global running
    running = True
    threading.Thread(target=dino_bot).start()
    return "Bot Started! Switch to Chrome."

def stop_bot():
    global running
    running = False
    return "Bot Stopped."

with gr.Blocks() as demo:
    gr.Markdown("## Chrome Dino Bot Controller")
    start_btn = gr.Button("Start Bot")
    stop_btn = gr.Button("Stop Bot")
    output = gr.Textbox()

    start_btn.click(start_bot, outputs=output)
    stop_btn.click(stop_bot, outputs=output)

demo.launch(share=True)