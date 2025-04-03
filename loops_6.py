# 6️⃣ Count the number of vowels in a given string.

vovels = ["a", "e", "i", "o", "u"]

word = input("Enter a word: ")

vovel_count = 0
for char in word:
    if char.lower() in vovels:
        vovel_count += 1

print(f"There are total {vovel_count} in {word}")
