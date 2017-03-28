"""

Tej V Labs Product (c) 2017
Written by Tejaswi Vemulapati
FamChat Server Side Code

"""

import sys
import random
from threading import *
userNames = []  # User Name Database for all users
passWords = []  # Password Database for all users
users = []  # User Database for all user objects
familys = []    # Family Databse storing data structures for all families

class User:
    userName = str
    passWord = str
    profileImageName = str
    age = int
    def _init_(self, userName, passWord, profileImageName, age):
        self.userName = userName
        self.passWord = passWord
        self.profileImageName = profileImageName
        self.age = age
        print("[FamChat] User Object Initiated")

def clearPasswordLogin(userEntry, passWord):
    for index in range(0, len(userNames)):
        if userNames[index] == userEntry:
            if passWords[index] == passWord:
                return True
            else:
                return False
    print("[FamChat] User Grant Access Login")
    # Will Grant Clearance for Password Login
def createNewUser(userName, passWord, age, profileImageName):
    userNames.append(userName)
    passWords.append(passWord)
    newUser = User(userName, passWord, age, profileImageName)
    users.append(newUser)
    print("[FamChat] New User Created")
