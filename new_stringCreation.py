input_string=input("Enter a string: \n")
length=len(input_string)
if length % 2 == 0:
    middle=input_string[length // 2 - 1: length // 2 + 1]
else:
    middle = input_string[length // 2]
new_string = input_string[0] + middle + input_string[-1]
print("New string:\n", new_string)

