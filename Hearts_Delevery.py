houses = input().split("@")
houses = [int(house) for house in houses]
line = input()
position = 0
last_position = 0
while not line == "Love!":
    line = line.split()
    length = int(line[1])
    position += length
    if position >= len(houses) or position < 0:
        position = 0

    if houses[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses[position] -= 2
        if houses[position] == 0:
            print(f"Place {position} has Valentine's day.")
    last_position = position
    line = input()

print(f"Cupid's last position was {last_position}.")
if houses.count(0) == len(houses):
    print(f"Mission was successful.")
else:
    fail_houses = len(houses) - houses.count(0)
    print(f"Cupid has failed {fail_houses} places.")