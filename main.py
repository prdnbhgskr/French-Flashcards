from tkinter import *
import random

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_word_dict = {}
french_words = {}

# --------------- READ WORDS ------------------ #

try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_df = pd.read_csv('data/french_words.csv')
    french_words = original_df.to_dict(orient="records")
else:
    french_words = df.to_dict(orient="records")

# --------------- PICK WORDS ------------------ #

def pick_words():
    global random_word_dict

    canvas.itemconfig(canvas_image, image=card_front_img)

    random_word_dict = random.choice(french_words)

    random_french = random_word_dict["French"]
    english_equivalent = random_word_dict["English"]

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_french, fill="black")
    canvas.itemconfig(counter, text=f"Remaining words: {len(french_words)}", fill="black")

    # Flip
    window.after(3000, lambda: flip(english_equivalent))

# --------------- FLIP --------------------- #

def flip(english):
    # Change the canvas image
    canvas.itemconfig(canvas_image, image=card_back_img)

    # Change the words color & contents
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english , fill="white")
    canvas.itemconfig(counter, text=f"Remaining words: {len(french_words)}", fill="white")

# ---------------- REMOVE KNOWN WORDS ------------------- #

def is_known():
    french_words.remove(random_word_dict)
    data = pandas.DataFrame(french_words)
    data.to_csv("data/words_to_learn.csv", index=False)

    pick_words()

# --------------- UI SETUP ----------------- #

window = Tk()
window.title("FLASH")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Flash Card
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
counter = canvas.create_text(680, 30, text="Hi I'm counter")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_words)
wrong_button.grid(row=1, column=0)


pick_words()

window.mainloop()