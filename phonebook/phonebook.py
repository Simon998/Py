phonebook = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        print("Contact already exists")
    else:
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print("Contact added")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted")
    else:
        print("Contact not found")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in phonebook:
        print(f"Phone number for {name}: {phonebook[name]}")
    else:
        print("Contact not found")

def print_contacts():
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")

while True:
    print("\nPhonebook App")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search for contact")
    print("4. Print all contacts")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print_contacts()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
