class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        self.contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully!")

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("------------------------")

    def search_contact(self):
        name = input("Enter name to search: ")
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone: {self.contacts[name]['phone']}")
            print(f"Email: {self.contacts[name]['email']}")
        else:
            print("Contact not found!")

    def update_contact(self):
        name = input("Enter name to update: ")
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            self.contacts[name] = {"phone": phone, "email": email}
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        name = input("Enter name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

def main():
    contact_book = ContactBook()
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()