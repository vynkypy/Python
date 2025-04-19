# 5️⃣ Write a function that converts Celsius to Fahrenheit.

num = float(input("Enter the temprature in degree Celsius: "))


def cel_to_fah(no):
    return (no*(9/5)) + 32


result = cel_to_fah(num)

print("Temprature in Fahrenheit:", result, "°F")
