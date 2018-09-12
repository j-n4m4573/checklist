# coding=utf-8

# print("Hello World")

checklist = list()

# def my_fun_function(say_this):
#
#     my_fun_function("Hello World")

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

# checklist = ['Hello','World']
# checklist[1] = 'Cats'
# print(checklist)

def update(index, item):
    checklist[index] = item

# checklist = ["Hello", "World"]
# checklist.pop(1)
# print(checklist)

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        # print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

list_all_items()

def marked_completed(index):
    checklist[index] = "√" + checklist[index]
    print(checklist[index])
# marked_completed(1)
#update and read functions

# gather user input
def user_input(prompt):
    user_value = input(prompt)
    return choose(user_value)

def choose(option_selected):

    #Create item
        if option_selected == "a":
            input_item = input("Add new item:  ")
            create(input_item)
            print("Item created: {}".format(input_item))
            return True
    #read Item
        elif option_selected == "f":
            item_index = int(input("Find index Number?"))
            read(item_index)
            print("Item selected: {}".format(input_item))
            return True
        elif option_selected == "m":
            index = int(input("Index of item completed: "))
            marked_completed(index)
            return True
        elif option_selected == "u":
            item_index = int(input("Update at item at index "))
            update_item = input("Update item with")
            update(item_index, update_item)
            print("Item updated: {}".format(input_item))
            return True
        elif option_selected == "d":
            item_index = int(input("delete item at index: "))
            print("{} item deleted".format(checklist[item_index]))
            return true
# Print all items
        elif option_selected == "p":
            list_all_items()
            return True
        elif option_selected == "q":
            print("option q")
            return False
# Catch All
        else:
            print("Unknown Option")
            return True

# def user_prompt():


def start():
        user_value = user_input("Please enter a value:")

def test():
        create("purple sox")
        create("red cloak")
        create("teal socks")
        create("real socks")
        print(read(0))
        print(read(1))
        update(0,"purple sox")
        destroy(1)
        print(read(0))
        choose("a")
        choose("f")
        choose("m")
        choose("u")
        choose("p")
        choose("d")
        list_all_items()
        # user_value = user_input("Please enter a value:")
        # print(user_value)
# test()
start()
running = True
while running:
    selection = user_input("choose an option: A - Add,F - Find, M- Mark complete, U -Update, P- Print")
    running = choose(selection)
