age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
max_weeks = 90 * 52
current_age_in_weeks = int(age) * 52
remaining_weeks = max_weeks - current_age_in_weeks
print(f"You have {remaining_weeks} weeks left.")
