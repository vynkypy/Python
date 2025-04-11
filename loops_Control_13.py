# 4️⃣ Find the first number divisible by both 4 and 7 in a given range (e.g., 1-50), using break.

for i in range(1, 51):
    if i % 4 == 0 and i % 7 == 0:
        print(i)
        break
