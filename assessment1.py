#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Functions#
#prime function
def isPrime(n):
    for d in range(2,n):
        if(n%d==0):
            break
    else:
        return True
    return False


# In[2]:


isPrime(17)


# In[4]:


#python list
ages = [19, 26, 23]
print(ages)

list1 = [1, "Hello", 3.4]
list2 = [1, "Hello", 3.4, "Hello", "world"]
list3 = []
print(list1)
print(list2)
print(list3)


# In[11]:


#python dictionary
student = {'name':'john','age':25, 'courses':['Math', 'compsci']}
print(student)
student.update({'name':'john','age':26, 'phone':9089453394})
print(student)

age = student.pop('age')
print(len(student))
print(student)
print(age)
print(student.keys())


# In[1]:


# python array
# append a new item at the end of the array
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Append 11 at the end of the array:")
array_num.append(11)
print("New array: "+str(array_num))


# In[ ]:




