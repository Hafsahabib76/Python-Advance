
# ANSI escape codes for text colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

KFC_Logo = """⣿⣿⣿⣿⣿⣿⣿⡿⢟⣋⣭⣥⣭⣭⣍⡉⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠁⠠⠶⠛⠻⠿⣿⣿⣿⣿⣷⡄⠄⠄⠄⠄⠉⠻⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠟⠄⢀⡴⢊⣴⣶⣶⣾⣿⣿⣿⣿⢿⡄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿
⣿⣿⡿⠁⠄⠙⡟⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣎⠃⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿
⣿⡟⠄⠄⠄⠄⡇⠰⠟⠛⠛⠿⠿⠟⢋⢉⠍⢩⣠⡀⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿
⣿⠁⠄⠄⠄⠄⠰⠁⣑⣬⣤⡀⣾⣦⣶⣾⣖⣼⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿
⡏⠄⠄⠄⠄⠄⠄⠄⠨⣿⠟⠰⠻⠿⣣⡙⠿⣿⠋⠄⢀⡀⣀⠄⣀⣀⢀⣀⣀⢸
⡇⠄⠄⠄⠄⠄⠄⠄⠄⣠⠄⠚⠛⠉⠭⣉⢁⣿⠄⢀⡿⢾⣅⢸⡗⠂⢿⣀⡀⢸
⡇⠄⠄⠄⠄⠄⠄⠄⠄⠘⢧⣄⠄⣻⣿⣿⣾⠟⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸
⣿⠄⠄⠄⠄⠄⠄⠄⠄⢠⡀⠄⠄⣿⣿⠟⢁⣴⣿⢸⡄⠄⢦⣤⣤⣤⣤⣄⡀⣼
⣿⣧⠄⠄⠄⠄⠄⠄⢠⡸⣿⠒⠄⠈⠛⠄⠁⢹⡟⣾⡇⠄⠈⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣧⣠⣴⣦⠄⠄⢸⣷⡹⣧⣖⡔⠄⠱⣮⣻⣷⣿⣿⠄⠄⠘⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠄⠄⠸⠿⠿⠚⠛⠁⠂⠄⠉⠉⡅⢰⡆⢰⡄⠄⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⣷⠘⣧⣠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣄⣀⣀⡀⠄⣀⣀⣹⣦⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿"""

burger_menu = {
    "Zinger Burger": 550,
    "Zinger Stacker": 590,
    "Kentucky Burger": 590,
    "Mighty Zinger": 700,
    "Zinger Super Charger": 590
}


def greet():
    print(RED + f"{KFC_Logo}" + RESET)
    print("Hi! Welcome to KFC. I am KFC ChatBot, the food ordering assistant.")

def display_burger_menu():
    burger_list = ""
    for burger, price in burger_menu.items():
        burger_list += f"{burger} - Rs.{price}\n"
    print(f"Here's our KFC burger menu 🍔: \n\n" + YELLOW + f"{burger_list}" + RESET)

def find_burger(user_input):
    user_input = user_input.lower()
    for burger in burger_menu:
        if user_input in burger.lower():
            return burger
    return None


def take_order(user_order, total_amount, order_history):
    user_quantity = int(input(f"Chatbot: How many {user_order} would you like to order?\nYou: "))
    order_amount = burger_menu[user_order] * user_quantity
    total_amount += order_amount
    response = (f"Your order of '{user_quantity} {user_order}' has been added to your cart. \nYour total cart "
                f"amount is Rs.{total_amount}. \nWould you like to order more Type 'yes' or 'no' to continue.")
    order_history.append({"burger": user_order, "quantity": user_quantity, "amount": order_amount})
    return response, total_amount, order_history


def payment_receipt(user_order, total_amount, order_history):
    payment_option = input(f"Chatbot: Please select the payment option: 'Cash on delivery' or 'Card payment': \nYou: ")
    response = f"Here's your KFC order receipt:\n" \
               + YELLOW + f"*****************************************************\n"
    for order in order_history:
        response += f" {order['burger']}({order['quantity']}) - Rs.{order['amount']}\n\n"
    response += f" Total Amount: Rs.{total_amount}\n\n" \
                f" Payment Option: {payment_option}\n" \
                f"*****************************************************\n" \
                f" Thank you for ordering from KFC. Enjoy your meal! 🍔" + RESET
    user_order = None
    total_amount = 0
    order_history = []  # Clear order history
    return response, user_order, total_amount, order_history
