# On start
print("Welcome to prudent Health Care")

import time

users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
    }
}


# approving form
def validate(form):
    if len(form) > 0:
        return False
    return True


# login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False


# login
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        return userscreen(username)
    else:
        print("Invalid username or password")


# registration
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("---------------------------------")
    print("Account Created Succesfully")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    time.sleep(1)
    print("Account has been created")
    print("---------------------------------")


# User screen
def userscreen(username):
    print("1. Book an appointment")
    print("2. View appointment status")
    choice_str = input("Input your choice\n")
    number = int(choice_str)
    if number == 1:
        appointment()
    elif number == 2:
        appoinment_status()
    else:
        appointment()


def appointment():
    print("Book an appointment")
    print("List of specialists")
    print("1. Doctor A")
    print("2. Doctor B")
    print("3. Doctor C")
    print("4. Doctor D")

    # This is for Doctor A
    select_doctor = input("Choose your doctor\n")

    if select_doctor == "1":

        print("Doctor A \n a. 08:00AM-09:00AM \n b.12:00AM-01:00PM \n c. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 08:00AM-09:00AM")
        elif your_time == "b":
            print("b. 12:00AM-01:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")

        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done. Go for payment ")
        else:
            print("waiting list")
            # This is for Doctor B

    elif select_doctor == "2":

        print("Doctor B \n a. 09:30AM-10:30AM\n b. 01:30PM-02:30PM \n c. 03:30PM-04:30PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 09:30AM-10:30AM")
        elif your_time == "b":
            print("b. 01:30PM-02:30PM")
        elif your_time == "c":
            print("c. 03:30PM-04:30PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done. Go for payment")
        else:
            print("waiting list")

            # This is for Doctor C

    elif select_doctor == "3":

        print("Doctor C \n a. 11:00AM-12:00AM \n b. 01:00PM-02:00PM \nc. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 11:00AM-12:00AM")
        elif your_time == "b":
            print("b. 01:00PM-02:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done. Go for payment")
        else:
            print("waiting list")

            # This is for Doctor D

    elif select_doctor == "4":

        print("Doctor D \n a. 07:30AM-08:30AM \n b. 10:30AM-11:30AM \n c. 04:30PM-05:30PM")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 07:30AM-08:30AM")
        elif your_time == "b":
            print("b. 10:30AM-11:30AM")
        elif your_time == "c":
            print("c. 04:30PM-05:30PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up Press y")
        if notification == "y":
            print("y. Check up done. Go por payment")
        else:
            print("waiting list")

            # This is for payment process
    print("For cash Enter C")
    print("For credit Enter L")
    payment = input("finish the payment")
    if payment == "C":
        print("payment done by cash")
        recebill = input("Please enter the receipt for the bill:-")
        print(recebill)
        print("Thank you")

    elif payment == "L":
        print("payment done by credit")
        crebill = input("Please enter the credit card number")
        print(crebill)
        print("Thank you")
    else:
        print("not paid and go for payment")
        print("Thank You")


# ---When you open the program....
print("---------------------------------------")
print("Options: register | login | payment | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "payment":
         payment()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")
print("-----------------------------------------po")
# On exit
print("Shutting down...")
time.sleep(1)