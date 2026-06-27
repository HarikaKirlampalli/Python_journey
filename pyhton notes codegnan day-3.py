'''Data Types:
1. int:
a=51
b=84

2.float:
num_2=7.34
num=5.65
print(num//2)


***String:
    context in between '.. ','' .. ''
    String is a squence of char that are enclosed in single quotes, double quotes
    String is immutable...

***Concatination:
 it is used to add words.
 Here , the (+) operator acts as to concatinate more than 2 strings'''

a= "Hello"
b= "Harika"
print(a+b)

'''
***Indexing:
Indexing is like a array concept (0,1,2,3 ....)
This is used to acess the particular char in the string by pass index position value..
Index starts from 0.
We have negtive indexing to count position from last to first)
'''

a="Hello welcome to Python Programming"
print(a[9])
print(a[-3])

'''
***Methods:
1.replace():
>This method is used to change any sub string in that particular string
Syntax--variable_name.replace("old string","new string",count)
count means how many times it to replace..it is optional
'''
a="Hello welcome to Python Programming"
print(a.replace("o","O",2))

a="Hello welcome to Python Programming"
print(a.replace("Hello","Hai"))
print(a)

'''2.join():
> this methos is used to add new substring after every char in the string..
Syntax--"String".join(variable_name)'''


a="Hello welcome to Python Programming"
print("#".join(a))

'''
3.split():
>This method can divide the string into different index into list, based on the string pass by us..
Syntax--> (variable_name.split('Substring'))

'''
a = "Hello welcome to Python Programming"
print(a.split(" my "))


'''
4.count():
>Useed to count the substring(letters) in the particular string and also specify the index position..
Syntax--varaible_name.count("substring",start index, ending index)'''

a = "Hello welcome to Python Programming"
print(a.count("o",0,12))


'''String built-in functions:
1.len():
> This will find the length of the '''

a = "Hello welcome to Python Programming"
print(len(a))

'''
2.max()
>max char in the string'''

a = "Hello welcome to Python Programming"
print(max(a))


'''
3.min():
>min char in the string
>In the below prgrm the output is coming space bcoz space is also a character '''

a = "Hello welcome to Python Programming"
print(min(a))



