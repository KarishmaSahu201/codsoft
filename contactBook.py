class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. Name: {contact.name}")
            print(f"   Phone: {contact.phone}")
            print(f"   Email: {contact.email}")
            print(f"   Address: {contact.address}")
            print()

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        return results

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added!")

        elif choice == "2":
            print("\nContact List:")
            contact_book.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(keyword)
            if results:
                print("\nSearch results:")
                for i, contact in enumerate(results, 1):
                    print(f"{i}. Name: {contact.name}")
                    print(f"   Phone: {contact.phone}")
                    print(f"   Email: {contact.email}")
                    print(f"   Address: {contact.address}")
                    print()
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))-1
            if 0 <= index < len(contact_book.contacts):
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                updated_contact = Contact(name, phone, email, address)
                contact_book.update_contact(index, updated_contact)
                print("Contact updated!")
            else:
                print("Invalid index.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))-1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("Contact deleted!")
            else:
                print("Invalid index.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
