import random
import tkinter as tk
from tkinter import messagebox


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "scissors" and computer_choice == "paper") \
        or (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    
    result = get_winner(user_choice, computer_choice)
    if result == "tie":
        message = f"Both chose {user_choice}. It's a tie!"
    elif result == "user":
        user_score += 1
        message = f"You chose {user_choice}, Computer chose {computer_choice}. You win!"
    else:
        computer_score += 1
        message = f"You chose {user_choice}, Computer chose {computer_choice}. You lose!"
    
  
    label_result.config(text=message)
    label_score.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")


root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x350")
root.config(bg="#222222")

user_score = 0
computer_score = 0


tk.Label(root, text="🪨📄✂ Rock-Paper-Scissors", font=("Arial", 16, "bold"), bg="#222222", fg="white").pack(pady=10)


btn_frame = tk.Frame(root, bg="#222222")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", font=("Arial", 12, "bold"), width=10, bg="#4CAF50", fg="white",
          command=lambda: play("rock")).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Paper", font=("Arial", 12, "bold"), width=10, bg="#2196F3", fg="white",
          command=lambda: play("paper")).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Scissors", font=("Arial", 12, "bold"), width=10, bg="#FF5722", fg="white",
          command=lambda: play("scissors")).grid(row=0, column=2, padx=5)


label_result = tk.Label(root, text="", font=("Arial", 12), bg="#222222", fg="white", wraplength=350, justify="center")
label_result.pack(pady=20)

label_score = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#222222", fg="yellow")
label_score.pack(pady=10)


tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="red", fg="white", command=root.destroy).pack(pady=10)

root.mainloop()