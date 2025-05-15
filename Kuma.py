kuma = [{"Name": "Mountain Dew", "Price": 20, "Quantity": 30},
        {"Name": "Nature Spring", "Price": 10, "Quantity": 14},
        {"Name": "Nescafe Original", "Price": 14, "Quantity": 17}]


def add():
    try:
        num = int(input("Enter how many times you want to input items: "))
        if num <= 10:
            for _ in range(num):
                name = str(input("\nProduct Name: "))
                try:
                    price = int(input("Price:"))
                    quan = int(input("Quantity: "))
                except ValueError:
                    print("Try Again...\n\n======================================== \n")
                    add()

                inventory = {
                    "Name": name,
                    "Price": price,
                    "Quantity": quan
                }
                kuma.append(inventory)

                print(f"\nSuccessfully added {name}.")
        else:
            print("Only 10 values can be entered!\n\n======================================== \n")
            add()

    except ValueError:
        print("Try Again...\n\n======================================== \n")
        add()

def delete():
    print("Select an Item to delete")
    for i, inventory in enumerate(kuma, start=1):
        print(f"{i}. Name: {inventory['Name']}, Price: {inventory['Price']}, Quantity: {inventory['Quantity']}")

    dl = input("\nSelect an Index Number: ")

    if dl.isdigit():
        x = int(dl)
        if 1 <= x <= len(kuma):
            ditem = kuma.pop(x - 1)
            print(f"Deleted {ditem['Name']} from Inventory.")
        else:
            print("Invalid Item Number...")
    else:
        print("Invalid Input...")

def update():

    print("\n\n========== UPDATE ==========")
    for i, inventory in enumerate(kuma, start=1):
        print(f"{i}. Name: {inventory['Name']}, Price: {inventory['Price']}, Quantity: {inventory['Quantity']}")

    c3 = input("\nWhat would you like to do?:\n\n"
               "1. Search by Name\n"
               "2. By Index Number\n\n"
               "Enter Choice: ")

    index = -1

    if c3 == "1":
        sname = input("Enter the product name: ").strip().lower()
        for i, item in enumerate(kuma):
            if item["Name"].lower() == sname:
                index = i
                break
        if index == -1:
            print("Item not found.")
            return
    elif c3 == "2":
        idinput = input("Enter index number: ")
        if idinput.isdigit():
            index = int(idinput) - 1
            if not (0 <= index < len(kuma)):
                print("Invalid index number.")
                return
        else:
            print("Invalid input. Please enter a number.")
            return
    else:
        print("Invalid choice.")
        return

    item = kuma[index]
    print(f"\nSelected Item: {item['Name']}, Price: {item['Price']}, Quantity: {item['Quantity']}")

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Price")
    print("3. Quantity")
    choice = input("Enter your choice: ")

    if choice == "1":
        nname = input("Enter new name: ")
        item["Name"] = nname
        print("Name updated successfully.")
    elif choice == "2":
        try:
            nprice = int(input("Enter new price: "))
            item["Price"] = nprice
            print("Price updated successfully.")
        except ValueError:
            print("Invalid price. Must be a number.")
    elif choice == "3":
        try:
            nquantity = int(input("Enter new quantity: "))
            item["Quantity"] = nquantity
            print("Quantity updated successfully.")
        except ValueError:
            print("Invalid quantity. Must be a number.")
    else:
        print("Invalid choice.")

def view():
    if not kuma:
        print("\nNo items in inventory.")
        return
    else:
        for i, inventory in enumerate(kuma, start=1):
            print(f"{i}. Name: {inventory['Name']}, Price: {inventory['Price']}, Quantity: {inventory['Quantity']}")

    vchoice = input("Would you like to sort? Y/N: ").upper()

    if vchoice == "Y":
        while True:
            print("\nHow would you like to sort the items?")
            print("1. Sort by Name")
            print("2. Sort by Price")
            print("3. Sort by Quantity")
            print("4. View without sorting")
            print("5. Return to Main Menu")

            schoice = input("Enter your choice (1-5): ")

            if schoice == "5":
                break

            r = False
            if schoice in ["1", "2", "3"]:
                print("\nChoose sort order:")
                print("1. Ascending (A-Z or 1-N)")
                print("2. Descending (Z-A or N-1)")
                order = input("Enter your choice (1-2): ")
                if order == "2":
                    r = True
                elif order != "1":
                    print("Invalid order choice. Defaulting to Ascending.")

            if schoice == "1":
                sk = sorted(kuma, key=lambda x: x["Name"].lower(), reverse=r)
            elif schoice == "2":
                sk = sorted(kuma, key=lambda x: x["Price"], reverse=r)
            elif schoice == "3":
                sk = sorted(kuma, key=lambda x: x["Quantity"], reverse=r)
            elif schoice == "4":
                sk = kuma[:]
            else:
                print("Invalid sort option. Please try again.")
                continue

            print("\nStored Item(s):")
            for i, inventory in enumerate(sk, start=1):
                print(f"{i}. Name: {inventory['Name']}, Price: {inventory['Price']}, Quantity: {inventory['Quantity']}")
    else:
        return None
while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. View Item")
    print("4. Update")
    print("5. Exit")

    c = int(input("Enter your choice: "))

    if c == 1:
        add()
    elif c == 2:
        delete()
    elif c == 3:
        view()
    elif c == 4:
        update()
    elif c == 5:
        print("\nENDING PROGRAM...")
        exit()
    else:
        print("You can only choose 1-4!!!")

