input_string=input("Enter a string: \n")
length=len(input_string)
if length < 3:
    print("Input string is too short to extract the middle three characters.\n")
else:
    middle_index = length // 2
    if length % 2 == 0:
        middle_three = input_string[middle_index - 1: middle_index + 2]
    else:
        middle_three = input_string[middle_index - 1: middle_index + 2]
    new_string = middle_three
    print("New string:\n", new_string)

