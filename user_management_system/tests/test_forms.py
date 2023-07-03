```python
import unittest
from user_management_system.forms import AddUserForm, EditUserForm

class TestForms(unittest.TestCase):

    def test_add_user_form_valid(self):
        form = AddUserForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com'
        })
        self.assertTrue(form.is_valid())

    def test_add_user_form_invalid(self):
        form = AddUserForm(data={})
        self.assertFalse(form.is_valid())

    def test_edit_user_form_valid(self):
        form = EditUserForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com'
        })
        self.assertTrue(form.is_valid())

    def test_edit_user_form_invalid(self):
        form = EditUserForm(data={})
        self.assertFalse(form.is_valid())

if __name__ == "__main__":
    unittest.main()
```