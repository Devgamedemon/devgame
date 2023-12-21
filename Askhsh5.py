#REGISTER Password system
# Write a program that checks the strength of a password entered by the user.
# Implement criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters,
# save the final password in a dictionary.
#
# The passWord must at least be, 8 characters in length, to have one at least a number and at two  characters ,
# at least one uppercase letter and one lowercase letter




password=[]

input1=str(input("\n Enter your strong-password: ") )
#password.append (input1)

print(input1)
cond=False
while  cond==False :
        cond1=False
        cond2=False
        cond3=False
        cond4=False
        input1 = str(input("\n your password must be at least 8 characters lond an uppercase and lowercase letter and a digit: "))
        if len(input1) >=8:
                print(len(input1))
                cond1=True
        for i in input1:
                if  i.isupper() :
                        cond2=True
        for i in input1:
                if i.islower():
                        cond3 = True
        for i in input1:
                if i.isdigit():
                        cond4 = True
        if cond1 and cond2 and cond3 and cond4 :
                cond=True




        print("Your password must be at least 7 characters long including A capital letter")
        print("What a secured password!")
        print("your password is strong")




#deyteros tropos
# password=[]
#
#
# while True:
#         password = input("Enter a password: ")
#         if len(password) > 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
#                 break
#         print("Your password must be at least 8 characters long including A capital letter and lowercase letter and number")
# print("What a secured password!")
#
