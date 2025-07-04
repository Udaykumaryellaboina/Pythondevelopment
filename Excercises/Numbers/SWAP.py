# Swap the number without using third varible

#Pythonic Way (Tuple Unpacking)
a=10
b=20
a,b=b,a

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
print(swap(10,20))

#Using Bitwise XOR (Best for Integers)
a = 10
b = 5

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a, "b =", b)

#Using Arithmetic  Operators(Multiplication and Division)
a = 10
b = 5

a = a * b  # a = 50
b = a / b  # b = 10
a = a / b  # a = 5

print("a =", int(a), "b =", int(b))

