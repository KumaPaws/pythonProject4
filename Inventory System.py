def main():
    print("Hello!! Welcome to the Student Record Management System!")
    print("What would you like to do?\n")
    print("1. ADD\n2. DELETE\n3. VIEW\n4. UPDATE\n5. EXIT")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add()
    elif choice == "2":
        delete()
    elif choice == "3":
        view()
    elif choice == "4":
        update()
    else:
        print("End of Program.")
        exit()

def add():
    while True:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        sid = input("Enter Student ID: ")

        with open("students.txt", "a") as file:
            file.write(f"{sid},{name},{age},{gender}\n")

        again = input("Would you like to add another student? (Y/N): ").upper()
        if again != "Y":
            break
    main()

def delete():
    sid = input("Enter Student ID to delete: ")
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
        with open("students.txt", "w") as file:
            for line in lines:
                if not line.startswith(sid + ","):
                    file.write(line)
        print("Deleted if student existed.\n")
    except FileNotFoundError:
        print("No student records found.\n")
    main()

def view():
    try:
        file = open("students.txt", "r")
        lines = file.readlines()
        file.close()

        if lines == []:
            print("No student records found.\n")
            main()
            return
    except:
        print("No students record yet.\n")
        main()
        return

print("\n1. View All Students\n2. Search by Student ID")

option = input("Choose an option (1 or 2): ")
def update():
    sid_to_update = input("Enter Student ID to update: ")
    updated = False
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
        with open("students.txt", "w") as file:
            for line in lines:
                sid, name, age, gender = line.strip().split(",")
                if sid == sid_to_update:
                    print(f"Current Info - Name: {name}, Age: {age}, Gender: {gender}")
                    new_name = input("Enter new name: ")
                    new_age = input("Enter new age: ")
                    new_gender = input("Enter new gender (M/F): ")
                    file.write(f"{sid},{new_name},{new_age},{new_gender}\n")
                    updated = True
                else:
                    file.write(line)
        if updated:
            print("Student record updated.\n")
        else:
            print("Student ID not found.\n")
    except FileNotFoundError:
        print("No student records found.\n")
    main()

main()