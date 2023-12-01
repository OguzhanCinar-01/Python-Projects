def encrypted():
    for x in message_list:
        shifted_message = chr(ord(x) + shift_number)
        if ord(x) + shift_number > 122:
            carry = ord(x) + shift_number - 122
            shifted_message = chr(96 + carry)
        shifted_message_list.append(shifted_message)
    print("".join(shifted_message_list))


def decrypted():
    for x in message_list:
        shifted_message = chr(ord(x) - shift_number)
        if ord(x) - shift_number < 97:
            carry = ord(x) - 96 - shift_number
            shifted_message = chr(122 + carry)
        shifted_message_list.append(shifted_message)
    print("".join(shifted_message_list))


program = True
while program:
    encrypted_decrypted = input("If you want to encrypt(e) or decrypt(d)? ")
    if encrypted_decrypted == "e":
        message = input("Type you message: ")
        message_list = []
        shifted_message_list = []
        for i in message:
            message_list.append(i)

        shift_number = int(input("Shift number: "))
        encrypted()
        exit = input("Do you want to exit?(y/n)")
        if exit == "y":
            program = False
        elif exit == "n":
            program = True
        else:
            print("Invalid digit please try again!")

    elif encrypted_decrypted == "d":
        message = input("Type encrypted message: ")
        message_list = []
        shifted_message_list = []
        for i in message:
            message_list.append(i)
        shift_number = int(input("Shift number: "))
        decrypted()

    else:
        print("Invalid letter. please try again!!")
