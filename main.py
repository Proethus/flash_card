import datetime
import random
from tkinter import *
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"


def learned_button_pressed():
    word = words[words.French == canvas.getvar("word")]
    word.to_csv("./data/learned_words.csv",mode="a", index=False, header=False)
    words.drop(word.index)
    get_card()


def wrong_button_pressed():
    get_card()


def get_card():
    if len(words) > 0:
        choice = random.choice(words.French)
        word = words[words.French == choice]
        canvas.itemconfig(image, image=photo_card_front)
        canvas.setvar("word", value=word.French.item())
        canvas.itemconfig(title_label, text="French")
        canvas.itemconfig(word_label, text=word.French.item())
        window.after(3000, flip_card, word.English.item())


def flip_card(word):
    canvas.itemconfig(image, image=photo_card_back)
    canvas.itemconfig(title_label, text="English")
    canvas.itemconfig(word_label, text=word)


def process_words():
    data_file = read_csv("./data/french_words.csv")
    try:
        learned_file = read_csv("./data/learned_words.csv")
    except FileNotFoundError:
        temp_data = DataFrame({"French": [], "English": []})
        temp_data.to_csv("./data/learned_words.csv", index=False)
    else:
        for item in learned_file.French.to_list():
            print(item)
            data_found = data_file[data_file.French == item]
            data_file = data_file.drop(data_found.index)
    return data_file


window = Tk()
window.minsize(width=800, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
photo_x_button = PhotoImage(file="./images/wrong.png")
photo_check_button = PhotoImage(file="./images/right.png")
photo_card_front = PhotoImage(file="./images/card_front.png")
photo_card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
image = canvas.create_image(400, 263, image=photo_card_front)
title_label = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))


button_wrong = Button(image=photo_x_button, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong_button_pressed)
button_correct = Button(image=photo_check_button, highlightthickness=0, bg=BACKGROUND_COLOR, command=learned_button_pressed)

canvas.grid(row=0, column=0, columnspan=2, sticky=NSEW)
button_wrong.grid(row=1, column=0, sticky=NSEW)
button_correct.grid(row=1, column=1, sticky=NSEW)


words = process_words()

window.after(100, get_card)

window.mainloop()
