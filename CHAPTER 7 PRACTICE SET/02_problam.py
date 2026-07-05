# Function to convert Fahrenheit to Celsius
def f_to_c(f):

    # Formula to convert Fahrenheit to Celsius
    c = (f - 32) * 5 / 9

    # Return the Celsius value
    return c


# Take input from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Call the function
celsius = f_to_c(fahrenheit)

# Display the result
print(f"{round(celsius, 2)}°C")

