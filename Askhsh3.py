
canon=[]
print(" \n *****MAIN MENU*****")
print("\n 1. Load(Add a cannon ball on the top of the loader)")
print("\n 2. Fire(Fire the cannon ball by firing the ball from the top of the loader)")
print("\n 3. Check(Preview the next cannon ball without firing)")
print("\n 4. isEmpty(Check if the loader is empty to ensure the cannon is always ready to fire)")
print("\n 5. Firepower(Keep track of the number of cannon balls in the loader)")
#print("\n Enter your action: ")

do = {1: "Load" , 2:"Fire" , 3:"Check" ,4:"isEmpty" , 5 :"Firepower"}
#action = input("\n Enter your action: ")
cond=True
while cond == True:
    action = input("\n Enter your action: ")
    if action.isdigit():
        actionn=int(action)
        if actionn == 1 :
            canonball = input("\n Enter your ammo: ")
            canon.append(canonball)
        elif actionn == 2 :
            canon.pop(0)
        elif actionn == 3 :
            print(canon[0])
        elif actionn == 4 :
            if canon[0] == []:
                print("ready to fire Canon====:")
        elif actionn == 5 :
            print(len(actionn))
    else:
        print("Invalid input")
