from cabecalho import cabecalho


try:
    # Creat a file text, if It doesn't exist
    with open("phonebook.txt", "x") as file:
        file.write("Name Phone Number\n")

except FileExistsError:
    # If exist, append what we will write
    with open("phonebook.txt", "a") as file:
        opc = 0
        while opc != 4:
            cabecalho("TELEPHONE BOOK")
            print(
                "[1]-Add contact \n\033[31m[2]-Delete contact\033[m \n[3]-Contact list \n[4]-Close the telephone book")
            opc = int(input("Options: "))

            if opc == 1:
                how_many_contact = int(input("How many contact you want to add in Telephone Book? "))
                for c in range(0, how_many_contact):
                    name = input(f"[{c + 1}] Name: ").capitalize()
                    phone_number = input(f'[{c + 1}] Phone number: ')
                    file.write(f"[{c+1}] {name:<15}")
                    file.write(f'{phone_number}\n')

            elif opc == 2:
                opc2 = 0
                while opc2 != 3:
                    print("\033[32mFirst, type the contact number you want to delete or choos option below\033[m")
                    print("\t[1] - Consult contact list to see the numbers\n"
                          "\t[2] - I know the contact number \n\t[3] - Cancel option")
                    opc2 = int(input("Options: "))

                    if opc2 == 1:
                        with open("phonebook.txt", "r") as file:
                            cabecalho("CONTACT LIST")
                            print(file.read())
                            file.close()

                    elif opc2 == 2:
                        contact_number = int(input("Type the contact number you want to delete: (or type)"))
                        try:
                            with open("phonebook.txt", "r") as file:
                                lines = file.readlines()

                                pointer = 1

                                with open("phonebook.txt", "w") as file:
                                    for line in lines:
                                        if pointer != contact_number+1:
                                            file.write(line)
                                        pointer += 1
                                print("Contact deleted")
                        except:
                            print("Write the a true number!")

                    elif opc2 == 3:
                        break
                    else:
                        print("\033[31mInvalid option!\033[m")

            elif opc == 3:
                with open("phonebook.txt", "r") as file:
                    cabecalho("CONTACT LIST")
                    print(file.read())
                    file.close()

            elif opc == 4:
                break

            else:
                print("\033[31mInvalid option! \nType again...\033[m")
