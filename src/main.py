import re
"""
 i used "https://github.com/STRstark/Ds-Classes-In-Python/blob/main/DataStructures-Py/Project/Project.py" for initial structure 
 with some change in pre initialize the tree with the first two digits of a phone number in way to 
 Flexibility and Dynamic Tree Construction .

 Matin Mohammadi : 40011173069

"""
class Contact:
    def __init__(self, full_name, nickname, phone_number, email, job_info):
        self.full_name = full_name
        self.nickname = nickname
        self.phone_number = phone_number
        self.email = email
        self.job_info = job_info

    def __str__(self):
        return f"Name: {self.full_name} ({self.nickname})\nPhone: {self.phone_number}\nEmail: {self.email}\nJob: {self.job_info}"
    
    @staticmethod
    def get_contact_details():

        # Validate full name 
        while True:
            full_name = input("Enter full name: ").strip()
            if re.match(r'^[A-Za-z\s]+$', full_name):  # letters and spaces allowed
                break
            print("Invalid name. Please enter only alphabetic characters and spaces.")

        nickname = input("Enter nickname (optional): ").strip()

        # Validate phone number 
        phone_number = PhoneNumberTree.get_valid_phone_number()

        # Validate email 
        while True:
            email = input("Enter email: ").strip()
            if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):  # Basic email format check
                break
            print("Invalid email format. Please enter a valid email.")

    
        while True:
            job_info = input("Enter job info: ").strip()
            if job_info:  # Ensure job info is not empty
                break
            print("Job info cannot be empty. Please enter your job info.")

        return Contact(full_name, nickname, phone_number, email, job_info)
    

class TreeNode:
    def __init__(self):
        self.children = {}  
        self.is_end_of_number = False  
        self.contact = None  

class PhoneNumberTree:
    def __init__(self):
        self.root = TreeNode()  

    @staticmethod
    def get_valid_phone_number():

        while True:
            phone_number = input("Enter phone number (11 digits): ").strip()
            if re.match(r'^\d{11}$', phone_number):  # Validate phone number format
                return phone_number
            print("Invalid phone number format. Please enter exactly 11 digits.")

    def insert(self, contact):
        """
        Insert a contact into the tree.
        """
        if not contact:
            print("Error: Contact object is None.")
            return False

        phone_number = contact.phone_number  

        # Check if the phone number already exists in the tree
        if self.search(phone_number):
            print(f"Error: A contact with the phone number '{phone_number}' already exists.")
            return False

        # Insert the new contact
        current_node = self.root
        for digit in phone_number:
            if digit not in current_node.children:
                current_node.children[digit] = TreeNode()
            current_node = current_node.children[digit]

        current_node.is_end_of_number = True
        current_node.contact = contact
        print(f"Contact '{contact.full_name}' added successfully!")
        return True

    def search(self, phone_number):
        """
        Search for a contact by phone number.
        """
        current_node = self.root
        for digit in phone_number:
            if digit not in current_node.children:
                print("Contact not found.")
                return None
            current_node = current_node.children[digit]

        if current_node.is_end_of_number:
            return current_node.contact
        else:
            print("Contact not found.")
            return None

    def update(self, phone_number, new_contact_updates):
        """
        Update a contact's information.
        """
        current_node = self.root
        for digit in phone_number:
            if digit not in current_node.children:
                print("Contact not found.")
                return False
            current_node = current_node.children[digit]

        if current_node.is_end_of_number:
            current_node.contact = new_contact_updates
            print(f"Contact '{new_contact_updates.full_name}' updated successfully!")
            return True
        else:
            print("Contact not found.")
            return False

    def delete(self, phone_number):
        """
        Delete a contact by phone number.
        """
        current_node = self.root
        for digit in phone_number:
            if digit not in current_node.children:
                print("Contact not found.")
                return False
            current_node = current_node.children[digit]

        if current_node.is_end_of_number:
            current_node.is_end_of_number = False
            current_node.contact = None
            print("Contact deleted successfully!")
            return True
        else:
            print("Contact not found.")
            return False

def main():
    tree = PhoneNumberTree()

    while True:
        print("\n------------- Phone Contact Management System -------------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAdd New Contact:")
            contact = Contact.get_contact_details()
            tree.insert(contact)

        elif choice == "2":
            print("\nSearch Contact:")
            phone_number = PhoneNumberTree.get_valid_phone_number()
            contact = tree.search(phone_number)
            if contact:
                print("\nContact Found:")
                print(contact)

        elif choice == "3":
            print("\nUpdate Contact:")
            phone_number = PhoneNumberTree.get_valid_phone_number()  
            print("Enter new contact details:")
            new_contact_updates = Contact.get_contact_details()
            tree.update(phone_number, new_contact_updates)

        elif choice == "4":
            print("\nDelete Contact:")
            phone_number = PhoneNumberTree.get_valid_phone_number()  
            tree.delete(phone_number)

        elif choice == "5":
            print("Exiting the program. Goodbye dear user!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()