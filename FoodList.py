# import sys
import os
Foodlist = "Foodlist.txt"
Itemnames = {'1':'Rice', '2':'Oil', '3':'Flour', '4':'Spice', '5':'Vegetable', '6':'Meat', '7':'Cheese', '8':'Milk', '9':'Noodle','0':'Tissue'}
ItemStruct ={'1':'Item No.','2':'name', '3':'weight', '4':'price', '5':'expire days'}
# global ItemNo
# ItemNo = 1000


def menu():
    print('''
    
    ''')
    print("====================Food stock managment system=====================")
    print("                   1. Input item")
    print("                   2. Search item")
    print("                   3. Delete item")
    print("                   4. Modify item")
    print("                   5. Sort item")
    print("                   6. Summarize item")
    print("                   7. Display all")
    print("                   0. Quit")
    print("====================================================================")

def fileRead():
    global ItemNo, ItemList
    ItemNo = 1000
    if os.path.exists(Foodlist):
        with open(Foodlist,'r') as lst:
            ItemList = list(lst.readlines())
            for i in range(len(ItemList)):
                temp = eval(ItemList[i])
                if ItemNo <= temp['Item No.']:
                    ItemNo = temp['Item No.']
                ItemList[i] = temp
        
    else:
        print("file doesn't exist, a data file is created!")
        DataFile = open(Foodlist, 'w')
        DataFile.close()
        ItemNo = 1000

    return

def fileSave():
    pass



def Input():        #done
    fileRead()

    item ={}
    with open(Foodlist,'a') as lst:
        while True:
            try:
                item["Item No."] = globals()['ItemNo'] +1
                item["name"] = Itemnames[input('''Please input an item
                1. Rice
                2. Oil
                3. Flour
                4. Spice
                5. Vegetable
                6. Meat
                7. Cheese
                8. Milk
                9. Noodle
                0. Tissue

                Name: ''')]
                item["weight"] = float(input("Weight(kg):"))
                item["price"] = float(input("Price($):"))
                item["expire days"] = int(input("Expire days:"))
            except:
                print("invalid input, please input again:")
 
            if globals()['ItemNo'] == 0:
                lst.write(str(item))
            else:
                lst.write("\n"+str(item))

            lst.flush()
            globals()['ItemNo'] += 1 
            # print('file wrote')

            choice = input('Do you wish to input more data? y/n?: ')
            if choice == 'y' or choice == 'Y':
                continue
            else:            
                break
   



def Search():       #search by Item No. and Name are done, by Weight, price and expire days are still due
    # if os.path.exists(Foodlist):
    #     with open(Foodlist,'r') as lst:
    #         ItemList = list(lst.readlines())
    #         dictedItemlist=[]
    #         for i in ItemList:
    #             # print(i)
    #             currentItem = dict(eval(i))
    #             dictedItemlist.append(currentItem)
    # else:
    #     print('The lis is Empty')
    fileRead()

    while True:
        try:
            Method = input('''
            1. Item No.
            2. Name
            3. Weight
            4. Price
            5. Expire days
            which key to search: ''')
            break
        except:
            print('wrong input, please input again')

    foundItem = []
    if Method == '1':
        #search item no.
        demondKey = int(input('please input the Item No. to search: '))
        for i in globals()['ItemList']:
            if i['Item No.'] == demondKey:
                foundItem.append(i)
    elif Method =='2':
        while True:
            try:
                demondKey =    Itemnames[input('''\n
                            1. Rice
                            2. Oil
                            3. Flour
                            4. Spice
                            5. Vegetable
                            6. Meat
                            7. Cheese
                            8. Milk
                            9. Noodle
                            0. Tissue

                            What to search: ''')]
                break
            except:
                print('invalid input, please try again')

        for i in globals()['ItemList']:
            if i['name'] == demondKey:
                foundItem.append(i)

    if foundItem:
        print('%d item are found' %(len(foundItem)))

        print("\nItem No.     Name       Weight(kg)    Price($)    Expire days")
        for i in foundItem:
            print(f"{i.get('Item No.'):<13}{i.get('name'):<13}{i.get('weight'):<13}{i.get('price'):<13}{i.get('expire days'):<10}")
   
    input('\nPress "Enter" to continue')


def Delete():       #done
    # if os.path.exists(Foodlist):
    #     with open(Foodlist,'r') as lst:
    #         ItemList = list(lst.readlines())
    #         dictedItemlist=[]
    #         for i in ItemList:
    #             # print(i)
    #             currentItem = dict(eval(i))
    #             dictedItemlist.append(currentItem)
    # else:
    #     print('The lis is Empty')       
    #     return
    fileRead()

    if len(globals()['ItemList']) <= 1:
        print('No item to delete!!')
        return
    
    DisplayAll()

    while True:
        try:
            itemToDelete = int(input('Please select an Item No. to delete: '))
            break
        except:
            print('invalid input value, please input again!')
    
    newFoodList =[]

    # newIndex = 1
    for i in globals()['ItemList']:
        if i['Item No.'] == itemToDelete:
            print('Item %d was deleted' % (i['Item No.']))
            continue
        # i['Item No.'] = newIndex
        newFoodList.append(i)
        # newIndex += 1

    with open(Foodlist,'w') as lst:
        for i in newFoodList:
            if newFoodList.index(i) == 0:
                lst.write(str(i))
            else:
                lst.write("\n"+str(i))

        # lst.write(str(newFoodList)+"\n")


        lst.flush()


def Modify():       #done

    if os.path.exists(Foodlist):
        with open(Foodlist,'r') as lst:
            ItemList = list(lst.readlines())
            dictedItemlist=[]
            for i in ItemList:
                # print(i)
                currentItem = dict(eval(i))
                dictedItemlist.append(currentItem)
    else:
        print('The lis is Empty')       
        return
    itemToModify =0
    try:
        itemToModify = int(input('Please enter the Item No. to modify:'))

    except:
        print('invalid Item No., Please enter again')

    item = {}
    currentLocation = 0
    for i in dictedItemlist:
        if itemToModify == i['Item No.']:
            while True:
                try:
                    item["Item No."] = itemToModify 
                    item["name"] = Itemnames[input('''
                    1. Rice
                    2. Oil
                    3. Flour
                    4. Spice
                    5. Vegetable
                    6. Meat
                    7. Cheese
                    8. Milk
                    9. Noodle
                    0. Tissue

                    Name: ''')]
                    item["weight"] = float(input("Weight(kg):"))
                    item["price"] = float(input("Price($):"))
                    item["expire days"] = int(input("Expire days:"))
                    break
                except:
                    print('invalid values, please input again!')
            dictedItemlist[currentLocation] = item
            break
        currentLocation +=1


    with open(Foodlist,'w') as lst:
        for i in dictedItemlist:
            if dictedItemlist.index(i) == 0:
                lst.write(str(i))
            else:
                lst.write("\n"+str(i))

        # lst.write(str(newFoodList)+"\n")

        lst.flush()



    # print("Calling Modify()")

def SortItem():
    fileRead()
    sortedItemList = []
    while True:
        try:
            sortingMethod = input('''
            1. Item No.
            2. Name
            3. Weight
            4. Price
            5. Expire days
            Please choose the key to sort:''')


            if int(sortingMethod) in range(1,6):
                sortedItemList = (sorted(ItemList, key = lambda x : x[ItemStruct[sortingMethod]]))
                with open(Foodlist,'w') as lst:
                    for i in sortedItemList:
                        if sortedItemList.index(i) == 0:
                            lst.write(str(i))
                        else:
                            lst.write("\n"+str(i))

                    lst.flush()
                print('Sorted by',ItemStruct[sortingMethod])
            else:
                print('invalid key to sort!')
            break

        except:
            print('invalid input, please choose again')
        
        # if sortingMethod == '1':
        #     sortedItemList = sorted(ItemList, key = lambda x : x['Item No.'])

        #     break
    
        # elif sortingMethod == '2':
        #     sortedItemList = sorted(ItemList, key = lambda x : x['name'])

        #     break
   
        # elif sortingMethod == '3':
        #     sortedItemList = (sorted(ItemList, key = lambda x : x['weight']))
        #     break

        # elif sortingMethod == '4':
        #     sortedItemList = (sorted(ItemList, key = lambda x : x['price']))

        #     break

        # elif sortingMethod == '5':
        #     sortedItemList = (sorted(ItemList, key = lambda x : x['expire days']))
        #     break

    # print("Calling Sort()")
            



def Summarize():        #done

    if os.path.exists(Foodlist):
        with open(Foodlist,'r') as lst:
            ItemList = list(lst.readlines())
            dictedItemlist=[]
            totalValue = 0
            for i in ItemList:
                # print(i)
                currentItem = dict(eval(i))
                dictedItemlist.append(currentItem)
                totalValue += currentItem['weight'] * currentItem['price']
            print('There are %d items in the database' %(len(ItemList)))
            print('The total value is $%.2f' % (totalValue))
    else:
        print('The lis is Empty')       
        return


def DisplayAll():       #done, need to add display 10 items per page
    print("\nHere are all the items\n===========================\n")
    if os.path.exists(Foodlist):

        with open(Foodlist,'r') as lst:
            ItemList = list(lst.readlines())
            print("Item No.     Name       Weight(kg)    Price($)    Expire days")
            for i in ItemList:
                # print(i)
                currentItem = dict(eval(i))
                print(f"{currentItem.get('Item No.'):<13}{currentItem.get('name'):<13}{currentItem.get('weight'):<13}{currentItem.get('price'):<13}{currentItem.get('expire days'):<10}")
    else:
        print('The list is empty!!!')

while True:
    menu()

    choice = input("Please choose what to do:")

    if choice == '1':
        Input()
    elif choice =='2':
        Search()
    elif choice =='3':
        Delete()
    elif choice =='4':
        Modify()
    elif choice =='5':
        SortItem()
    elif choice =='6':
        Summarize()
        input('\nPress "Enter" to continue')
    elif choice =='7':
        DisplayAll()
        input('\nPress "Enter" to continue')
    elif choice =='0':
        print('Bye~~!')
        break
    else:
        print("Invalid input, please input again!!")









