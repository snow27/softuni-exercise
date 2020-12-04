def check_index(target_index, targets_place):
    if 0 <= target_index < len(targets_place):
        return True
    else:
        return False


targets = [int(shoot) for shoot in input().split()]

command = input()

while not command == "End":
    type_command = command.split()[0]
    index = int(command.split()[1])
    index_value = int(command.split()[2])
    is_exist = check_index(index, targets)
    if type_command == "Shoot":
        if is_exist:
            targets[index] -= index_value
            if targets[index] <= 0:
                targets.pop(index)
    elif type_command == "Add":
        if is_exist:
            targets.insert(index, index_value)
        else:
            print("Invalid placement!")
    elif type_command == "Strike":
        start = index - index_value
        stop = index + index_value + 1
        if 0 <= start < len(targets) and 0 <= stop < len(targets):
            del targets[start:stop]
        else:
            print("Strike missed!")
    command = input()

print("|".join(map(str, targets)))