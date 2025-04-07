# 8️⃣ Find the factorial of a number using a loop.
# 5! = 5 × 4 × 3 × 2 × 1 = 120

n_number = int(input("Enter the number you want factorial for: "))

result = 1
for i in range(1, n_number+1):
    result = result*i
print(result)
