#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 1:
def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('python.txt')


# In[9]:


#question 2 :
n = int(input("\n\t\tEnter Lines To Read : "))
f = open("python.txt" , "r")
for i in range(n):
	print(f.readline())


# In[8]:


#question 3 :
n = int(input("type how many last lines you want to see :"))
f = open("python.txt")
lines = f.readlines()
last_lines = lines[-n:]

print(last_lines)


# In[13]:


#question 4 :
f = open('python.txt','r+')
lines=f.read()
words=lines.split()
print("the text contains ",len(words) ,"words")


# In[ ]:




