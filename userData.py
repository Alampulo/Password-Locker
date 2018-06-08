class UserData:
    """
    """

    create_account = []

    def __init__(self, firstName, lastName, email, username, password, confirmPassword):
        
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password
        self.confirmPassword = confirmPassword

        @classmethod

    def save_account(cls):

        UserData.create_account.append(cls)

    