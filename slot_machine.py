import random

# Constants
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

# Symbols in each wheel
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


# Win if they get all the same symbols in a row
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount


def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        bet = input(f"Enter your bet (min: ${MIN_BET}, max: ${MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number")
    return bet


def game(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    print(f"Your remaining balance is: ${balance - total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return balance - total_bet + winnings


def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        spin = input("Press Enter to play (q to quit).")
        if spin == 'q':
            break
        balance = game(balance)
    print(f"You left with ${balance}.")


main()


# import random

# class SlotMachine:
#     MAX_LINES = 3
#     MAX_BET = 1000
#     MIN_BET = 10
#     ROWS = 3
#     COLS = 3

#     # Frequency of symbols on the wheels
#     symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
#     # Value of each symbol when calculating wins
#     symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self):
#         while True:
#             amount = input("Enter the amount to deposit: $")
#             try:
#                 amount = int(amount)
#                 if amount > 0:
#                     self.balance += amount
#                     break
#                 else:
#                     print("Amount must be greater than 0.")
#             except ValueError:
#                 print("Please enter a valid number.")
#         print(f"New balance: ${self.balance}")

#     def get_no_of_lines(self):
#         while True:
#             lines = input("Enter the number of lines to bet on (1 - " + str(self.MAX_LINES) + "): ")
#             try:
#                 lines = int(lines)
#                 if 1 <= lines <= self.MAX_LINES:
#                     return lines
#                 else:
#                     print("Enter a valid number of lines.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     def get_bet(self):
#         while True:
#             bet = input(f"Enter your bet per line (min: ${self.MIN_BET}, max: ${self.MAX_BET}): $")
#             try:
#                 bet = int(bet)
#                 if self.MIN_BET <= bet <= self.MAX_BET:
#                     return bet
#                 else:
#                     print(f"Bet must be between ${self.MIN_BET} and ${self.MAX_BET}.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     def get_slot_machine_spin(self):
#         # Build a list with symbols weighted by their counts
#         all_symbols = []
#         for symbol, count in self.symbol_count.items():
#             all_symbols.extend([symbol] * count)

#         columns = []
#         for _ in range(self.COLS):
#             column = []
#             current_symbols = all_symbols[:]  # Copy the list to preserve original weights for each column
#             for _ in range(self.ROWS):
#                 value = random.choice(current_symbols)
#                 current_symbols.remove(value)
#                 column.append(value)
#             columns.append(column)
#         return columns

#     def print_slot_machine(self, columns):
#         print("\nSlot Machine Spin:")
#         for row in range(self.ROWS):
#             row_symbols = []
#             for col in range(self.COLS):
#                 row_symbols.append(columns[col][row])
#             print(" | ".join(row_symbols))
#         print()

#     def check_winnings(self, columns, lines, bet):
#         winnings = 0
#         winning_lines = []

#         # Check horizontal (row) wins
#         for line in range(lines):
#             symbol = columns[0][line]
#             for column in columns:
#                 if column[line] != symbol:
#                     break
#             else:
#                 win_amount = self.symbol_value[symbol] * bet
#                 winnings += win_amount
#                 winning_lines.append(f"Row {line+1} win (${win_amount})")

#         # If the player bets on all lines, check for diagonal wins
#         if lines == self.ROWS:
#             # Main diagonal: positions (0,0), (1,1), (2,2)
#             diag_symbol = columns[0][0]
#             for i in range(self.ROWS):
#                 if columns[i][i] != diag_symbol:
#                     break
#             else:
#                 win_amount = int(self.symbol_value[diag_symbol] * bet * 1.5)
#                 winnings += win_amount
#                 winning_lines.append(f"Main Diagonal win (${win_amount})")

#             # Anti-diagonal: positions (0,2), (1,1), (2,0)
#             anti_diag_symbol = columns[0][self.ROWS - 1]
#             for i in range(self.ROWS):
#                 if columns[i][self.ROWS - 1 - i] != anti_diag_symbol:
#                     break
#             else:
#                 win_amount = int(self.symbol_value[anti_diag_symbol] * bet * 1.5)
#                 winnings += win_amount
#                 winning_lines.append(f"Anti Diagonal win (${win_amount})")

#         # Bonus: If the entire board shows the same symbol, award an extra bonus
#         first_symbol = columns[0][0]
#         bonus = True
#         for col in columns:
#             for sym in col:
#                 if sym != first_symbol:
#                     bonus = False
#                     break
#             if not bonus:
#                 break
#         if bonus:
#             bonus_amount = 10 * bet  # Arbitrary bonus multiplier
#             winnings += bonus_amount
#             winning_lines.append(f"Full Board Bonus (${bonus_amount})")

#         return winnings, winning_lines

#     def play_round(self):
#         print(f"\nCurrent balance: ${self.balance}")
#         lines = self.get_no_of_lines()

#         while True:
#             bet = self.get_bet()
#             total_bet = bet * lines

#             if total_bet > self.balance:
#                 print(f"Insufficient funds. Your balance: ${self.balance}, total bet: ${total_bet}")
#             else:
#                 break

#         self.balance -= total_bet
#         print(f"You are betting ${bet} on {lines} line(s). Total bet: ${total_bet}.")
#         print(f"Remaining balance: ${self.balance}")

#         slots = self.get_slot_machine_spin()
#         self.print_slot_machine(slots)

#         winnings, winning_lines = self.check_winnings(slots, lines, bet)
#         print("Winning Details:")
#         if winning_lines:
#             for win in winning_lines:
#                 print("  " + win)
#         else:
#             print("  No wins this round.")

#         print(f"You won: ${winnings}\n")
#         self.balance += winnings

#     def start_game(self):
#         print("Welcome to the Enhanced Slot Machine Game!")
#         self.deposit()

#         while True:
#             choice = input("Press Enter to play, 'd' to deposit more, or 'q' to quit: ").lower()
#             if choice == 'q':
#                 break
#             elif choice == 'd':
#                 self.deposit()
#             else:
#                 self.play_round()

#         print(f"\nGame over! You leave with ${self.balance}.")


# def main():
#     game = SlotMachine()
#     game.start_game()


# if __name__ == '__main__':
#     main()
