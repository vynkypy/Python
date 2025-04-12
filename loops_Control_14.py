# 5️⃣ Print numbers from 1 to 10, but skip multiples of 3 using continue.


for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
