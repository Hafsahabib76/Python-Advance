# Prompt the user to input a word
userInput = input('Enter a word to Reverse it: ')

# Reverse the input word
reversed_word = userInput[:: -1]

# Display the reversed word to the user
print(f"Reversed Word: {reversed_word}")

