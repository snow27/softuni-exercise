def add_stop(index, string, t_line):
    index = int(index)
    if index < len(t_line):
        t_line = t_line[:index] + string + t_line[index:]
    print(t_line)
    return t_line


def remove_stop(start_index, end_index, t_line):
    start_index = int(start_index)
    end_index = int(end_index)
    if 0 <= start_index < len(t_line) and 0 <= end_index < len(t_line):
        t_line = t_line[:start_index] + t_line[end_index + 1:]
    print(t_line)
    return t_line


def switch(old_string, new_string, t_line):
    if old_string in t_line:
        t_line = t_line.replace(old_string, new_string)
    print(t_line)
    return t_line


text_line = input()

command = input()

while not command == "Travel":
    type_command = command.split(":")[0]
    first_command = command.split(":")[1]
    second_command = command.split(":")[2]
    if type_command == "Add Stop":
        text_line = add_stop(first_command, second_command, text_line)
    elif type_command == "Remove Stop":
        text_line = remove_stop(first_command, second_command, text_line)
    elif type_command == "Switch":
        text_line = switch(first_command, second_command, text_line)
    command = input()

print(f"Ready for world tour! Planned stops: {text_line}")
