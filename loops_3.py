# 3️⃣ Find the sum of numbers from 1 to 100 using a loop.

addition = 0
for i in range(101):
    addition += i
print("Addition of first 100 numbers using for loop: ", addition)


count = 0
addition_while = 0
while count <= 100:
    addition_while += count
    count += 1
print("Addition of first 100 numbers using while loop: ", addition_while)
