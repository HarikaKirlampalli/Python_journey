'''
DAY-16
    GENERATORS:
    -----------
>>This generator is special function that returns the iterator. instead of returning all the values at once...
>>Here we are going to use yield keyword

def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))

**Working of Generator
-----------------------
>>When a function is called
>>It does not execute the function immediately.
>>It will returns the generator object
>>Then the function will pauses at each yield.
>>when the next() is called again, execution resumes froom where it stopped.

@code
def demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3
how = demo()
print(next(how))
print(next(how))

with Generator
---------------
@code
def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

Without Generator
-----------------
@code
def sqt(n):
    for j in range(n):
        print(j*j)
sqt(5)

Q)Difference b/w function and generator.

    FUNCTION                      GENERATOR
   -----------                   ------------
1.return                      1.Yeild
2.Return complete result      2.return one value at once
3.Function will end after     3.pauses after every yield.
   the return value.
4.More memory used            4.Less Memory used
5.This function never resume  5.Resumes after next()


Yield Keyword
--------------
>>This will produce the value
>>But the yield pauses the function
>>And yield will save the functions current state
>>Yield will continue where it stopped.

next() keyword
--------------
>>The next() function is used to retrieve the next value from a generator.

StopIteration
--------------
>> Calling next() function after all values retrieve then it will raise stopIteration Exception.

def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


def how(so):
    for i in range(so):
        yield i*2+2
any_ = how(10)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


Generator expression
---------------------
>>The generator expression is similar to a list compherehension bot uses parenthesis() instead of [].
'''
gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))








































