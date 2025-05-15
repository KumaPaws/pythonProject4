
def d_to_b(dnumber):
    if dnumber == 0:
        return "0"

    binarydigits = []
    while dnumber > 0:
        r = dnumber % 2
        binarydigits.insert(0, str(r))
        dnumber = dnumber // 2

    return ''.join(binarydigits)

def main():
    d_input = input("Enter a non-negative decimal number: ")

    if d_input.isdigit():
        dnumber = int(d_input)
        boutput = d_to_b(dnumber)
        print("Binary: ", boutput)
    else:
        print("Invalid Input.")

main()

#=========================================================================

