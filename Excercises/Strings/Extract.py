#Extract all the emailid for the given string
string="Hi my name is Govind Das and my mail id is milindmali108@gmail.com"
new=list(string.split())
for i in new:
    if ".com" in i:
        print(i)


''' Calculate the sum and average of the digits present in a string
 Given a string s1, write a program to return the sum and average of the digits that appear in the string,
 ignoring all other characters.'''

str1 = "PYnative29@#8496"
str2=list(str1)
total=0
counter=0
for i in str2:
    if i.isdigit()==True:
        total=total+int(i)
        counter+=1
print("sum of digits in the given string is ",total)
print("avg of digits in the given string is ",round(total/counter,2))

'''Find words with both alphabets and numbers
 Write a program to find words with both alphabets and numbers from an input string.'''

#isalnum()
str1 = "Emma253 is Data scientist50000 and AI Expert"
str2=str1.split()
new=[]
for i in str2:
    for j in i:
        if j.isdigit()==True:
            if i not in new:
                new.append(i)
print(new[:])