users = {}
status = ""

def displayMenu():
    status = input("Are you a registered user? y/n? Press q to quite. : ")
    
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
        
def newUser():
    createLogin = input("Create Login Name: ")
    
    if createLogin in users:
        print("\nLogin name already exist.\n")
    else:
        createPassw = input("Create Password : ")
        users[createLogin]=createPassw
        print("\nUser created.\n")
        
def oldUser():
    login = input("Enter Login Name : ")
    passw = input("Enter password : ")
    if login in users and users[login] == passw:
        print("\nLogin successfull\n")
    else:
        print("\nUsers doesn't exist or wrong password.\n")

while status != "q":
    displayMenu()