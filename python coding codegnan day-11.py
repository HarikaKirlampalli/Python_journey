'''

***DAY-11 (coding practice):

 #palindrome or not
txt=input()
empty_=""
for i in txt:
    empty_=i+empty_
if empty_==txt:
    print(f"{txt} is a palindrome")
else:
    print(f"{txt} not a palindrome")

#same with inbuilt function
txt=input()
empty_=""
for i in txt:
    empty_=txt[::-1]
if empty_==txt:
    print(f"{txt} is a palindrome")
else:
    print(f"{txt} not a palindrome") 

#fabinocci series
num1=0
num2=1
limit_=int(input("Enter a num:"))
print(num1,num2,end=" ")
for i in range(1,limit_+1):
    all_=num1+num2
    num1=num2
    num2=all_
    print(all_,end=" ")

    
#calculator
val1=int(input())
val2=int(input())
user_in=int(input("enter \n1.add \n2.subtraction \n3.multiplication \n4.division \n5.mod \n6.power \n7.floor div:"))
if user_in==1:
    print(val1+val2)
elif user_in==2:
    print(val1-val2)
elif user_in==3:
    print(val1*val2)
elif user_in==4:
    print(val1/val2)
elif user_in==5:
    print(val1%val2)
elif user_in==6:
    print(val1**val2)
else:
    print(val1//val2)

#printing table
n=int(input("enter a num:"))
for i in range(1,11):
    res=n*i
    print(f"{n} x {i} = {res}")
    

#perfect number
num=int(input("Enter a num:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not a perfect number")'''





