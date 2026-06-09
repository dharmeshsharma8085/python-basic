from random import shuffle, randint

# --- Wallet / Payment system ---
wallet_balance = 0

def add_money():
    """Simulate adding money via UPI or wallet"""
    global wallet_balance
    while True:
        amt = input("Enter amount to add to your wallet (₹): ")
        if amt.isdigit() and int(amt) > 0:
            wallet_balance += int(amt)
            print(f"✅ ₹{amt} added to your wallet. Current balance: ₹{wallet_balance}")
            break
        print("❌ Invalid amount. Try again.")

def check_balance():
    print(f"💰 Current wallet balance: ₹{wallet_balance}")

# --- Game functions ---
def setup_game(num_cups):
    cups = [""] * num_cups
    ball_position = randint(0, num_cups - 1)
    cups[ball_position] = "🥎"
    return cups

def shuffle_cups(cups):
    shuffle(cups)
    return cups

def player_guess(num_cups):
    while True:
        guess = input(f"Pick a cup (0 to {num_cups-1}): ")
        if guess.isdigit() and 0 <= int(guess) < num_cups:
            return int(guess)
        print("❌ Invalid input. Try again.")

def place_bet(balance):
    while True:
        bet = input(f"You have ₹{balance}. Enter your bet: ₹")
        if bet.isdigit() and 0 < int(bet) <= balance:
            return int(bet)
        print("❌ Invalid bet amount.")

def play_round(balance):
    print("\n🔥 High Stakes Round! One chance only!")
    print("Choose your risk:")
    print("1️⃣ 2x Money (5 cups → easier)")
    print("2️⃣ 5x Money (10 cups → harder)")

    while True:
        choice = input("Enter 1 for 2x or 2 for 5x: ")
        if choice in ["1","2"]:
            break
        print("❌ Invalid choice. Try again.")

    num_cups = 5 if choice=="1" else 10
    multiplier = 2 if choice=="1" else 5

    cups = setup_game(num_cups)
    cups = shuffle_cups(cups)

    bet = place_bet(balance)
    guess = player_guess(num_cups)

    print("\nShuffling cups... 🌀🌀🌀")

    if cups[guess] == "🥎":
        winnings = bet * multiplier
        balance += winnings
        print(f"🎉 JACKPOT! You found the ball and won ₹{winnings}!")
    else:
        balance -= bet
        print("💀 Sorry! No ball under that cup. You lost your bet.")

    print("Cups were:", cups)
    print(f"Your new balance: ₹{balance}")
    return balance

def shell_wallet_game():
    global wallet_balance
    print("🎯 Welcome to the High-Stakes Shell Game with Wallet!")
    
    # Add initial money to wallet
    add_money()
    balance = wallet_balance
    round_number = 0

    while balance > 0:
        round_number += 1
        print(f"\n--- Round {round_number} ---")
        balance = play_round(balance)

        if balance <= 0:
            print("💸 You ran out of money! Game over.")
            wallet_balance = 0
            break

        # Update wallet
        wallet_balance = balance

        cont = input("\nDo you want to play another round? (y/n): ").lower()
        if cont != "y":
            print(f"Thanks for playing! Wallet balance: ₹{wallet_balance}")
            break

# Start the game
shell_wallet_game()
