waiting_people = int(input())
wagons = [int(num) for num in input().split()]

for i in range(len(wagons)):
    while wagons[i] < 4:
        if waiting_people > 0:
            wagons[i] += 1
            waiting_people -= 1
        else:
            break

all_people = len(wagons) * 4
taken_seats = sum(wagons)
if taken_seats < all_people and waiting_people == 0:
    print("The lift has empty spots!")
elif taken_seats == all_people and waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
str_wagons = map(str, wagons)
print(" ".join(str_wagons))


