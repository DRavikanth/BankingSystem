import peewee
from peewee import *
import sys

db = peewee.SqliteDatabase('internet_banking.db')

#Creating the models for the project
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user = CharField(unique=True)
    dob = CharField()
    gender = CharField()
    address = CharField()    
    
class Funds(BaseModel):
    user = ForeignKeyField(User, backref='funds')
    amount = DoubleField()


def create_user():
    name = raw_input("Please enter your name:")
    date_of_birth = raw_input("Please enter your date of birth:")
    gender = raw_input("Please enter your gender:")
    address = raw_input("Please enter your address:")
    

def balance_check():
    print "Checking Balance"

def withdrawal():
    print "Withdrawing amount"

def deposit():
    print "Depositing amount"


def existing_user():
    existing_user_message()
    
    
    
def existing_user_message():
    print """
        Thanks for your confirmation. Please choose from the following options:
            a. Check Balance
            b. Withdrawal
            c. Deposit
            d. Quit
    """
    banking_choice = raw_input("Please enter your choice:")
    banking_choice = banking_choice.lower()
    
    if banking_choice == 'a':
        balance_check()
    elif banking_choice == 'b':
        withdrawal()
    elif banking_choice == 'c':
        deposit()
    elif banking_choice == 'd':
        sys.exit()
    else:
        print "Invalid Choice. Please try again."
        existing_user_message()

print """
        Welcome to Internet Banking
            a. New User
            b. Existing User
"""

user_choice = raw_input("Please enter your choice:")
user_choice = user_choice.lower()

if user_choice == 'a':
    create_user()
elif user_choice == 'b':
    existing_user()
else:
    print "Invalid Choice. Please try again later. Good Bye."
    
    