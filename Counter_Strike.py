energy = int(input())

line = input()
count_battle = 0
while not line == "End of battle":

    distance = int(line)

    if energy < distance:
        print(f"Not enough energy! Game ends with {count_battle} won battles and {energy} energy")
        break
    else:
        energy -= distance
    count_battle += 1
    if count_battle % 3 == 0:
        energy += count_battle

    line = input()

if line == "End of battle":
    print(f"Won battles: {count_battle}. Energy left: {energy}")