 # Task 1 calculator
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
operator=input("enter operator(+,-,/,*):")
if operator==('+'):
     result=a+b
     print("result=",result)
elif operator==('-'):
     result=a-b     
     print("result=",result)
elif operator==('*'):
     result=a*b
     print("result=",result)     
elif operator==('/'):
     if b!=0:
         result=a/b 
         print("result=",result)
     else:
         print("error: division by zero")     
else :
     print("invalid operator") 