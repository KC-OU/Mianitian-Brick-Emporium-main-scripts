# Riley Oard
# 11/20/19
# Final Project
# creating an inventory management system for a company

import os
import fileinput

def menuDisplay():
    print('=============================')
    print('= Mianitian Brick Emporium - Lego Parts =')
    print('=============================')
    print('(1) Add New Lego Part to Inventory')
    print('(2) Remove Lego Part from Inventory')
    print('(3) Update Part Inventory')
    print('(4) Search Lego Part in Inventory')
    print('(5) Print Part Inventory Report')
    print('(99) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 99:
        exit()

def addInventory():
    InventoryFile = open('parts-Inventory.txt', 'a')
    print("Adding Inventory")
    print("================")
    Part_Name = input("Add Part Name")
    Part_ID_Bricklink = input("Add Part ID from BrickLink")
    Part_ID_Lego_Instructions = input("Add Part ID from Lego Instructions")
    part_description = input("Enter the part description: ")
    part_quantity = input("Enter the quantity of the item: ")
    Part_Colour = input("Add Part Colour")
    Part_Category = input("Add Part Category")
    Bricklink_Price = input("Bricklink Price")
    Lego_Price = input("Lego Price")
    
    # InventoryFile.wrire
    
    InventoryFile.write(Part_Name + '\n')
    InventoryFile.write(Part_ID_Bricklink + '\n')
    InventoryFile.write(Part_ID_Lego_Instructions + '\n')
    InventoryFile.write(part_description + '\n')
    InventoryFile.write(part_quantity + '\n')
    InventoryFile.write(Part_Colour + '\n')
    InventoryFile.write(Part_Category + '\n')
    InventoryFile.write(Bricklink_Price + '\n')
    InventoryFile.write(Lego_Price + '\n')
    InventoryFile.close()
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    
def removeInventory():
    print("Removing Inventory")
    print("==================")
    Part_Name = input("Enter the item name to remove from inventory: ")

    file = fileinput.input('parts-Inventory.txt', inplace=True)

    for line in file:
         if Part_Name in line:
             for i in range(1):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    Part_Name
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def updateInventory():
    print("Updating Inventory")
    print("==================")
    Part_Name = input('Enter the part name to update: ')
    part_quantity = int(input("Enter the updated quantity. Enter - for less: "))
    with open('parts-Inventory.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('parts-Inventory.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if Part_Name in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (part_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('parts-Inventory.txt', 'w') as f:
        for line in filedata:
            f.write(line)
                                            
                
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def searchInventory():
    print('Searching Inventory')
    print('===================')
    Part_Name = input('Enter the name of the item: ')
    
    f = open('parts-Inventory.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if Part_Name in line:
            for b in search[i:i+1]:
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
                print('----------')
        
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        
def printInventory():
    InventoryFile = open('parts-Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit:'))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

menuDisplay()
