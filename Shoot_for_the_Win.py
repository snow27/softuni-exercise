sequence = [int(seq) for seq in input().split()]

command = input()
count = 0
while not command == "End":
    index = int(command)
    if 0 <= index < len(sequence):
        count += 1
        save_value = sequence[index]
        sequence[index] = -1
        for i in range(len(sequence)):
            if sequence[i] == -1:
                continue
            elif save_value >= sequence[i]:
                sequence[i] += save_value
            else:
                sequence[i] -= save_value

    command = input()

print(f"Shot targets: {count} -> {' '.join(map(str, sequence))}")
