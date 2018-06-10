#!/usr/bin/env python3.6

import random
import string

from userData import UserData
from credentialsData import CredentialsData



def new_user(name_one, name_two, email_address, user_name, pseudo_name, pass_word, confirm_password):

    """
    creates new user 
    """
    new_user = UserData(name_one, name_two, email_address, user_name, pseudo_name, pass_word, confirm_password)
    
    return new_user

def save_accounts(account):
    """
    save new user account
    """
    account.save_account()

def check_user(used_name, used_password):
    """
    checks if user exists
    """
    user_exists = UserData.user_login(used_name, used_password)

    return user_exists

def add_credential(acc, acc_name, acc_password):
    """
    adds a credential
    """
    added_credential = CredentialsData(acc, acc_name, acc_password)

    return added_credential

def save_credentials(credential):
    """
    saves created credential
    """
    credential.save_credential()

def randompassword():
    """
    generates a random password
    """

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    password = ''.join(random.choice(chars) for x in range(size))

    return password

def display_credentials():
    """
    returns the saved credential
    """
    return CredentialsData.display_credentials()

def delete_credentials(credential):
    """
    delete a credential
    """
    credential.delete_credential()

def main():
    print("Hello, welcome to Password Locker.")
    print("-" * 50)

    while True:
        print(
            "Type 'new' to create and account or 'login' to log in to an existing account.")
        code = input().lower()

        if code == "new":
            print("User name....")
            login_name = input()
            print('\n')

            print(
                "Options: Create your password - 'create'; get generated password - 'gen'")
            option = input()
            while True:
                if option == "create":
                    print("Password....")
                    password = input()
                    break
                elif option == "gen":
                    password = generate_password()
                    print('\n')
                    break
                else:
                    print("Not recognized. Please use one of the codes.")
                    break

            save_user(create_user(login_name, password))
            print(f"Account created successfully. User name: {login_name}, password: {password}. You are currently logged in.")
            print('\n')
            break

        elif code == "login":
            print("Log In")
            print("-"*30)

            print("User name....")
            login_name = input()
            print('\n')

            print("Account password....")
            password = input()
            print('\n')

            sign_in = auth_user(login_name, password)

            if sign_in == True:
                break
            print("Username or password not recognized. Please try again.")
            print('\n')

        else:
            print('\n')
            print("Not recognized. Please use one of the codes.")
            print('\n')

    while True:
            print(f"Please use the following codes to navigate: 'add' - add new credentials, 'list' - show all stored credentials, 'find' - find specific credentials, 'exit' - leave.")

            short_code = input().lower()

            if short_code == 'add':
                    print("New Credentials")
                    print("-" * 10)

                    print("To which website does this account belong?")
                    w_site = input()

                    print("Username....")
                    u_name = input()

                    print("Password....")
                    p_word = input()

                    # create and save new cred
                    save_credentials(create_credential(w_site, u_name, p_word))
                    print('\n')
                    print(f"New Credential created: {w_site}: {u_name} -- {p_word}")
                    print('\n')

            elif short_code == 'list':
                    if display_credentials():
                            print("Here is a list of all your credentials:")
                            print('\n')

                            for credential in display_credentials():
                                    print(f"{credential.website}: {credential.user_name} -- {credential.password}")
                            print('\n')
                    else:
                            print('\n')
                            print("You do not have any credentials saved yet.")
                            print('\n')

            elif short_code == 'find':
                    print("Enter the user name you want to search for.")

                    search_name = input()
                    if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print('\n')
                            print(f"{credential.website}: {search_credential.user_name} -- {search_credential.password}")
                            print('\n')
                    else:
                        print('\n')
                        print(
                            "That credential cannot be found. Please check your spelling and try again.")
                        print('\n')

            elif short_code == 'exit':
                    print("Goodbye...")
                    break
            else:
                print('\n')
                print("Not recognized. Please use one of the short codes.")
                print('\n')


if __name__ == '__main__':
    main()
                                                                                                                                 
