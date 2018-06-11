import unittest
from userData import UserData

class TestuserData(unittest.TestCase):
    def setUp(self):
        """
        set up method
        """
        self.new_user = UserData("cliff", "kasera", "ckasera@gmail.com", "Blankphrase" "lololo") 

    def test_init(self):
        """
        testing initialization of class
        """
        self.assertEqual(self.new_user.firstName, "cliff")
        self.assertEqual(self.new_user.lastName, "kasera")
        self.assertEqual(self.new_user.email, "ckasera@gmail.com")
        self.assertEqual(self.new_user.username, "Blankphrase")
        self.assertEqual(self.new_user.password, "lololo")

    def tearDown(self):
        """
        restart
        """
        UserData.create_account = []

    def test_save_account(self):
        """
        testing save account method
        """
        self.new_user.save_account() 
        self.assertEqual(len(UserData.create_account), 1)


if __name__ == '__main__':
    unittest.main()
