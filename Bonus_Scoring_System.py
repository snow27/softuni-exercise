
import math
count_of_the_students = int(input())
count_of_the_lectures = int(input())
initial_bonus = int(input())
high_bonus = 0
high_attendances = 0

for i in range(count_of_the_students):
    attendances_for_each = int(input())
    total_bonus = attendances_for_each / count_of_the_lectures * (5 + initial_bonus)
    if high_bonus < total_bonus:
        high_bonus = total_bonus
        high_attendances = attendances_for_each

print(f"Max Bonus: {math.ceil(high_bonus)}.")
print(f"The student has attended {high_attendances} lectures.")
