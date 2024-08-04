def add(a,b):
    x=a+b
    return x
def sub(a,b):
    x=a-b
    return x
def mul(a,b):
    x=a*b
    return x
def div(a,b):
    if b==0:
        return "Not Possible"
    else:
        x=a/b
    return x
def rem(a,b):
    x=a%b 
    return x
def pow(a,b):
    x=a**b
    return x
def sr(a):
    x=a**(0.5)
    return x
def operations():
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Remainder\n6.Power\n7.Square root")
    print("Enter your choice: ")
    q=int(input())
    if q not in range(1,8):
        print("Invalid input,please enter a number between 1 to 7.")
    else:
        if q==7:
            s=eval(input("Enter the number: "))
        else:
            s=eval(input("Enter 1st number: "))
            n=eval(input("Enter 2nd number: "))
        if q==1:
            print("Addition of "+str(s)+" and "+str(n)+" is "+str(add(s,n)))
        elif q==2:
            print("Substraction of "+str(s)+" and "+str(n)+" is "+str(sub(s,n)))
        elif q==3:
            print("Multiplication of "+str(s)+" and "+str(n)+" is "+str(mul(s,n)))
        elif q==4:
            print("Division of "+str(s)+" and "+str(n)+" is "+str(div(s,n)))
        elif q==5:
            print("Remainder, if "+str(s)+" is divided by "+str(n)+" is "+str(rem(s,n)))
        elif q==6:
            print(str(s)+" to the power of "+str(n)+" is "+str(pow(s,n)))
        elif q==7:
            print("Square root of "+str(s)+" is "+str(sr(s)))
        
def main():
    y=True
    while y:
        operations()
        print("Enter \'y\' if you want to continue else \'n\'")
        c=input()
        if c.lower()=='y':
            y=True
        else:
            y=False
main()
