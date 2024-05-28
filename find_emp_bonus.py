years_of_experience = float(input("Enter the employee's years of experience: \n"))
salary = float(input("Enter the employee's salary: \n"))

if years_of_experience > 8:
    bonus_percentage = 10
elif years_of_experience > 4:
    bonus_percentage = 7
elif years_of_experience > 2:
    bonus_percentage = 4
else:
    bonus_percentage = 0

bonus_amount = (bonus_percentage / 100) * salary
print(f"The employee's bonus is: {bonus_amount:.2f}")
