import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

clicked = True
count = 0
buttons = []

def disable_all_buttons():
    for button in buttons:
        button.config(state="disabled")

def check_winner():
    global winner
    winner = False

    # Check rows
    for row in range(0, 9, 3):
        if buttons[row]['text'] == buttons[row+1]['text'] == buttons[row+2]['text'] != " ":
            buttons[row].config(bg="green")
            buttons[row+1].config(bg="green")
            buttons[row+2].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"{buttons[row]['text']} wins!")
            disable_all_buttons()

    # Check columns
    for col in range(3):
        if buttons[col]['text'] == buttons[col+3]['text'] == buttons[col+6]['text'] != " ":
            buttons[col].config(bg="green")
            buttons[col+3].config(bg="green")
            buttons[col+6].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"{buttons[col]['text']} wins!")
            disable_all_buttons()

    # Check diagonals
    if buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != " ":
        buttons[0].config(bg="green")
        buttons[4].config(bg="green")
        buttons[8].config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", f"{buttons[0]['text']} wins!")
        disable_all_buttons()

    if buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != " ":
        buttons[2].config(bg="green")
        buttons[4].config(bg="green")
        buttons[6].config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", f"{buttons[2]['text']} wins!")
        disable_all_buttons()

    # Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
        disable_all_buttons()

def button_click(button):
    global clicked, count

    if button['text'] == " " and clicked:
        button['text'] = "X"
        clicked = False
        count += 1
        check_winner()
    elif button['text'] == " " and not clicked:
        button['text'] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Tic-Tac-Toe", "This box has already been selected!")

def reset_game():
    global clicked, count, buttons
    clicked = True
    count = 0

    for i in range(9):
        buttons[i].config(text=" ", bg="SystemButtonFace", state="normal")

# Create buttons
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda b=i: button_click(buttons[b]))
    button.grid(row=i//3, column=i % 3)
    buttons.append(button)

menu = tk.Menu(root)
root.config(menu=menu)
options_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset_game)

root.mainloop()
