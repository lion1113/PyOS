# Imports
import sys

# Global Variables
Users = []
Passwords = []
LoggedUser = ""
ShellCommands = {"exit": "quit()"}


# Functions
def FetchLoginData():
    global Users
    global Passwords
    with open("Usernames", "r") as file:
        Users = file.read().split("\n")
    with open("Passwords", "r") as file:
        Passwords = file.read().split("\n")


def Login():
    FetchLoginData()
    while True:
        UserInput = input("Username: ")
        if UserInput not in Users:
            print("User not found. Please try again.\n")
            continue
        PasswordInput = input("Password: ")
        try:
            if Passwords.index(PasswordInput) != Users.index(UserInput):
                print("Password incorrect. Please try again.\n")
                continue
        except ValueError:
            print("Password incorrect. Please try again.\n")
            continue
        print("Welcome, " + UserInput)
        break


def PyShell():
    print("Welcome to PyShell!")
    while True:
        CommandInput = input(">>> ")
        try:
            exec(ShellCommands[CommandInput])
        except KeyError:
            print(CommandInput + " is not recognised as a valid command.")


# Main Script
try:
    Login()
    PyShell()
except KeyboardInterrupt:
    print("\nShutting down...")
    sys.exit()
