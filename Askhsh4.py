

def my_sum(numbers):
    apotelesma = sum(numbers)
    return apotelesma

def my_ave(numbers,apotelesma):
    aver =  apotelesma/len(numbers)
    return aver

def my_min(numbers):
    minim = min(numbers)
    return minim

def my_max(numbers):
    maxim = max(numbers)
    return maxim



numbers=[]

while len(numbers) < 5 :
    try:
        input1=int(input("\n Enter your number: ") )
        numbers.append (input1)
    except:
        print("input a digit you bastard")

#numbers=int(numbers)
sum=my_sum(numbers)
average=my_ave(numbers,sum)
minimum=my_min(numbers)
maximum=my_max(numbers)
print("The sum is: ",sum)
print("The average is: ",average)
print("The minimum is: ",minimum)
print("The maximum is: ",maximum)