
def my_mail():
    email=[]
    cond=False
    while cond==False :
            cond1=False
            email = input("\n Enter a valid email adress: ")
            mailstring = email.split('@')
            print(mailstring)
            counter1=email.count("@")
            print(counter1)
            if len(mailstring)==2 :
                    counter2 = mailstring[1].count(".")
            else:
                    print("invalid email")
                    continue
            counter4 = False
            counter3 = False
            counter5 = False
            counter6 = False
            if len(mailstring[0]) < 64 and len(mailstring[1]) <= 9 :
                    counter3 = True
            if any(c.isupper() for c in mailstring[0]) or any(c.islower() for c in mailstring[0]):
                    counter4 = True
            if any(c.isupper() for c in mailstring[1]) or any(c.islower() for c in mailstring[1]):
                    counter5 = True
            mailstring2 = mailstring[1].split('.')
            if any(c.isupper() for c in mailstring2[0]) or any(c.islower() for c in mailstring2[0]):
                    counter6 = True
            if counter2==1 and counter1==1 and (counter3==True) and (counter4==True) and (counter5==True) and (counter6==True):
                    print("valid")
                    cond = True
                    validmail=True

    return email , validmail



def my_password():
    password = []

    cond = False
    while cond == False:
        cond1 = False
        cond2 = False
        cond3 = False
        cond4 = False
        input1 = input("\n your password must be at least 8 characters long and uppercase and lowercase letter and a digit: ")
        if len(input1) >= 8:
            print(len(input1))
            cond1 = True
        for i in input1:
            if i.isupper():
                cond2 = True
        for i in input1:
            if i.islower():
                cond3 = True
        for i in input1:
            if i.isdigit():
                cond4 = True
        if cond1 and cond2 and cond3 and cond4:
            cond = True
            validpass=True
            password=input1
        else:
            if cond1 == False:
                print("The password must be at least 8 chars")
            if cond2 == False:
                print("The password must have at least a uppercase letter!")
            if cond3 == False:
                print("The password must have at least a lowercase letter!")
            if cond4 == False:
                print("The password must have at least one digit!")

    return password , validpass




pass1= my_password()
mail1= my_mail()
print(type(pass1))
print(type(mail1))
print(pass1[0])
print(mail1[0])
print("oeo")
f = open("myfile.txt", "x")
f.close()
f = open("myfile.txt", "a")
passlast=(pass1[0]+"\n" )
maillast=(mail1[0]+"\n" )
f.write(passlast)
f.write(maillast)
f.close()
f = open("myfile.txt", "r")
print(f.read())