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