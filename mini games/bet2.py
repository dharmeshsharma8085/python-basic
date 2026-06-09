import tkinter as tk
from PIL import Image, ImageTk
import random
import threading
import time
import winsound

# ---------- GLOBAL VARIABLES ----------
wallet_balance = 0
balance = 0
num_cups = 5
multiplier = 2
cups = []
ball_position = 0
win_streak = 0
cup_widgets = []

# ---------- UTILITY FUNCTIONS ----------
def play_sound(file):
    threading.Thread(target=lambda: winsound.PlaySound(file, winsound.SND_FILENAME)).start()

# ---------- WALLET FUNCTIONS ----------
def add_money():
    global wallet_balance, balance
    amt = entry_deposit.get()
    if amt.isdigit() and int(amt) > 0:
        wallet_balance += int(amt)
        balance = wallet_balance
        lbl_wallet.config(text=f"Wallet Balance: ₹{wallet_balance}")
        entry_deposit.delete(0, tk.END)
        tk.messagebox.showinfo("Wallet", f"✅ ₹{amt} added!")
    else:
        tk.messagebox.showerror("Error", "Enter valid amount!")

# ---------- GAME FUNCTIONS ----------
def setup_game(num_cups_):
    global cups, ball_position
    cups = [""] * num_cups_
    ball_position = random.randint(0, num_cups_-1)
    cups[ball_position] = "🥎"

def place_bet():
    bet_amt = entry_bet.get()
    if not bet_amt.isdigit() or int(bet_amt) <= 0 or int(bet_amt) > balance:
        tk.messagebox.showerror("Error", "Enter valid bet!")
        return None
    return int(bet_amt)

def start_round(option):
    global num_cups, multiplier, cup_widgets
    if balance <= 0:
        tk.messagebox.showinfo("Game Over", "No balance left!")
        return
    option = int(option)
    num_cups = 5 if option == 1 else 10
    multiplier = 2 if option == 1 else 5

    setup_game(num_cups)

    # Clear previous cups
    for widget in frame_cups.winfo_children():
        widget.destroy()
    cup_widgets.clear()

    # Create cup labels
    spacing = 80
    start_x = 50
    for i in range(num_cups):
        lbl = tk.Label(frame_cups, image=cup_img, bg="#222")
        lbl.place(x=start_x + i*spacing, y=50)
        cup_widgets.append(lbl)

    lbl_status.config(text="Shuffling cups... 🌀")
    play_sound("shuffle.wav")
    threading.Thread(target=shuffle_animation).start()

def shuffle_animation():
    global cup_widgets
    spacing = 80
    start_x = 50
    for _ in range(20):  # shuffle 20 times
        positions = list(range(len(cup_widgets)))
        random.shuffle(positions)
        for i, lbl in enumerate(cup_widgets):
            target_x = start_x + positions[i]*spacing
            threading.Thread(target=animate_move, args=(lbl, target_x, 50)).start()
        time.sleep(0.3)
    # Enable clicks
    time.sleep(0.7)
    for idx, lbl in enumerate(cup_widgets):
        lbl.bind("<Button-1>", lambda e, i=idx: guess_cup(i))
    lbl_status.config(text="Pick a cup! One chance only!")

def animate_move(widget, target_x, y):
    x = widget.winfo_x()
    steps = 10
    dx = (target_x - x)/steps
    for _ in range(steps):
        widget.place(x=widget.winfo_x()+dx, y=y)
        time.sleep(0.03)
    widget.place(x=target_x, y=y)

def guess_cup(idx):
    global balance, wallet_balance, win_streak
    bet_amt = place_bet()
    if bet_amt is None:
        return

    # Disable clicks
    for lbl in cup_widgets:
        lbl.unbind("<Button-1>")

    def reveal():
        time.sleep(0.5)
        for i, lbl in enumerate(cup_widgets):
            if i == idx:
                if cups[i] == "🥎":
                    lbl.config(image=ball_img)
                else:
                    lbl.config(bg="red")
            else:
                lbl.config(image=cup_img)
        global balance, wallet_balance, win_streak
        if cups[idx] == "🥎":
            win_streak += 1
            bonus = 1 + 0.1*win_streak
            winnings = int(bet_amt*multiplier*bonus)
            balance += winnings
            wallet_balance = balance
            lbl_wallet.config(text=f"Wallet Balance: ₹{wallet_balance}")
            play_sound("win.wav")
            tk.messagebox.showinfo("WIN!", f"🎉 You won ₹{winnings}!\nStreak Bonus x{bonus:.1f}")
        else:
            balance -= bet_amt
            wallet_balance = balance
            lbl_wallet.config(text=f"Wallet Balance: ₹{wallet_balance}")
            win_streak = 0
            play_sound("lose.wav")
            tk.messagebox.showinfo("LOSS", "💀 You lost your bet!")
        lbl_status.config(text="Round over! Choose risk to play again.")

    threading.Thread(target=reveal).start()

# ---------- GUI SETUP ----------
root = tk.Tk()
root.title("🎰 Cinematic Shell Betting Game")
root.geometry("1200x500")

# Load images
cup_image = Image.open("cup.png").resize((60,60))
cup_img = ImageTk.PhotoImage(cup_image)
ball_image = Image.open("ball.png").resize((60,60))
ball_img = ImageTk.PhotoImage(ball_image)
background_image = Image.open("background.png").resize((1200,500))
bg_img = ImageTk.PhotoImage(background_image)
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

# Wallet
frame_wallet = tk.Frame(root, bg="#222")
frame_wallet.pack(pady=10)
lbl_wallet = tk.Label(frame_wallet, text=f"Wallet Balance: ₹{wallet_balance}", font=("Arial",14), fg="yellow", bg="#222")
lbl_wallet.pack(side=tk.LEFT, padx=10)
entry_deposit = tk.Entry(frame_wallet)
entry_deposit.pack(side=tk.LEFT, padx=5)
btn_add = tk.Button(frame_wallet, text="Add Money", command=add_money)
btn_add.pack(side=tk.LEFT, padx=5)

# Bet
frame_bet = tk.Frame(root, bg="#222")
frame_bet.pack(pady=10)
tk.Label(frame_bet, text="Enter Bet Amount: ₹", bg="#222", fg="white").pack(side=tk.LEFT)
entry_bet = tk.Entry(frame_bet)
entry_bet.pack(side=tk.LEFT, padx=5)

# Risk options
frame_risk = tk.Frame(root, bg="#222")
frame_risk.pack(pady=10)
tk.Label(frame_risk, text="Choose Risk:", bg="#222", fg="white").pack(side=tk.LEFT, padx=5)
btn_risk1 = tk.Button(frame_risk, text="2x Money (5 cups)", command=lambda: start_round(1))
btn_risk1.pack(side=tk.LEFT, padx=5)
btn_risk2 = tk.Button(frame_risk, text="5x Money (10 cups)", command=lambda: start_round(2))
btn_risk2.pack(side=tk.LEFT, padx=5)

# Cups Frame
frame_cups = tk.Frame(root, width=1200, height=200, bg="#222")
frame_cups.pack(pady=20)

# Status
lbl_status = tk.Label(root, text="Welcome! Add money and choose risk to start.", font=("Arial",12), bg="#222", fg="white")
lbl_status.pack(pady=10)

root.mainloop()
