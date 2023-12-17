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

#----------------------------------------------------------

#tuples are a type of data structure that is very similar to lists.
#The main difference between the two is that tuples are immutable,
#A tuple is a collection which is ordered and unchangeable.Allows duplicate members.
#meaning they cannot be changed once they are created.
#meaning that we cannot change, add or remove items after the tuple has been created
#There are two main types of tuples: named tuples and unnamed tuples

print("--------------------tuples")
x = ("apple", "banana", "cherry")            	# tuple
print(type(x))
print("length of x=", len(x))
#to i pairnei thn timh tou aple , banana , cherry
for i in x:
    print(i)

#allos tropos me to y na einai to index to tuple dhladh 0 ,1 ,2
y=0
for y in range(len(x)):
    print(x[y])

print("--------------------dictionaries")
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered, changeable and do not allow duplicates.
#Dictionaries cannot have two items with the same key,
#It is separated by a colon(:), and the key/value pair is separated by comma(,)
#Dictionaries are written with curly brackets, and have keys and values
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#If there is a duplicate key defined in a dictionary,The preference will be given to the last one defined
#The data-type for your key can be a number, string, float, boolean, tuples, built-in objects like class and functions
#Only thing that is not allowed is, you cannot defined a key in square brackets

x = {"name" : "John", "age" : 36}	            # dictionary
print(x)
print(type(x))
x["name"] = "Jim"    #allazw stoixeia sto dictionary
x["age"]=32          #allazw stoixeia sto dictionary
x["model"]="mustang"
print(x)
x.update({'age': 33})    #allazw kai etsi stoixeia sto dictionary

x.pop("model")   #afairw stoixeia apo to dictionary
print(x)
del x["age"]    #afairw kai etsi stoixeia apo to dictionary
print(x)

x["age"]=32
x["model"]="mustang"
print(x.keys())

#mou ektypwnei ta keys kai oxi ta values etsi
for i in x:
    print(i)
#mou ektypwnei ta values kai oxi ta keys etsi
for i in x.values():
    print(i)
#Loop through both keys and values, by using the items() method
for i, y in x.items():
  print(i, y)

print("--------------------sets")

#Sets are used to store multiple items in a single variable
#A set is a collection which is unordered, unchangeable*, and unindexed.
#you cannot change its items,but you can remove items and add new items
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Sets cannot have two items with the same value
#The values True and 1 are considered the same value in sets, and are treated as duplicates
#The values False and 0 are considered the same value in sets, and are treated as duplicates
#A set can contain different data types

x = {"apple", "banana", "cherry"}	            # set

print(x)
print("length of x=", len(x))
print(type(x))

x.remove("banana")   #afairw sygekrimena stoixeia apo to set
print(x)

x.add("banana")        #prosthetw sygekrimena stoixeia apo to set
x.add("pear")
print(x)

for i in x:
    print(i)

