import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random

def main():
    root = tk.Tk()
    root.title("Dice")

    frm_main = Frame(root)
    frm_main.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)

    setup_main(frm_main)

    # ✅ This must be root, not frame
    root.mainloop()

def setup_main(frm):
    lbl_sides = Label(frm, text="Enter the number of sides on the dice (2-20)")
    lbl_sides.grid(row=0, column=0)

    ent_side = IntEntry(frm, width=2, lower_bound=2, upper_bound=20)
    ent_side.grid(row=0, column=1, padx=3, pady=3)

    lbs_count = Label(frm, text="Enter the number of dice to roll (1-10)")
    lbs_count.grid(row=1, column=0, padx=3, pady=3)

    ent_count = IntEntry(frm, width=2, lower_bound=1, upper_bound=10)
    ent_count.grid(row=1, column=1, padx=3, pady=3)  # ✅ fixed row

    btn_roll = Button(frm, text="Roll it!")
    btn_roll.grid(row=2, column=0, padx=3, pady=3)

    lbl_roll = Label(frm, text="")
    lbl_roll.grid(row=3, column=0, padx=3, pady=3)

    def roll_dice(sides, count):
        total = 0
        roll_text = ""
        for _ in range(count):
            die_roll = random.randint(1, sides)
            total += die_roll
            roll_text += f"{die_roll} "
        roll_text += f"Total {total}"
        return roll_text

    def roll_action():
        try:
            sides = ent_side.get()
            count = ent_count.get()
        except ValueError:
            lbl_roll.config(text="Enter valid numbers!")
            return

        lbl_roll.config(text=roll_dice(sides, count))

    btn_roll.config(command=roll_action)

# ✅ 
main()
