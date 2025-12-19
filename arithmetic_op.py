#arthmetic operstor in python
a=10
b=20
c=a+b
print(c)
c=a-b
print(c)
c=a*b
print(c)
c=a/b #gives floating point value
print(c)
c=a//b #gives integer value
print(c)
c=a%b #gives remainder
print(c)
c=a**b # is ae^b
print(c)

#augmented operator
x=1;
x=x+3
x+=3; #this augmented operator add x to 3 and store in x.
print(x)
#precedence of operator
#expoential , multiplication or division, addition or subtract
x= 10 + 2*5
print(x); #it first multiply and then add

# parenthesis will change the precedence. parenthesis will take the priority first
x=(10+3)*2
print(x);
x=(10+3)*2**2 #here parenthesis operation will first execute 10+3 =13 ,then expoential 2**2=4 then multiple 13*4= 52
print(x);

#methods to manipulate the numbers.
x=2.888
print(round(x))

print(abs(-4.5)) # this function gives a +ve number , though the number passed was -ve.


#predefined module:
#MODULE: Module in python is inbuild which has predefined methods.
import math
print(math.ceil(x));
print(math.floor(x));


