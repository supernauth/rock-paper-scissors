import tkinter as tk
from tkinter import messagebox
import random

class KoPapirOllo:
    def __init__(self, master):
        self.master = master
        master.title("Kő Papír Olló")

        self.main_label = tk.Label(master, text="Válassz: Kő, papír vagy olló?")
        self.main_label.config(font=("Verdana", 15, "bold"))
        self.result_text = tk.StringVar()
        
        self.ko_kep = tk.PhotoImage(file='ko.png')
        self.papir_kep = tk.PhotoImage(file='papir.png')
        self.ollo_kep = tk.PhotoImage(file='ollo.png')

        self.Kő = tk.Button(master, image=self.ko_kep, command=lambda: self.play("Kő"))
        self.Papír = tk.Button(master, image=self.papir_kep, command=lambda: self.play("Papír"))
        self.Olló = tk.Button(master, image=self.ollo_kep, command=lambda: self.play("Olló"))

        self.user_points = 0
        self.computer_points = 0
        self.points_label = tk.Label(master, text="Pontszám: 0 - 0")
        self.points_label.config(font=("Verdana", 13))

        self.main_label.grid(row=1, column=0, columnspan=3, padx=30, pady=10)
        self.points_label.grid(row=2, column=0, columnspan=3, pady=10)
        self.Kő.grid(row=3, column=0, padx=10, pady=10)
        self.Papír.grid(row=3, column=1, padx=10, pady=10)
        self.Olló.grid(row=3, column=2, padx=10, pady=10)
        
    def play(self, user_choice):
        choices = ["Kő", "Papír", "Olló"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        result_text = f"Választásod: {user_choice}.\nA gép választása: {computer_choice}.\nEredmény: {result}"
        self.result_text.set(result_text)
        messagebox.showinfo("Eredmény", result_text)

        if result == "Nyertél.":
            self.user_points += 1
        elif result == "A gép nyert.":
            self.computer_points += 1

        self.points_label.config(text=f"Pontszám: {self.user_points} - {self.computer_points}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Döntetlen!"
        elif (
            (user_choice == "Kő" and computer_choice == "Olló") or
            (user_choice == "Papír" and computer_choice == "Kő") or
            (user_choice == "Olló" and computer_choice == "Papír")
        ):
            return "Nyertél."
        else:
            return "A gép nyert."

if __name__ == '__main__':
    root = tk.Tk()
    app = KoPapirOllo(root)

    root.mainloop()
