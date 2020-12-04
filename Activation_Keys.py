

activation_key = input()

s = ">>>"

command = input()

while not command == "Generate":
    type_command = command.split(s)[0]
    if type_command == "Contains":
        substring = command.split(s)[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif type_command == "Flip":
        u_or_l = command.split(s)[1]
        i_1 = int(command.split(s)[2])
        i_2 = int(command.split(s)[3])
        if u_or_l == "Upper":
            up = activation_key[i_1:i_2].upper()
            activation_key = activation_key[:i_1] + up + activation_key[i_2:]
        elif u_or_l == "Lower":
            low = activation_key[i_1:i_2].lower()
            activation_key = activation_key[:i_1] + low + activation_key[i_2:]
        print(activation_key)
    elif type_command == "Slice":
        i_1 = int(command.split(s)[1])
        i_2 = int(command.split(s)[2])
        activation_key = activation_key[:i_1] + activation_key[i_2:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")