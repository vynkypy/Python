# 4️⃣ Print the multiplication table of a user-input number.

num = int(input("Enter the number: "))

print("Table using for loop")
for i in range(1, 11):
    print(num * i)

temp = 1
print("Table using while loop")
while temp <= 10:
    print(temp * num)
    temp += 1
