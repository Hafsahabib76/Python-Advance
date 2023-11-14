# import libraries and modules
import re
import kfcModule
import random

# Create a list to store order history
order_history = []
# start user_order with none
user_order = None
# total amount
total_amount = 0

# Define a dictionary of patterns and responses
patterns = {
    r'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey!'],
    r'how are you': ["I am fine, thank you! What would you like to order today? Type 'menu'",
                     'I feel great! What would you like to order today?'],
    r'what is your name': ['I am a KFC Chatbot.', 'My name is KFC chatbot.'],
    r'menu|kfc menu|burger menu': ['Here is the KFC Burger menu:\n' + '\n'.join(
        [f"{sandwich} - Rs.{price}" for sandwich, price in kfcModule.burger_menu.items()])],
    r'cash on delivery': ['Great choice! Your order will be delivered shortly. Enjoy your meal!'],
    r'quit|exit': ['Thank you for using KFC Chatbot. Have a great day!', 'Goodbye! Have a great day.']
}

# Greet the user
kfcModule.greet()
# Display burger menu
kfcModule.display_burger_menu()

# continue the conversation with the user
while True:
    user_input = input("You: ")
    user_input_lower = user_input.lower()
    response = None

    # Check if the user wants to quit
    if user_input_lower == 'quit':
        print("Chatbot: Goodbye! Have a great day.")
        break

    # Manually checking for the patterns and responses
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input, flags=re.IGNORECASE):
            response = random.choice(responses)
            break

    if response is None:
        if user_order is None:
            # check the user item order in the menu
            user_order = kfcModule.find_burger(user_input)
            if user_order:
                response, total_amount, order_history = kfcModule.take_order(user_order, total_amount, order_history)
            else:
                # If user input item is not in the menu
                response = "I'm sorry, we don't have that item on our menu."

    # generate receipt
    if user_input_lower == 'receipt':
        if user_order is not None:
            response, user_order, total_amount, order_history = kfcModule.payment_receipt(user_order, total_amount,
                                                                                           order_history)
    # Handle the condition: if user want to order more items
    elif user_input_lower == 'yes':
        user_order = None
        user_quantity = 0
        response = "Sure! What burger would you like to order next?"

    # Handle the condition: if user dont want to order more, display the total order amount
    elif user_input_lower == 'no':
        if user_order is not None:
            response = f"Your total cart amount is Rs.{total_amount}. Type 'receipt' to generate the receipt."
        else:
            response = "There are no active orders in your cart."

    # print the responses
    print("Chatbot:", response)

