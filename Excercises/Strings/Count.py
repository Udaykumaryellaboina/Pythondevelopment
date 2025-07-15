#Exercise 1: Return the count of a given substring from a string
""" Write a program to find how many times substring “radha” appears in the given string
 radha is most beutiful,radha is queen of vraj"""

sentence="radha is most beutiful,radha is queen of vraj,radha is most beloved to govind"
x=sentence.count("radha")
print(x)

#write progrme to count the number of vowels in the string

string="Milind Dattatray Mali"
vowel="AEIOUaeiou"
count=0
for i in string:
    if i in vowel:
        count+=1
print(count)

'''Count all letters, digits, and special symbols from a given string
 given-->str1 = "P@#yn26at^&i5ve"
 expected-->Total counts of chars, digits, and symbols'''

str1 = "P@#yn26at^&i5ve"
l1=list(str1)
char=0
digit=0
special_char=0
for i in l1:
    if i.isalpha()==True:
        char+=1
    elif i.isdigit()==True:
        digit+=1
    else:
        special_char+=1
print("char",char)
print("digit",digit)
print("special_char",special_char)