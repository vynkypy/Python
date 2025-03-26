# 1️⃣ Write a program to check if a number is positive, negative, or zero.
num = int(input('Enter a number: '))

if num > 0:
    print('It is a positive number')
elif num == 0:
    print('It is a zero')
else:
    print('It is a negative number')


# 2️⃣ Take a number from the user and print "Even" if it is even, otherwise print "Odd".
num2 = int(input('Enter a number: '))

if num2 % 2 == 0:
    print('The number is Even')
else:
    print('The number is Odd')


# 3️⃣ Write a program to check if a given year is a leap year or not.
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year")
else:
    print("It's not a leap year")

# 4️⃣ Ask the user for age and check if they are eligible to vote (18+) or not.
age = int(input("Enter the age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 5️⃣ Take three numbers as input and print the largest among them.
no1, no2, no3 = map(int, input("Enter three numbers").split())

if no1 > no2 and no1 > no3:
    print(f"{no1} is the largest")
elif no2 > no1 and no2 > no3:
    print(f"{no2} is the largest")
else:
    print(f"{no3} is the largest")


# 6️⃣ Write a program to determine if a number is divisible by both 3 and 5.
num_div = int(input("Enter the number: "))
if num_div % 3 == 0 and num_div % 5 == 0:
    print("The number is divisible by 3 and 5")
else:
    print("Number is not divisble by 3 and 5")


# 7️⃣ Create a program that checks if a given character is a vowel or consonant.
char = input("Enter a character: ").lower()
vovel = ['a', 'e', 'i', 'o', 'u']

if char in vovel:
    print("It's a vovel")
else:
    print("It's a consonent")


# 8️⃣ Ask the user for a password and check if it meets criteria (length ≥ 8).
password = input("Enter the password: ")
if len(password) >= 8:
    print("Password is strong")
else:
    print("Password is weak")


# 9️⃣ Write a program that calculates discount based on purchase amount (e.g., if amount > 5000, give 10% discount).
amount = int(input("What is your purchase amount: "))
if amount > 5000:
    dis_amount = amount - amount*0.1
    print("Your discounted amount is: ", dis_amount)
else:
    print("You are not eligible for discount")

# 🔟 Create a grading system where marks are given as input and output is A, B, C, or F.
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 35:
    print("Grade: E")
else:
    print("Grade: F")
