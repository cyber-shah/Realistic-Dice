import tkinter as tk
import random
import pygame
import time

# Initialize sound
pygame.mixer.init()
ROLL_SOUND = "roll.wav"  # Dice rolling sound file (place in same folder)

# Main window
root = tk.Tk()
root.title("🎲 Realistic Dice Roller")
root.geometry("350x450")
root.configure(bg="#f0f0f0")

# Canvas for dice
canvas = tk.Canvas(root, width=200, height=200, bg="#f0f0f0", highlightthickness=0)
canvas.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
result_label.pack(pady=10)

def draw_dice(num: int):
    """Draw dice face with shading and realistic style"""
    canvas.delete("all")

    # Dice shadow
    canvas.create_rectangle(40, 40, 160, 160, outline="", fill="#d3d3d3")
    # Dice face
    canvas.create_rectangle(30, 30, 150, 150, outline="#333", width=4, fill="white")

    # Dot positions
    positions = {
        1: [(90, 90)],
        2: [(50, 50), (130, 130)],
        3: [(50, 50), (90, 90), (130, 130)],
        4: [(50, 50), (50, 130), (130, 50), (130, 130)],
        5: [(50, 50), (50, 130), (130, 50), (130, 130), (90, 90)],
        6: [(50, 50), (50, 90), (50, 130), (130, 50), (130, 90), (130, 130)],
    }

    # Draw dots
    for x, y in positions[num]:
        canvas.create_oval(x-10, y-10, x+10, y+10, fill="black")

def roll_dice():
    """Animate realistic dice rolling synced with sound"""
    result_label.config(text="")

    try:
        pygame.mixer.Sound(ROLL_SOUND).play()  # play rolling sound
    except Exception as e:
        print("Sound error:", e)

    total_animation_time = 1000  # 1 second
    rolls = 12
    delay = total_animation_time // rolls  # delay per frame

    for _ in range(rolls):
        num = random.randint(1, 6)
        draw_dice(num)
        shake_dice()
        root.update()
        root.after(delay)

    final_num = random.randint(1, 6)
    draw_dice(final_num)
    result_label.config(text=f"You rolled a {final_num}!")

def shake_dice():
    """Small shake effect for realism"""
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        canvas.move("all", dx, dy)
        root.update()
        time.sleep(0.015)
    canvas.move("all", 0, 0)

# Styled roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice,
                        font=("Helvetica", 14, "bold"),
                        bg="#4CAF50", fg="white", padx=20, pady=10,
                        activebackground="#45a049", relief="raised", bd=5)
roll_button.pack(pady=20)

root.mainloop()
