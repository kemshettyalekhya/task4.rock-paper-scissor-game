import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Game options and logic
options = ['rock', 'paper', 'scissors']
results = {
    ('rock', 'scissors'): 'You win!',
    ('paper', 'rock'): 'You win!',
    ('scissors', 'paper'): 'You win!',
    ('scissors', 'rock'): 'Computer wins!',
    ('rock', 'paper'): 'Computer wins!',
    ('paper', 'scissors'): 'Computer wins!'
}

# Initialize scores
user_score = 0
comp_score = 0

# Game function
def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(options)
    
    user_img_label.config(image=images[user_choice])
    comp_img_label.config(image=images[comp_choice])

    if user_choice == comp_choice:
        result_label.config(text="It's a tie!", fg="orange")
    else:
        outcome = results.get((user_choice, comp_choice), 'Computer wins!')
        result_label.config(text=outcome, fg="white" if 'win' in outcome else "red")
        if 'You win' in outcome:
            user_score += 1
        elif 'Computer wins' in outcome:
            comp_score += 1

    score_label.config(text=f"You: {user_score}   Computer: {comp_score}")

# Reset game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_img_label.config(image=placeholder_img)
    comp_img_label.config(image=placeholder_img)
    result_label.config(text="")
    score_label.config(text="You: 0   Computer: 0")

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("700x500")
root.config(bg="#34495e")

# Load images
images = {
    "rock": ImageTk.PhotoImage(Image.open("download.png").resize((100, 100))),
    "paper": ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100))),
    "scissors": ImageTk.PhotoImage(Image.open("sissor.png").resize((100, 100)))
}
placeholder_img = ImageTk.PhotoImage(Image.new('RGB', (100, 100), color='#95a5a6'))

# Title
title = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="white", pady=10)
title.pack(fill="x")

# Display frame
display_frame = tk.Frame(root, bg="#34495e")
display_frame.pack(pady=20)

user_img_label = tk.Label(display_frame, image=placeholder_img, bg="#34495e")
user_img_label.grid(row=0, column=0, padx=20)

vs_label = tk.Label(display_frame, text="VS", font=("Arial", 16, "bold"), fg="white", bg="#34495e")
vs_label.grid(row=0, column=1)

comp_img_label = tk.Label(display_frame, image=placeholder_img, bg="#34495e")
comp_img_label.grid(row=0, column=2, padx=20)

# Result and score
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#34495e")
result_label.pack()

score_label = tk.Label(root, text="You: 0   Computer: 0", font=("Arial", 14), fg="white", bg="#34495e")
score_label.pack(pady=5)

# Buttons frame
buttons_frame = tk.Frame(root, bg="#2c3e50", pady=20)
buttons_frame.pack()

rock_btn = tk.Button(buttons_frame, text="Rock", font=("Arial", 12), command=lambda: play('rock'), bg="#3498db", fg="white", padx=20, pady=10)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(buttons_frame, text="Paper", font=("Arial", 12), command=lambda: play('paper'), bg="#2ecc71", fg="white", padx=20, pady=10)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(buttons_frame, text="Scissors", font=("Arial", 12), command=lambda: play('scissors'), bg="#e67e22", fg="white", padx=20, pady=10)
scissors_btn.grid(row=0, column=2, padx=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, bg="#e74c3c", fg="white", font=("Arial", 12), pady=5)
reset_btn.pack(pady=10)

root.mainloop()
