'''
DAY-4:
**List dataType:
------------------
>>List is a collection of different datatypes that are enclosed in [] separated by coma(,)...
>>List is mutable
      Mutable                 Immutable
   ------------              -----------
1.The datatype can be      1.Can't be modified.
modified.
 eg:                           eg:
   any_=[1,2,3,4]             so= 'python is a language
 print(any_)                  print(so.replace('python','java'))
any_.append(5)                  print(so)
 print(any_)'''

#code                          
all_type=[1,'python',[1,2]]
for j in all_type:
    print(j)

'''Methods:
-------------
1.append():
>>This is used to add new item into list, but it will add in the last index position.
..At a time it will take only one argument. means append(90,34).
>>complete word in the single index.
'''
#code
any_=[1,2,3,4]
print(any_)
any_.append(5)
print(any_)
any_.append('python')
print(any_)

'''
2.extend():
>>In this it will also  add a item in the last position, but it will give each value in the each index positions
>> complete word in single single index'''
#code
any_=[1,2,3,4]
any_.extend('python')
any_.append('python')#i used append here for the difference
print(any_)

'''
3.pop():
>>Used to delete the item from the list, but it will delete based on index position..
-->Syntax--> variable_name.pop(index position)'''
#code
any_=[1,2,45,78,90]
any_.pop(3)
print(any_)

'''
4.remove():
>>used to delete the item from list, but it will delete value from the list
-->Syntax--> variable_name.remove(value)
'''
#code
any_=[1,2,45,78,90]
any_.remove(45)
print(any_)


#5.index():
any_=[1,2,'python is a language',[45,78,"java is a language",[1,23],90],'Hello']
print(any_[3][2][10])

#6.Sort
any_=[12,45,56,95,16]
any_.sort()
print(any_)


'''
**TUPLE:
---------
--> tuple is a collection of different datatypes represent in () and separated by (,)
>>it is immutable'''

how=(1,2,3,4,"python",[4,5],(90,78))
print(how)

'''***Methods:
1.index()
2.count()'''







