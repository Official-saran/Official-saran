str1 = input("Enter the first string (str1): ")
str2 = input("Enter the second string (str2): ")
middle_index = len(str1) // 2
str3 = str1[:middle_index] + str2 + str1[middle_index:]
print("New string:", str3)
