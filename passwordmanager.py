master =input("What is your master password")

def view():
    pass

def add():
    name=input("Account Name: ")
    passwo=input("Password: ")

    with open("passwords.txt" , "a") as f:
        f.write(name + " " + passwo)
        #continue at 1:15:15

        

while True:

    mode=input("WOuld you like to add a new password or view existing ones  (Enter either view or add or q to quit)  ?")

    if  mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add( )
    else:
        print("invalid mode")