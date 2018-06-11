#!/usr/bin/env python3.6

import random
import string

from userData import UserData
from credentialsData import CredentialsData



def new_users(name_one, name_two, email_address, user_name, pass_word):

    """
    creates new user 
    """
    new_user = UserData(name_one, name_two, email_address, user_name, pass_word)
    
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

def display_credential():
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
    print("\n")
    print("Welcome to Password Locker")
    print("This will store your credentails and generate a password for you")

    while True:
        print("Type register to create account. If you already created one, type signin.")
        account_login = input().lower()
        if account_login == "register":
            print("First name:")
            firstname = input()
            print('\n')
            print("Last name:")
            lastname = input()
            print('\n')
            print("Username:")
            username = input()
            print('\n')
            print("email:")
            emails = input()
            print('\n')
            print("To create a password, type create or to generate a password type generate")
            pass_choice = input()
            while True:
                if pass_choice == "create":
                    print("Password:")
                    password = input()
                    break
                elif pass_choice == "generate":
                    password = randompassword()
                    print('\n')
                    break
                else:                    
                    print("Type create or 'generate")
                    break
            save_accounts(new_users(firstname, lastname, emails, username, password))
            print("Created successfully.")
            print(f" Username: {username}, password: {password}.")
            print('\n')
            break

        elif account_login == "signin":
            print("Sign In:\n")
            print("Username:")
            username = input()
            print('\n')
            print("Password:")
            password = input()
            print('\n')
            sign_in = check_user(username, password)
            if sign_in == True:
                break
            print("Please sign up to access password locker.\n")

        else:
            print("Try the choices above")

    while True:
        print(f"Type create to add a credential, saved to see the saved credentials or exit to stop adding credentials.")

        credentials2 = input().lower()

        if credentials2 == 'create':
            print("Type platform to add:")
            plat_form = input()
            print("\n")

            print("Type in username for the platform:")
            username2 = input()

            print("Type in password for the platform:")
            password2 = input()

            print("To create a password, type create or to generate a password type generate")
            pass_choice = input()
            while True:
                if pass_choice == "create":
                    print("Password:")
                    password2 = input()
                    break
                elif pass_choice == "generate":
                    password2 = randompassword()
                    print('\n')
                    break
                else:
                    print("Type create or 'generate")
                    break

            save_credentials(add_credential(plat_form, username2, password2))
            print('\n')
            print(f" {plat_form}: {username2}: {password2}")
            print('\n')

        elif credentials2 == 'saved':
            if display_credential():
                print("Credentials:\n")
                for credential in display_credential():
                    print(f"Platform => {credential.platform}: Username => {credential.username}: Password => {credential.password}")
                    print('\n')
                else:
                    print("There are no more credentials saved for now. Type create to create a credential.")
                    print('\n')

        elif credentials2 == 'exit':
                    break
        else:
            print("Sorry, try again.")
            print('\n')


if __name__ == '__main__':
    main()
                                                                                                                                 
