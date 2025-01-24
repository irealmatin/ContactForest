import unittest
from main import Contact,  PhoneNumberTree  

class TestPhoneContactSystem(unittest.TestCase):
    def setUp(self):
        self.tree = PhoneNumberTree()
        self.contact1 = Contact("matin mohamadi", "monfared", "09123156789", "matin@example.com", "Builder")
        self.contact2 = Contact("mohmadreza fathi", "samani", "09123156788", "mohmadreza@example.com", "TA")

    def test_insert_contact(self):

        self.assertTrue(self.tree.insert(self.contact1))
        self.assertTrue(self.tree.insert(self.contact2))

    def test_insert_none_contact(self):

        self.assertFalse(self.tree.insert(None))  

    def test_duplicate_phone_number(self):
  
        self.assertTrue(self.tree.insert(self.contact1))

        duplicate_contact = Contact("ali ahmadi", "ali", "09123156789", "ali@example.com", "engineer")
        self.assertFalse(self.tree.insert(duplicate_contact))

    def test_search_contact(self):

        self.tree.insert(self.contact1)
        self.tree.insert(self.contact2)

        # Search for an existing contact
        found_contact = self.tree.search("09123156789")
        self.assertIsNotNone(found_contact)
        self.assertEqual(found_contact.full_name, "matin mohamadi")

        # Search for a non-existing contact
        non_existing_contact = self.tree.search("09123456789")
        self.assertIsNone(non_existing_contact)

    def test_update_contact(self):
 
        self.tree.insert(self.contact1)

        # Update the contact
        updated_contact = Contact("matin mohamadi", "matin_new", "09123156789", "matin_new@example.com", "Product Manager")
        self.assertTrue(self.tree.update("09123156789", updated_contact))

        # Verify the update
        found_contact = self.tree.search("09123156789")
        self.assertIsNotNone(found_contact)
        self.assertEqual(found_contact.nickname, "matin_new")
        self.assertEqual(found_contact.email, "matin_new@example.com")

        # Try updating a non-existing contact
        non_existing_contact = Contact("Non Existing", "None", "09123456789", "none@example.com", "None")
        self.assertFalse(self.tree.update("09123456789", non_existing_contact))

    def test_delete_contact(self):

        self.tree.insert(self.contact1)
        self.tree.insert(self.contact2)

        # Delete an existing contact
        self.assertTrue(self.tree.delete("09123156789"))

        # Verify the contact is deleted
        found_contact = self.tree.search("09123156789")
        self.assertIsNone(found_contact)

        # Try deleting a non-existing contact
        self.assertFalse(self.tree.delete("09123456789"))

    def test_contact_str_representation(self):

        contact = Contact("matin mohamadi", "matin", "09123156789", "matin@example.com", "Builder")
        expected_output = (
            "Name: matin mohamadi (matin)\n"
            "Phone: 09123156789\n"
            "Email: matin@example.com\n"
            "Job: Builder"
        )
        self.assertEqual(str(contact), expected_output)

if __name__ == "__main__":
    unittest.main()