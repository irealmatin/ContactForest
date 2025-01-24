# 📞 ContactForest: Phone Contact Management System 

Welcome to **ContactForest**, a simple  phone contact management system built using a custom tree data structure. This project allows you to efficiently store, search, update, and delete contacts while ensuring fast and optimized operations.

---

##  Features

- **Tree-Based Storage**: Each digit of a phone number is stored as a node in the tree, ensuring efficient storage and retrieval.

- **Fast Operations**: Insertion, search, update, and deletion operations are performed in **O(d)** time, where **d** is the number of digits in the phone number.


---

##  How It Works

1. **Tree Structure**:
   - Each node in the tree represents a digit (0-9).
   - The path from the root to a leaf node represents a complete phone number.
   - Leaf nodes store contact information (name, email, job info, etc.).

2. **Operations**:
   - **Add Contact**: Insert a new contact into the tree.
   - **Search Contact**: Find a contact by their phone number.
   - **Update Contact**: Modify the details of an existing contact.
   - **Delete Contact**: Remove a contact from the tree.

---

##  Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/irealmatin/ContactForest.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ContactForest
   ```

### Running the Program
1. Run the main script:
   ```bash
   python main.py
   ```
2. Follow the on-screen instructions to manage your contacts.

---

##  Testing

To run the test cases, use the following command:
```bash
python -m unittest test_main.py
```

---

##  Project Structure

- `main.py`: The main script to run the contact management system.
- `test_main.py`: Test cases for the system.
- `README.md`: This file.

---

##  Example Usage

### Adding a Contact
```
Enter full name: jane hardi
Enter nickname (optional): jane
Enter phone number (11 digits): xxxxxxxxxxx
Enter email: jane@example.com
Enter job info: student
Contact 'jane hardi' added successfully!
```

### Searching for a Contact
```
Enter phone number to search (11 digits): xxxxxxxxxxx
Contact Found:
Name: jane hardi (jane)
Phone: xxxxxxxxxxx
Email: jane@example.com
Job: student
```

### Updating a Contact
```
Enter phone number to update (11 digits): xxxxxxxxxxx
Enter new contact details:
Enter full name: jane hardi
Enter nickname (optional): jane_lor
Enter phone number (11 digits): xxxxxxxxxxx
Enter email: jane@example.com
Enter job info: senior student
Contact 'jane hardi' updated successfully!
```

### Deleting a Contact
```
Enter phone number to delete (11 digits): xxxxxxxxxxx
Contact deleted successfully!
```

---

