#Replace each special symbol with # in the following string


str1 = '/*Jon is @developer & musician!!'
import string
for i in string.punctuation:
    if i in str1:
        str1=str1.replace(i,"#")
print(str1)

'''Write a python program to convert a string to title case without using the title()'''

a=input("enter the title: ")
b=a.split()
r=''
 #print(b)
for i in b:
    r=r+i.capitalize()+" "
print(r)

'''Remove empty strings from a list of strings'''

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for i in str_list:
    if i == "" or i==None:
        str_list.remove(i)
print(str_list)

''' Remove special symbols / punctuation from a string
 expected-->"Jon is developer musician"'''

sentence = "/*Jon is @developer & musician"
import re
clean_sentence=re.sub('[^A-Za-z0-9\s]+',"",sentence)
print(clean_sentence)


'''Removal all characters from a string except integers
 str1 = 'I am 25 years and 10 months old'
 expected-->2510'''

str1 = 'I am 26 years and 10 months old'
str2=str1.split()
new=[]
for i in str2:
    if i.isdigit()==True:
        new.append(i)
print("".join(new))