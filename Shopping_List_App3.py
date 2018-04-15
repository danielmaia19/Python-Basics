import os

# make a list to hold the shopping list items
shopping_list_items = []


def clear_screen():
    # enable this if the script is ran on the terminal
    #os.system("cls" if os.name == "nt" else "clear")
    print("\n"*100)


def show_help():
    clear_screen()
    # print out instructions on how to use the app
    print("What shall we get from the store?")
    print("""
Type DONE to quit the app
Type HELP to show instructions
Type SHOW to show shopping list
    """)


def show_items():

    clear_screen()

    show_help()

    print("Here is your list: ")

    # print out the whole list
    for index, item in enumerate(shopping_list_items, start=1):
        print("{}. {}".format(index, item))

    print("-"*10)


def remove_from_list():
    show_items()

    what_to_remove = input("What would you like to remove?\n> ")

    try:
        shopping_list_items.remove(what_to_remove)
    except ValueError:
        pass

    show_items()


def add_item(new_item):
    show_items()

    if len(shopping_list_items):
        position = input("Where do you want to put {} \n"
                         "Press Enter to add it to the end of the list \n"
                         "> ".format(new_item)
                         )
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list_items.insert(position-1, new_item)
    else:
        # add new items to our list
        shopping_list_items.append(new_item)


show_help()

while True:

    # ask for new items
    new_item = input("> ")

    # how type DONE to quit the app
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_items()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    elif new_item == "":
        print("Cannot add an empty item to the list, please enter a valid item")
        continue
    else:
        # adds new items
        add_item(new_item)

    show_items()



