# Write a program which accept number from user and if number is less than 50 then print small,
# if it is greater than 50 and less than 100 then print medium, if it is greater than 100 then print large.

num = int(input("Enter a number: "))

if num < 50:
    print("Small")
elif num > 50 and num < 100:
    print("Medium")
else:
    print("Large")
