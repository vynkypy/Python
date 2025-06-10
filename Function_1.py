# 1️⃣ Define a function that calculates the factorial of a number.
def factorial(var1):
    temp = 1

    for i in range(1, var1+1):
        temp = i*temp
    return temp


num = int(input("Enter a number: "))
print("The factorial of given number is: ", factorial(num))
