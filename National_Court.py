first_employee = int(input())
second_employee = int(input())
three_employee = int(input())
people_count = int(input())

sum_of_people = first_employee + second_employee + three_employee

hour_count = 0

while not people_count <= 0:
    hour_count += 1
    people_count -= sum_of_people

    if hour_count % 4 == 0:
        hour_count += 1

print(f"Time needed: {hour_count}h.")
