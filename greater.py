#python program to find greater number for 3 number
x=input("enter the value of x")
y=input("enter the value of y")
z=input("enter the value of z")
print("the greater number is")
    
if x>y and x>z:
    print("x is greater")
elif y>x and y>z:
    print("y is greater")
else:
    print("z is greater")

#to check for equality
eq=input("do you wanna check for equlity y or n").lower()
if eq=='yes':
    if x==y:
        print("x and y are equal")
    elif x==z:
        print("x and z are equal")
    elif y==z:
        print("y and z are equal")
    else:
        print("all are equal")
    

