import tkinter as tk
import random
import time
from functools import partial

root = tk.Tk()
root.title("Simon Says")
root.geometry("500x550")
root.config(bg="#1e1e2f")

# Better colors with soft pastel/neon feel
color_map = {
    "red": "#ff4d4d",
    "green": "#2ecc71",
    "blue": "#3498db",
    "yellow": "#f1c40f"
}

bright_map = {
    "red": "#ff9999",
    "green": "#66ffb3",
    "blue": "#85c1ff",
    "yellow": "#ffec99"
}

sequence = []
user_sequence = []
buttons = {}

# Round label
round_label = tk.Label(root, text="Simon Says", font=("Segoe UI", 22, "bold"),
                       bg="#1e1e2f", fg="#ffffff")
round_label.pack(pady=20)

def flash(btn, color):
    btn.config(bg=bright_map[color])
    root.update()
    time.sleep(0.3)
    btn.config(bg=color_map[color])
    root.update()
    time.sleep(0.2)

def play_sequence():
    global user_sequence
    user_sequence = []
    for color in sequence:
        flash(buttons[color], color)
    enable_buttons()

def next_round():
    disable_buttons()
    round_label.config(text=f"Round {len(sequence)+1}")
    sequence.append(random.choice(list(color_map.keys())))
    root.after(1000, play_sequence)

def handle_click(color):
    user_sequence.append(color)
    flash(buttons[color], color)
    if user_sequence != sequence[:len(user_sequence)]:
        round_label.config(text="💥 Game Over! Press Start")
        disable_buttons()
        return
    if len(user_sequence) == len(sequence):
        root.after(1000, next_round)

def disable_buttons():
    for btn in buttons.values():
        btn.config(state="disabled")

def enable_buttons():
    for btn in buttons.values():
        btn.config(state="normal")

# Button grid
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=30)

for i, color in enumerate(color_map):
    btn = tk.Button(btn_frame, bg=color_map[color], activebackground=bright_map[color],
                    width=10, height=5, relief="flat", bd=0,
                    command=partial(handle_click, color))
    btn.grid(row=i//2, column=i%2, padx=20, pady=20)
    btn.config(font=("Segoe UI", 12, "bold"))
    btn.configure(highlightthickness=2, highlightbackground="#ffffff")
    buttons[color] = btn

# Start button
start_btn = tk.Button(root, text="▶ Start Game", font=("Segoe UI", 14, "bold"),
                      bg="#6c5ce7", fg="white", padx=20, pady=10,
                      activebackground="#a29bfe", command=lambda: [sequence.clear(), next_round()])
start_btn.pack(pady=20)

disable_buttons()
root.mainloop()
