# 2️⃣ Print even numbers from 2 to 20.


for i in range(1, 21):
    if i % 2 == 0:
        print(i)

num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
        num += 1
    else:
        num += 1
