#python program to swap two variables
a=3
b=5
print("the values before swapping")
print("a=",a)
print("b=",b)
#lets swap a and b
#using temp variable
temp=a
a=b
b=temp
print("the values after swapping")
print("a=",a)
print("b=",b)



#python program to find greater number for 3 number
x=input("enter the value of x")
y=input("enter the value of y")
z=input("enter the value of z")
print("the greater number is")
    
if x>y:
    if x>z:
        print(x)
    else:
        print(z)
else:
    if y>z:
        print(y)
    else:
        print(z)
