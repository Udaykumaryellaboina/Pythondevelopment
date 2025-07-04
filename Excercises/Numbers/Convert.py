#Write a Python program to convert kilometers to miles.
def kmToMl(KM:float):
    return km * 0.621371

    # Input from user


km = float(input("Enter distance in kilometers: "))

# Convert and display
miles = kmToMl(km)
print(f"{km} kilometers is equal to {miles:.2f} miles.")

# Write a Python program to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Formula: F = (C × 9/5) + 32
    return (celsius * 9/5) + 32

# Input from user
c = float(input("Enter temperature in Celsius: "))

# Convert and display
f = celsius_to_fahrenheit(c)
print(f"{c}°C is equal to {f:.2f}°F")
