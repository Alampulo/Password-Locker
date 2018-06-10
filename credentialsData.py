class CredentialsData:

    """
    create new instances
    """

    credentials = []

    def __init__(self, platform, username, password):

        self.platform = platform
        self.username = username
        self.password = password

    def save_credential(self):

        """
        save credential objects to the credential list
        """
        CredentialsData.credentials.append(self)

    @classmethod

    def display_credentials(cls):

        """
        displays the credentials 
        """
        return cls.credentials
        
    @classmethod

    def delete_credential(cls):

        """
        deletes credential from credentials list
        """
        CredentialsData.credentials.remove(cls)  