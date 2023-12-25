
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
        counter4 = False
        counter3 = False
        counter5 = False
        counter6 = False
        print(len(mailstring[1]))
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