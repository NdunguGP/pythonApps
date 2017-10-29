item_list = []



def add_item(item):
    """add item to list"""
    item_list.append(item)


while True:
    data = input("> ")
    if data.upper() == "DONE":
        print("Your item list is: {}".format(item_list))
        break
    else:
        add_item(data)
#print(item_list)





#def end_fun():
 #   """finish entering item"""



