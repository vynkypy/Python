# 5️⃣ Reverse a string using a loop.

name = input("Enter a name: ")

reversed_str = ""
for char in name:
    reversed_str = char+reversed_str

print("Reversed string is: ", reversed_str)
