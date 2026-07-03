'''
  DAY-10
 --------
1.
num = int(input("Enter a number:"))
count = 0
for j in range(1,num+1):
    if num % j == 0:
         count += 1
if count == 2:
    print(f"{num} is a prime")#prime number code
else:
    print(f"{num} is not a prime")
    
2.prime number counting
limit_=10
for j in range(2,limit_+1):
    count = 0
    for i in range(1,j+1):
        if j % i == 0:
            count += 1
            print(count)
    if count == 2:
      print(f"{j} is a prime")
3.
num = 5
for j in range(1,num+1):#code to print right angle triangle
    for i in range (1,j+1):
        print("*", end = " ")#end (" ") is used to print *'s side by side
    print()
4.
num = 5
for j in range(1,num+1): 
    for i in range (1,j+1):
        print(i, end = " ")
    print()
5.
num = 4
count = 0
for j in range(1,num+1): 
    for i in range (1,j+1):
        count += 1
        print(count, end = " ")
    print()
6.
num = 4
count = 0
for j in range(num, 0, -1): 
    for i in range (1,j+1):
        count += 1
        print(count, end = " ")
    print()
7.
am_str = int(input("Enter a value:"))#armstrong code
length_ = len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) ** length_
if all_sum == am_str:
        print(f"{am_str} is armstrong")
else:
         print(f"{am_str} is not armstrong")
8.
num = 6
for j in range(num):#pyramid code
    print(" " *(num - j -1),end = " ")
    print("*" *(2 * j + 1))
'''















