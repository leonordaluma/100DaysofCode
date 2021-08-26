age = input("What is your current age? ")
age_in_int = int(age)
past_days = age_in_int * 365
past_weeks = age_in_int * 52
past_months = age_in_int * 12
remaining_days = (365 * 90) - past_days
remaining_weeks = (52 * 90) - past_weeks
remaining_months = (12 * 90) - past_months
print(f"You have {remaining_days}, {remaining_weeks} weeks and {remaining_months} left.")