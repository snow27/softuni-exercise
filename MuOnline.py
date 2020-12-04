rooms = input().split("|")
health = 100
bitcoins = 0
is_over = False

for room in rooms:
    command = room.split()[0]
    number = int(room.split()[1])
    if command == "potion":
        if (health + number) > 100:
            number = 100 - health
            health = 100
        else:
            health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            index = rooms.index(room)
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index + 1}")
            is_over = True
            break
    if is_over:
        break
if not is_over:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {health}")