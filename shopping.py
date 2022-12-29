# shopping.py
# A prototype script to create a shopping list from scanned items 
# (using a barcode scanner) and print a receipt.
# Tom Dalby - https://github.com/thomasjackdalby
# 28/12/2022

import json
import os
import datetime
from escpos.printer import Serial

END_CODE = "5021265245932"
COM_PORT = "COM4"
ITEMS_FILE_NAME = "items.json"
ITEMS_FILE_PATH = os.path.join(os.path.dirname(__file__), ITEMS_FILE_NAME)

def load_items(file_path):
    """ Loads items from a .json file """

    with open(file_path, "r") as file:
        return {item["number"] : item for item in json.load(file)}

def save_items(file_path, items):
    """ Saves items to a .json file """
    
    with open(file_path, "w") as file:
        json.dump([item for item in items.values()], file)

def create_shopping_list(items):
    """ Creates a shopping list by allowing the user to scan many items, 
    returning a sorted shopping list.\n
    
    The list is completed by scanning the END_CODE """

    shopping_list = {}
    while True:
        item_barcode = input("SCAN >")

        # break out of the loop if we've finished scanning
        if item_barcode == END_CODE: 
            print("END_CODE scanned. Generating shopping list.")    
            break

        # add the item if it is a new item
        if item_barcode not in items:
            print("New item scanned!")
            items[item_barcode] = {
                "name": input("Please enter item name: "),
                "number": item_barcode
            }

        # Update the item in the shopping list
        item = items[item_barcode]
        if item_barcode not in shopping_list:
            shopping_list[item_barcode] = 0
            print(f"Added {item['name']} to shopping list.")
        shopping_list[item_barcode] += 1
        item_amount = shopping_list[item_barcode]
        print(f"Updated amount of {item['name']} from {item_amount-1} to {item_amount}.")

    # convert the dictionary to list of tuples
    sorted_shopping_list = [(items[number], shopping_list[number]) for number in shopping_list.keys()] 
    
    # sort the shopping list by item name
    sorted_shopping_list.sort(key=lambda item: item[0]["name"])

    return sorted_shopping_list

def print_shopping_list(shopping_list):
    """ Prints a shopping list using a receipt printer """

    # setup the printer (the com port may/will be different each use) 
    p = Serial(COM_PORT, baudrate=19200)

    p.set(double_width=True, double_height=True, align="center")
    p.textln("SHOPPING")
    p.textln("--------")
    p.set(double_width=True, double_height=False, align="center")
    p.textln(f"{datetime.datetime.now().strftime('dd/MM/yy hh:mm:ss')}")

    # print out the items
    for item, amount in shopping_list:
        p.set(double_width=True, double_height=True, align="left")
        p.textln(f"{item['name']} (x{amount})")
        p.set(double_width=False, double_height=False, align="right")
        p.textln(item["number"])
        p.textln()

    # terminate the receipt
    p.cut()

if __name__ == "__main__":
    items = load_items(ITEMS_FILE_PATH)
    shopping_list = create_shopping_list(items)
    print_shopping_list(shopping_list)
    save_items(ITEMS_FILE_PATH, items)
