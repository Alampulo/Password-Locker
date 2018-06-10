import random
import string

global create_account


class UserData:

    '''
    class to create new user accounts 
    '''

    create_account = []

    def __init__(self, firstName, lastName, email, username, nick_name, password, confirmPassword):

        """
        Initializes the class
        """

        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.nick_name = nick_name
        self.password = password
        self.confirmPassword = confirmPassword

    def save_account(self):

        """
        saves the new user to create_account list
        """

        UserData.create_account.append(self)

    
    @classmethod

    def user_login(cls, username, password):

        """
        authenticates the user 
        """

        for user in UserData.create_account:
            if user.username == username and user.password == password:
                return user
            return False

    def randompassword():

        """
        generates a random password
        """

        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits   
        size = random.randint(8, 12)
        password = ''.join(random.choice(chars) for x in range(size))
     
        return password
 
