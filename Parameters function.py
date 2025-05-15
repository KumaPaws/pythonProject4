def add(a, b):
    return a + b

print(add(2, 3))

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
def greet(name = ""):
    print(f"\nHello, {name}!")

def main():
    name = input("Enter Name: ")
    greet(name)
main()

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

def total(*args):
    return sum(args)

print("\n",total(1, 2, 3, 4))

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"\n{key}: {value}")

print_info(name = "Alice", Age = 25)
