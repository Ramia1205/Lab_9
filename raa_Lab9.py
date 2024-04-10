def encode(password):
    encoded = ""
    for element in password:
        if element == "0":
            encoded += "3"
        elif element == "1":
            encoded += "4"
        elif element == "2":
            encoded += "5"
        elif element == "3":
            encoded += "6"
        elif element == "4":
            encoded += "7"
        elif element == "5":
            encoded += "8"
        elif element == "6":
            encoded += "9"
        elif element == "7":
            encoded += "0"
        elif element == "8":
            encoded += "1"
        elif element == "9":
            encoded += "2"
    return (encoded)


def decode(n):
    decoded = []
    for number in str(n):
        number = int(number) - 3
        if number >= 10:
            decoded.append(number - 10)
        else:
            decoded.append(number)
    return decoded


def main():

    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        if option == 2:
            print(f"The decoded password is {encoded_password}, and the original password is {password}.")

        if option == 3:
            break


if __name__ == "__main__":
    main()