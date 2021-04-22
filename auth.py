#register
#username, email address and password is supplied
#generate user account

#login
# - account number and password

#bank operations

#we need an entry point to the system

#initialising the system

#a for loop requires that we know how many times the user
#keeps trying unlike a while loop that can keep running until
#they select what you want them to select

import random

database = {
    7054323973: ['Tobs','Odmon','tobs@gmail.com','password', 200]
}#dictionary

#balance = [234, 532, 422, 0]


#initialising the system

def init():

    #isValidOptionSelected = False
    print("Welcome to bankPHP")

    #while isValidOptionSelected == False:
    haveAccount = int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))

    if haveAccount == 1:
            #isValidOptionSelected = True
        login()
    elif haveAccount == 2:
            #isValidOptionSelected = True
        print(register())
    else:
        print("You have selected an invalid option")
        #so that if all the conditions above fail and it finally gets here,
        #it initialises the computation all over again
        init()

def login():
    print("*********Login***********")

    #isLoginSuccessful = False

    #while isLoginSuccessful == False:

    accountNumberFromUser = input("Whats is your account number?\n")

    is_valid_account_number = account_number_validation(accountNumberFromUser)

    if is_valid_account_number:
        
        password = input("What is your passsword? \n")
        
        for accountNumber, userDetails in database.items():
            if(accountNumber == int(accountNumberFromUser)):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
                    #isLoginSuccessful = True

        print('Invalid account or password')
        login()

    else:
        init()

    #bankOperation(userDetails)

def account_number_validation(accountNumber):
    # check if account number is not empty
    # check if account number is 10 digits
    # check if the account number is an integer

    if accountNumber:
        #you can't check the length of an integer so you need to convert to string to confirm the length
        if len(str(accountNumber)) == 10:

        #we are try to convert account number to an integer
            try:
                int(accountNumber)
                return True
        #capturing the different type of errors that may occur
            except ValueError:
                print("Invalid Account number, account number should be integer")
                return False
            
            except TypeError:
                print("Invalid account type")
                return False
        
        else:
            print("Account number cannot be more than or less than 10 digits")
            return False
    else:
        print("Account number is a required field")
        return False
def register():
    print("************** You need to register **************")
    email = input("what is your email address?\n")
    firstname = input("what is your first name?\n")
    lastname = input("what is your last name?\n")
    password = input("create a password for yourself\n")

    accountNumber = generateAccountNumber()

    try:
        accountNumber = generateAccountNumber()
    except ValueError:
        print("Account generation failed due to internet connection failure")
        init()

    database[accountNumber] = [firstname, lastname, email, password, 0]

    print("Your account has been created")
    print("== ==== ===== ==== ==== ==== ====")
    print("Your account number is %d" %accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ==== ==== ==== ==== ==== ==")
    #return database

    login()


    bankOperation()

def bankOperation(user):
    print("Welcome %s %s" %(user[0], user[1]))

    #isSelectedOptionValid = False
    #while isSelectedOptionValid == False:

    selectedOption = int(input("what will you like to do? (1) deposit (2) withdrawal (3) logout (4) exit"))

    if(selectedOption == 1):
        #isSelectedOptionValid == True
        depositOperation()
    elif(selectedOption == 2):
        # isSelectedOptionValid == True
        withdrawalOperation()
    elif(selectedOption == 3):
        #isSelectedOptionValid == True
        logout()
    elif (selectedOption == 4):
            #isSelectedOptionValid == True
        exit()
    else:
            
            print("Invalid option selected")
            bankOperation(user)


def withdrawalOperation():
    print("withdrawal")
    #get current balance
    #get amount to withdraw
    #check if current balance > withdraw balance
    #deduct withdrawn amount from current balance
    #display current balance

def depositOperation():
    print("deposit operations")
    #get current balance
    #get amount to deposit
    #add deposited amount to current balance
    #display current balance
    #Do you want to perform another operation?

def generateAccountNumber():
    print("generating account number")
    return random.randrange(1111111111,9999999999)
#find out out to generate random numbers and specify the
#starting and the ending in python

def setCurrentBalance(userDetails):
    userDetails[4] = balance

def getCurrentBalance(userDetails):
    return userDetails[4]

def logout():
    #call login
    login()


#### ACTUAL BANKING SYSTEM ####
#this function initializes our system
#print(generateAccountNumber())
init()