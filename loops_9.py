# 9️⃣ Print the following pattern using nested loops:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

number = int(input("Enter the number: "))

for i in range(number):
    for j in range(i+1):
        print(j, end="")
    print()
