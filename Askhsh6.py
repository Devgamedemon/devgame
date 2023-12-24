
#import Askhsh5
import re



# email=[]
#
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# cond=False
# while  cond==False :
#         cond1=False
#
#         email = input("\n Enter a valid email adress: ")
#         #if email == "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b" :
#         if re.fullmatch(regex, email):
#                 print("Valid Email")
#                 cond=True
#         else:
#                 print("Invalid Email")



#deyteros tropos
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
        if counter2==1 and counter1==1 :
                print("valid")
                cond = True