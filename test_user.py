import unittest

class BasicTests(unittest.TestCase):
    def login(self, username, password):
        response = self.register('henry@gmail.com', 'password')
        self.assertEqual(response.status_code, 200)

    def comment(self, username):
        pass

    def logout(self):
        return self.assertEquals(200)


 if __name__ == '__main__':
     unittest.main()

