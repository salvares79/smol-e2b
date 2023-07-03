```python
import unittest
from user_management_system.models import User, UserSchema

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.user = User("John Doe", "john.doe@example.com", "password")
        self.user_schema = UserSchema()

    def test_create_user(self):
        data = self.user_schema.dump(self.user)
        self.assertEqual(data['name'], "John Doe")
        self.assertEqual(data['email'], "john.doe@example.com")

    def test_edit_user(self):
        self.user.name = "Jane Doe"
        data = self.user_schema.dump(self.user)
        self.assertEqual(data['name'], "Jane Doe")

    def test_delete_user(self):
        del self.user
        self.assertIsNone(self.user, None)

if __name__ == '__main__':
    unittest.main()
```