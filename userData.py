class UserData:

    '''
    class to create new user accounts 
    '''

    create_account = []

    def __init__(self, firstName, lastName, email, username, password):

        """
        Initializes the class
        """

        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password

    def save_account(self):

        """
        saves the new user to create_account list
        """

        UserData.create_account.append(self)

    @classmethod
    def user_login(cls, used_name, used_password):
        """
        checks whether user exists
        """
        for user in UserData.create_account:
            if user.username == used_name and user.password == used_password:
                return user
            return False
