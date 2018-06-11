import unittest

from credentialsData import CredentialsData


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_credential = CredentialsData("Gmail", "cliff", "lolololo") 

    def test_init(self):
        """
        testing initialization
        """
        self.assertEqual(self.new_credential.platform, "Gmail")
        self.assertEqual(self.new_credential.username, "cliff")
        self.assertEqual(self.new_credential.password, "lolololo")

    def tearDown(self):
    
        CredentialsData.credentials = []

    def test_save_credential(self):
        """
        test if credential is saved in the credentials list
        """
        self.new_credential.save_credential()  
        self.assertEqual(len(CredentialsData.), 1)

    def test_delete_credential(self):
        """
        test delete_credential method
        """
        self.new_credential.save_credential()
        test_credential = CredentialsData("Gmail", "cliff", "lolololo")
        test_credential.save_credential()

        self.new_credential.delete_credential() 
        self.assertEqual(len(CredentialsData.credentials), 1)

    def test_display_credentials(self):
        """
        test display credentials method
        """
        self.assertEqual(CredentialsData.display_credentials(),CredentialsData.credentials)

if __name__ == '__main__':
    unittest.main()
