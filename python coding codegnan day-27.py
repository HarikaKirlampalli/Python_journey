'''
REGULAR EXPRESSIONS(RegEx)
--------------------------
>>RegEx is an sequence of char that can searching pattern
>>To use RegEx we have import re module..
 SYNTAX :
 --------
 import re

FUNTIONALITIES
----------------
1)findall() :
@code
-------
import re
txt = 'Python is a language and also called dynamically typed'
print(re.findall('[an]',txt))

o/p : ['n', 'a', 'a', 'n', 'a', 'a', 'n', 'a', 'a', 'n', 'a', 'a']

2)search() :
>>this search() will find the char,but it will the first sequence that found in the string..
@code
------
import re
txt = 'Python is a language and also called dynamically typed'
print(re.search('[a]',txt))

o/p : <re.Match object; span=(10, 11), match='a'>

3)split() :
@code
-----
import re
txt = 'Python is a language and also called dynamically typed'
print(re.split(' ',txt))

o/p : ['Python', 'is', 'a', 'language', 'and', 'also', 'called', 'dynamically', 'typed']

4)sub() :
@code
-----
import re
txt = 'Python is a language and also called dynamically typed'
print(re.sub(' ','@',txt))

o/p : Python@is@a@language@and@also@called@dynamically@typed

5)fullmatch() :


**METACHAR**
------------
[] :
----
import re
txt = 'I have 5000 Rupees'
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))
print(re.findall('[0-9]',txt))

o/p :
['h', 'a', 'v', 'e', 'u', 'p', 'e', 'e', 's']
['I', 'R']
['5', '0', '0', '0']

^ :
---
import re
txt = 'I have 5000 Rupees'
print(re.findall('^I have',txt))
print(re.search('^I have',txt))

o/p:
['I have']
<re.Match object; span=(0, 6), match='I have'>

$ :
---
import re
some = 'I am going to college'
print(re.findall('college$',some))
print(re.search('college$',some))

o/p :
['college']
<re.Match object; span=(14, 21), match='college'>

. :
---
import re
any_ = 'Hello! This is Harika'
print(re.findall('Ha...a',any_))
print(re.search('T...',any_))

o/p :
['Harika']
<re.Match object; span=(7, 11), match='This'>

* :
----
import re
how = 'python is a programming language'
print(re.findall('p.*m',how))
print(re.findall('p.*',how))
print(re.search('p.*n',how))

o/p :
['python is a programm']
['python is a programming language']
<re.Match object; span=(0, 27), match='python is a programming lan'>

+ :
----
import re
how = 'python is a programming language'
print(re.findall('p.+thon',how))
print(re.search('p.+thon',how))

o/p:
['python']
<re.Match object; span=(0, 6), match='python'>

{} :
------
import re
how = 'python is a programming language'
print(re.findall('p.{3}',how))
print(re.search('p.{5}',how))

o/p:
['pyth', 'prog']
<re.Match object; span=(0, 6), match='python'>
'''
import re
how = 'python is a programming language'
print(re.findall('p.{3}',how))
print(re.search('p.{5}',how))


















