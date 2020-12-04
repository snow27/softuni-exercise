message = input()

command = input()

while not command == 'Decode':
    type_command = command.split('|')[0]
    if type_command == 'Move':
        num_letters = int(command.split('|')[1])
        message = message[num_letters:] + message[:num_letters]
    elif type_command == 'Insert':
        index = int(command.split('|')[1])
        value = command.split('|')[2]
        message = message[:index] + value + message[index:]
    elif type_command == 'ChangeAll':
        substring = command.split('|')[1]
        replacement = command.split('|')[2]
        message = message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {message}")
