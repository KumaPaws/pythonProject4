Name = ['Kasilag', 'Tristan', 'Jan']
Age = [23,18,18]
Gender = ['M', 'M', 'M']


def main():
    print("Hello!! Welcome to the Inventory!!")
    print("What would you like to do?\n")

    print("1. ADD\n2. DELETE\n3. VIEW\n")

    o1 = int(input("What would you like to do?: "))

    if o1 == 1:
        add()
    elif o1 == 2:
        delete()
    elif o1 == 3:
        view()
    else:
        print("End of Program")
        exit()

def add():
    i = 0
    while i <= 10:
        Name.append(input("Add Name: "))
        Age.append(input("Add Age: "))
        Gender.append(input("Add Gender: "))

        o2 = input("Would you like to enter again? Y/N: ").upper()

        if o2 == "Y":
            continue
        else:
            main()
    i+=1
def delete():
    print()
def view():

    i = 0

    while i <= Name:

        i+=1
        c3 = input("Would you like to go back? Y/N: ").upper()
        if c3 == "Y":
            main()
        else:
            exit()

main()