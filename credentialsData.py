class credentialsData:
    """
    create new instances
    """

    credentials = []

    def __init__(self, platform, username, password):

        self.platform = platform
        self.username = username
        self.password = password

    @classmethod


    def save_credential(self):
        '''
        save credential objects to the credential list
        '''
        credentialsData.credentials.append(self)

    def displayCredentials(cls):

        for nick_name in cls.credentials:
                    
            return credentials
    def delete_credential(self):
        '''
        remove credential objects from credential list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_username(cls, name):
        '''
        method takes in the user name and returns a credential that matches it
        '''
        for credential in cls.credential_list:
            if credential.user_name == name:
                return credential

    @classmethod
    def credential_exist(cls, name):
        for credential in cls.credential_list:
            if credential.user_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def copy_user_name(cls, name):
        credential_found = Credential.find_by_username(name)
        pyperclip.copy(credential_found.user_name)
