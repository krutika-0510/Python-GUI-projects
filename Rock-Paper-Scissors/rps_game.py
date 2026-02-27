import tkinter as tk
import random

# ==============================
# ROCK PAPER SCISSORS - INSTANT
# ==============================

user_score = 0
computer_score = 0
win_streak = 0

choices = ["Rock", "Paper", "Scissors"]

# ---------- GAME LOGIC ----------

def play(user_choice):
    global user_score, computer_score, win_streak

    computer_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
        result_label.config(fg="orange")
        win_streak = 0

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):

        result = "You Win! 🎉"
        result_label.config(fg="green")
        user_score += 1
        win_streak += 1

    else:
        result = "You Lose! 😢"
        result_label.config(fg="red")
        computer_score += 1
        win_streak = 0

    result_label.config(text=result)

    score_label.config(
        text=f"Score  You: {user_score}  |  Computer: {computer_score}"
    )

    streak_label.config(text=f"🔥 Winning Streak: {win_streak}")


def reset_game():
    global user_score, computer_score, win_streak
    user_score = 0
    computer_score = 0
    win_streak = 0

    result_label.config(text="")
    user_label.config(text="")
    computer_label.config(text="")
    score_label.config(text="Score  You: 0  |  Computer: 0")
    streak_label.config(text="🔥 Winning Streak: 0")


# ---------- WINDOW ----------

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("520x550")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Title
tk.Label(root, text="🎮 Rock Paper Scissors",
         font=("Arial", 20, "bold"),
         bg="#1e1e2f", fg="cyan").pack(pady=20)

tk.Label(root, text="Choose your move",
         font=("Arial", 12),
         bg="#1e1e2f", fg="white").pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=20)

tk.Button(button_frame, text="🪨 Rock",
          width=12, height=2,
          font=("Arial", 12),
          command=lambda: play("Rock")).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="📄 Paper",
          width=12, height=2,
          font=("Arial", 12),
          command=lambda: play("Paper")).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="✂ Scissors",
          width=12, height=2,
          font=("Arial", 12),
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Display Labels
user_label = tk.Label(root, text="",
                      font=("Arial", 12),
                      bg="#1e1e2f", fg="white")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="",
                          font=("Arial", 12),
                          bg="#1e1e2f", fg="white")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="",
                        font=("Arial", 18, "bold"),
                        bg="#1e1e2f")
result_label.pack(pady=20)

score_label = tk.Label(root,
                       text="Score  You: 0  |  Computer: 0",
                       font=("Arial", 12),
                       bg="#1e1e2f", fg="yellow")
score_label.pack(pady=10)

streak_label = tk.Label(root,
                        text="🔥 Winning Streak: 0",
                        font=("Arial", 12, "bold"),
                        bg="#1e1e2f", fg="orange")
streak_label.pack(pady=5)

# Reset Button
tk.Button(root, text="🔄 Reset Game",
          command=reset_game,
          font=("Arial", 12)).pack(pady=20)

root.mainloop()
