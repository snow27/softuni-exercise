# def check_valid(p, plants_dict):
#     if p in plants_dict:
#         return True
#     return False


n = int(input())
plants = {}
for i in range(n):
    text_input = input().split("<->")
    plant = text_input[0]
    rarity = int(text_input[1])
    if plant not in plants:
        plants[plant] = [0, 0.0, 0]
    plants[plant][0] = rarity

command = input()

while not command == "Exhibition":
    command = command.split()
    type_command = command[0]
    plant = command[1]
    if plant not in plants:
        print('error')
    elif type_command == "Rate:":
        rating = float(command[3])
        plants[plant][1] += rating
        plants[plant][2] += 1
    elif type_command == 'Update:':
        new_rarity = int(command[3])
        plants[plant][0] = new_rarity
    elif type_command == 'Reset:':
        plants[plant][1] = 0.0
        plants[plant][2] = 0
    else:
        print('error')
    command = input()
print('Plants for the exhibition:')
sorted_plants = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])))
for plant in sorted_plants:
    rarity = sorted_plants[plant][0]
    if sorted_plants[plant][2] > 0:
        rating = float(sorted_plants[plant][1] / sorted_plants[plant][2])
    else:
        rating = 0.0
    print(f'- {plant}; Rarity: {rarity}; Rating: {rating:.2f}')

