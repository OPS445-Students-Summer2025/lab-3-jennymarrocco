#!/usr/bin/env python3
'''Lab 3 Part 6 - List Modification Functions'''
# Author ID: jlmarroc

# Global list
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Add next number to list (increment last element)
    if ordered_list:  # Check if list is not empty
        next_value = ordered_list[-1] + 1
        ordered_list.append(next_value)

def remove_items_from_list(ordered_list, items_to_remove):
    # Remove all items that match items_to_remove from ordered_list
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
