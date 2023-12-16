#sets tuples lists dictionaries


x = ["apple", "banana", "cherry"]	            # list
x = ("apple", "banana", "cherry")              	# tuple

x = {"name" : "John", "age" : 36}	            # dict
x = {"apple", "banana", "cherry"}	            # set


x="rizos"
y=4+7
try:
    z=x+y
    print(z)
except:
    print("Error")

#ti diafora exei to ena me to allo ,na prosthesw kai na afairesw ena stoixeio apo to kathena
#na ta kanw iterate , na allaxw ena stoixeio pou exei mesa to kathena

x = ["apple", "banana", "cherry"]
x.append("pear")
print(x)
x.remove("pear")
print(x)

# Python code to iterate over a list
# Using for loop
for i in x:
    print(i)

#alaxw ena stoixeio sth lista pou den xerw thn thesh
x[1]="pear"
print(x)

counter=0
for i in x:

    if i == "pear":
        x[counter]="banana"
    counter += 1
print(x)