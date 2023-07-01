master_password = input("What is the master password? ")

def view():
    with open("password.txt", "r") as f:      # in here f stand for of file
        for line in f.readlines():
            data =  line.rstrip()
            user , password = data.split("|")  # it means we want to return the data as a list from a string
            print("USER:" , user , "|" , "PASSWORD:" , password)

def add():
    account = input("Account name: ")
    password = input("Password: ")
    with open("password.txt", "a") as f:      # in here f stand for of file
        f.write(account + "|" + password + "\n")


while True:
    mode = input("Would you like to add a new password or view the existing one? (add , view, quit): ")

    if mode == "quit":
        break 

    if mode == "view":
        view() 

    elif mode == "add": 
        add() 

    else:
        print("Invalid")
        continue

