"""Exercise 2: Print characters from a string that are present at an even index number
 Write a program to accept a string from the user and display characters that are present at an even index
 number.
 For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’"""

string=input("enter the text: ")
x=list(string)
print(string)
for i in x[0::2]:
 print(i,end=" ")


"""Exercise 3: Write a program to remove characters from a string starting from zero up to n and return
 a new string.
 For example:
 remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a
 string. remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters
 from a string. Note: n must be less than the length of the string."""

def remove (word,n):
    x=len(word)
    p=list(word)
    for i in p:
        if n<=x:
            z=word[n:]
    print(z)

remove("pynative",2)