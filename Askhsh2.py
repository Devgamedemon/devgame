# 1.φτιάξε μου ένα κενό αρχείο txt και αποθηκευσέτο
# 2. ανοιξε αυτο το αρχείο και γράψε ένα ποιήμα μέσα, αποθήκευσέτο
# 3.ανοιξε αυτό το αρχείο, εκτύπωσε τις λέξεις που έχει μέσα , in reverse



#creating a text file with the command function "x"

f = open("myfile.txt", "x")
f.close()
f = open("myfile.txt", "a")
f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
        " sed do eiusmod tempor incididunt ut labore et \n dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip \n ex ea commodo consequat."
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore \n eu fugiat nulla pariatur."
        " Excepteur sint occaecat cupidatat non proident, "
        "sunt in culpa qui officia \n deserunt mollit anim id est laborum.")
f.close()
f = open("myfile.txt", "r")
print(f.read())

f = open("myfile.txt", "r")
f2=(f.read())
f = open("myfile.txt", "w")
f.write(f2[::-1])
f = open("myfile.txt", "r")
print("\n" ,f.read())
f.close()


f = open("myfile.txt", "r")
f3=(f.read())
wordsf3 = f3.split(" ")
print(wordsf3)
n=0
wordsf4=[]
for i in wordsf3:
        wordsf4.append(i[::-1])
        n+=1
f4=' '.join(wordsf4)
print(wordsf4)
f = open("myfile.txt", "w")
f.write(f4)
f = open("myfile.txt", "r")
print("\n" ,f.read())
f.close()

#allos tropos pou anapodogirizei tis lexeis kai tis kanei opws htan sto arxiko lorem ipsum
y=len(wordsf4)-1   #gia na einai sto swsto range to y to -1
for x in range (len(wordsf4)):
        #print(wordsf4[y])
        y=y-1