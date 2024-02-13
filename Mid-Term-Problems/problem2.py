# Ask the user to input a temperature value
temperature_value = int(input('Enter Temperature value: '))
# Ask the user to specify whether the temperature is in Celsius or Fahrenheit
temperature_type = input("Press 'C' for Celsius or 'F'' for Fahrenheit: ")


# Function to convert the temperature to the other unit
# (if it's in Celsius, convert it to Fahrenheit, and vice versa)
def convert_temperature(value, type):
    if type.lower() == 'c':
        return (value - 32) * 5/9
    elif type.lower() == 'f':
        return (value * 9/5) + 32
    else:
        return 0


# Get the result by calling the convert_temperature function
# And passing the user input in parameters.
result = convert_temperature(temperature_value, temperature_type)

# if user press something else instead of C or F in temperature type
if result == 0:
    # Display the incorrect temperature type message
    print('Incorrect Temperature Type')
else:
    # Display the converted temperature to the user
    print(f"The temperature in {temperature_type}° is {result}")

