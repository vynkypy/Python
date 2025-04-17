# 3️⃣ Write a function that takes a string and returns it reversed.

word = input("Enter a word: ")

reversed_word = ""

for char in word:
    reversed_word = char+reversed_word
print("Reversed_Word is: ", reversed_word)
