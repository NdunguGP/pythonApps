
shopping_list = []

def show_help():
    print("Items to pick at the stores")
    print("""
enter HELP to show help
enter DONE to stop entering items
enter SHOW to view list items
"""
          )

def show_list():
    print("here is your list")
    for item in shopping_list:
        print(item)


def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items".format(new_item, len(shopping_list)))

show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE':
        #show_list()
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()
    
