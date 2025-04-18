# 4️⃣ Create a function to check if a given number is prime.
num = int(input("Enter a number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        # print("It's NOT a Prime Number")
        is_prime = False
        break
if is_prime:
    print("It's Prime Number")
else:
    print("It's NOT a Prime Number")
