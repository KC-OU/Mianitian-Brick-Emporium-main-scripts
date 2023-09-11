# Riley Oard
# 11/20/19
# Final Project
# creating an inventory management system for a company

import os
import fileinput

def menuDisplay():
    print('=============================')
    print('= Mianitian Brick Emporium - Lego Set =')
    print('=============================')
    print('(1) Add New Lego Set to Inventory')
    print('(2) Remove Lego Set from Inventory')
    print('(3) Update Set Inventory')
    print('(4) Search Lego Set in Inventory')
    print('(5) Print Set Inventory Report')
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
    InventoryFile = open('sets-Inventory.txt', 'a')
    print("Adding Inventory")
    print("================")
    Set_Name = input("Add Set Name")
    Set_ID = input("Add Set ID")
    Set_Year = input("Add Set Year")
    Set_Retried = input("is the set retired or not retried")
    Set_quantity = input("Enter the quantity of the item: ")
    Set_Category = input("Add Part Category")
    Bricklink_Price = input("Bricklink Price")
    Lego_Price = input("Lego Price")
    
    # InventoryFile.wrire
    
    InventoryFile.write(Set_Name + '\n')
    InventoryFile.write(Set_ID + '\n')
    InventoryFile.write(Set_Year + '\n')
    InventoryFile.write(Set_Retried +'\n')
    InventoryFile.write(Set_quantity + '\n')
    InventoryFile.write(Set_Category + '\n')
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
    Set_Name = input("Enter the item name to remove from inventory: ")

    file = fileinput.input('sets-Inventory.txt', inplace=True)

    for line in file:
         if Set_Name in line:
             for i in range(1):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    Set_Name
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def updateInventory():
    print("Updating Inventory")
    print("==================")
    Set_Name = input('Enter the part name to update: ')
    Set_quantity = int(input("Enter the updated quantity. Enter - for less: "))
    with open('sets-Inventory.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('sets-Inventory.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if Set_Name in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (Set_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('sets-Inventory.txt', 'w') as f:
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
    Set_Name = input('Enter the name of the item: ')
    
    f = open('sets-Inventory.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if Set_Name in line:
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
    InventoryFile = open('sets-Inventory.txt', 'r')
    Set_Name = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    while Set_Name != '':
        Set_quantity = InventoryFile.readline()
        Set_ID = Set_ID.rstrip('\n')
        Set_quantity = Set_quantity.rstrip('\n')
        print('Item:     ', Set_ID)
        print('Quantity: ', Set_quantity)
        print('----------')
        Set_ID = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit:'))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

menuDisplay()
