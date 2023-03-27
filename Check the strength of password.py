#To check the strength of a password entered by the user as Strong, Medium or Weak:
while True:     #It reiterates the whole code until user decides to stop the code.
    pwd=input("Enter your password: ")

    #First we check if the basic requirements of a password are fulfilled:
    if len(pwd)<8:
        print("Your password is weak.")
    elif (len(pwd)>=16):
        print("Your password is very long.")
    elif (len(pwd)>=8) and (len(pwd)<16):
        if pwd.isalpha():
            print("Your password only contains alphabets. Please set a new password.")
        elif pwd.isdigit():
            print("Your password only contains digits. Please set a new password.")
        elif pwd.isalnum():
            print("Your password doesn't contain any special characters. Please set a new password.")
        else:
            up=0
            low=0
            sc=0
            digit=0
            space=0
            for ch in pwd:
                if ch.isupper():
                    up+=1
                elif ch.islower():
                    low+=1
                elif ch.isdigit():
                    digit+=1
                elif ch.isspace():
                    space+=1
                else:
                    sc+=1
            if up==0:
                print("Your password must contain atleast 1 Uppercase Alphabet. Please try again.")
            elif low==0:
                print("Your password must contain atleast 1 lowercase alphabet. Please try again.")
            elif digit==0:
                print("Your password must contain atleast 1 digit. Please try again.")
            else:
                print("Your password is strong!")
                print("Password Length:",len(pwd))
                print("Number of Uppercase Letters:",up)
                print("Number of Lowercase Letters:",low)
                print("Number of Digits:",digit)
                print("Number of Special Characters:",sc)
                print("Number of Spaces:",space)
    
    cont=input("Do you want to check for another password? [y/n]")
    while cont.lower() not in ("y","n"):
        print("Please enter the correct input.")
        cont=input("Do you want to check for another password? [y/n]")
    if cont.lower()=='n':
        break
