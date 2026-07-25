'''
Matplotlib
-----------
>>Matplotlib library is an python library that provides functionality to charts,
graphs, bar and data visualization.

Line plot
------------
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,23,15,30,5]
plt.plot(x,y)
plt.title('Simple Plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

@code2
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [109,124,158,98,75]
plt.plot(x,y)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')
plt.show()

Bar plot
-------------
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [109,124,158,98,75]

plt.bar(x,y,color='blue',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')
plt.show()

Pie chart
-----------  
import matplotlib.pyplot as plt
subjects_= ['python','java','.net','mern']
stu_ = [68,42,12,32]
plt.pie(stu_,labels=subjects_,colors =['grey','green','pink','orange'],autopct='%1.1f%%')
plt.legend(subjects_)
plt.title('courses')
plt.show()

Scatter plot
-------------

import matplotlib.pyplot as plt
x = ['TOYOTA','BMW','SWIFT']
y = [92,142,126]
plt.scatter(x,y,color='green')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')
plt.show()

Histogram
-----------
import matplotlib.pyplot as plt
y = [92,142,126]
plt.hist(y,bins=20)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')
plt.show()

'''
