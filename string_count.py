str1 = input("Enter a string :")

chars_count = 0
digits_count = 0
symbols_count = 0

for char in str1:
    if char.isalpha():
        chars_count += 1
    elif char.isdigit():
        digits_count += 1
    else:
        symbols_count += 1

print("Total counts of chars, digits, and symbols")
print("Chars =", chars_count)
print("Digits =", digits_count)
print("Symbols =", symbols_count)
