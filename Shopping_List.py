def check_item_exist(list_items, item):
    return True if item in list_items else False


shopping_list = input().split("!")

line = input()

while not line == "Go Shopping!":
    line = line.split()
    command = line[0]
    product = line[1]
    if command == "Urgent":
        if not check_item_exist(shopping_list, product):
            shopping_list.insert(0, product)
    elif command == "Unnecessary":
        if check_item_exist(shopping_list, product):
            shopping_list.remove(product)
    elif command == "Correct":
        if check_item_exist(shopping_list, product):
            new_product = line[2]
            current_index = shopping_list.index(product)
            shopping_list[current_index] = new_product
    elif command == "Rearrange":
        if check_item_exist(shopping_list, product):
            current_index = shopping_list.index(product)
            x = shopping_list.pop(current_index)
            shopping_list.append(x)

    line = input()

print(", ".join(shopping_list))

