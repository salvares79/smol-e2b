```python
import unittest
from user_management_system.views import addUser, editUser, deleteUser, viewUsers, viewUser

class TestViews(unittest.TestCase):

    def setUp(self):
        self.userList = []

    def test_addUser(self):
        addUser(self.userList, 'Test User')
        self.assertEqual(len(self.userList), 1)

    def test_editUser(self):
        addUser(self.userList, 'Test User')
        editUser(self.userList, 0, 'Edited User')
        self.assertEqual(self.userList[0], 'Edited User')

    def test_deleteUser(self):
        addUser(self.userList, 'Test User')
        deleteUser(self.userList, 0)
        self.assertEqual(len(self.userList), 0)

    def test_viewUsers(self):
        addUser(self.userList, 'Test User 1')
        addUser(self.userList, 'Test User 2')
        users = viewUsers(self.userList)
        self.assertEqual(len(users), 2)

    def test_viewUser(self):
        addUser(self.userList, 'Test User')
        user = viewUser(self.userList, 0)
        self.assertEqual(user, 'Test User')

if __name__ == '__main__':
    unittest.main()
```