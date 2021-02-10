import unittest
import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.obj = user.User()

    def tearDown(self):
        pass

    def test_init(self):
        alex = user.User("Alex",56)
        self.assertEqual(alex.name, "Alex")
        self.assertEqual(alex.age, 56)

        bob = user.User("Bob")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.age, 35)

        self.assertEqual(self.obj.name, "Bot")
        self.assertEqual(self.obj.age, 35)

    def test_printAll(self):
        self.assertEqual(self.obj.printAll(), "Bot возрастом 35")

    def test_printToFile(self):
        self.obj.printToFile('text.txt')
        res = self.obj.readFromFile('text.txt')
        self.assertEqual(res, self.obj.printAll())


if __name__ == '__main__':
    unittest.main()