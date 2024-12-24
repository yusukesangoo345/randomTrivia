import tkinter as tk
import random

# Trivia data
TRIVIA_LIST = [
    "ハチミツは腐らない。",
    "タコには心臓が3つある。",
    "バナナはベリーの一種だが、イチゴは違う。",
    "サメは木が存在する前から存在していた。",
    "金星の1日は金星の1年よりも長い。"
]

# Function to display random trivia
def show_random_trivia():
    trivia = random.choice(TRIVIA_LIST)
    trivia_label.config(text=trivia)

# Create the main application window
app = tk.Tk()
app.title("ランダム豆知識ジェネレーター")
app.geometry("400x200")

# UI Elements
header_label = tk.Label(app, text="ボタンをクリックしてランダムな豆知識を表示！", font=("Arial", 14))
header_label.pack(pady=10)

trivia_label = tk.Label(app, text="", font=("Arial", 12), wraplength=350, justify="center")
trivia_label.pack(pady=20)

trivia_button = tk.Button(app, text="豆知識を生成", command=show_random_trivia, font=("Arial", 12))
trivia_button.pack(pady=10)

# Run the application
app.mainloop()
