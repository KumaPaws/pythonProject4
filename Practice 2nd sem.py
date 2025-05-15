people = []

num_people= int(input("How many people do you want to enter?: "))

for _ in range(num_people):
    name = input("\nEnter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender M/F: ")

    person = {"\nName": name, "Age": age, "Gender": gender}
    people.append(person)

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("\n==========\n",)