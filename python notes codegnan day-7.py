'''
DAY-7
***Input formatting from user
-------------------------------
1.input():
>>The input() function is used to take input from user
(i) int:
@code
num = int(input("Enter a number:"))
num_2= int(input("Enter a number:"))
print(num+num_2)

(ii)string:
@code
how = input("enter a char:")
print(how+'Haari')

(iii)float:
@code
num = float(input("Enter your account balance:"))
print(num,"is your account balance")

(iv)list:
@code
group_=list(map(int,input().split()))
print(group_)

(v)tuple:
@code
some = tuple(map(int,input().split()))
print(some)
2.
group_=tuple(input().split())
print(group_)

**evoulve(): in this we can use any data type without mensioning.
@code
num=eval(input("Enter:"))
print(type(num))

*f string:
@code
name_=input("Enter your name:")
age_=int(input("Enter your age:"))
print(f"{name_} your age is {age_}")#used f string instead of print(name_,"your age is",age_)
@eg2
accpin_=int(input("Enter your acc pin:"))
bal_=int(input("Enter balance:"))
print(f"{accpin_} pin account balance is {bal_}")

**modulus format(using %)
@code
name_=input("Enter your name:")
age_=int(input("Enter your age:"))
print("My name is %s and iam %d years old"%(name_, age_))#modulus formatting
'''



























