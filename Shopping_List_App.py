# make a list to hold the shopping list items
shopping_list_items = []


def show_help():
    # print out instructions on how to use the app
    print("What shall we get from the store?")
    print("""
Type DONE to quit the app
Type HELP to show instructions
Type SHOW to show shopping list
    """)


def show_items():

    # show items in the list
    print("You have the following items in your list: ")

    # print out the whole list
    for item in shopping_list_items:
        print(item)

    print("Total items {}".format(len(shopping_list_items)))


def add_item(new_item):
    # add new items to our list
    shopping_list_items.append(new_item)


show_help()

while True:

    # ask for new items
    new_item = input("> ")

    # how type DONE to quit the app
    if new_item == 'DONE':
        show_items()
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_items()
        continue

    # adds new items
    add_item(new_item)

    print("You have added {}. You now have {} in your list".format(new_item.upper(), len(shopping_list_items)))





