#Python Assignment2---Prem Shankar  SID = 21104084

#1.A Finding the length of the string
str = "Python is a case sensitive language"
length = len(str)
print("The length of the string is:\n",length)


#1.B
orderreverse = str.replace(str,"language sensitive case a is Python")
print("The new string after changing the order is:\n",orderreverse)


#1.C creating a new string by using a substring of a given string using slicing
slicedsubstring  = str[10:26]
newstring = slicedsubstring
print("The new string using a substring of the original string is:\n",newstring)


#1.D replacing a substring of a string with another substring.
replacing = str.replace("a case sensitive","object oriented")
print("The new string after replacing a substring of the original string is:\n",replacing)


#1.E knowing the index of a substring in a string
k = str.index("a")
print("The index of a is:\n",k)


#1.F Removing the whitespaces present in a string ..
nowhitespace = str.replace(" ","")
print("After removing the whitespaces the string become:\n",nowhitespace)


#2
name = "Prem"
SID = "21104084"
Department = "EE"
CGPA = "9.9"

print(f"Hey {name} here!\nMy SID is {SID}\nI am from {Department} department and my CGPA is {CGPA}")


#3
a = 56
b = 10

#3.a. Using Logical AND
print(a&b)

#3.b.Using Logical OR
print(a|b)

#3.c. Using XOR
print(a^b) # XOR gives 1 as output only when one input is 0 and the other input is 1..

#3.d. using left shift
print(a<<2)
print(b<<2)

#3.e. using right shift
print(a>>2)
print(b>>4)


#4. Finding the maximum number among three numbers available from the user..

n1 = int(input("Enter the first number\n"))
n2 = int(input("Enter the second number\n"))
n3 = int(input("Enter the third number\n"))

if( n1 > n2 and n1> n3) :
    print("The greatest number is:")
    print(n1)
elif (n2 >n1 and n2 > n3):
    print("The greatest number is :")
    print(n2)
else:
    print("The greatest number is :")
    print(n3)




#5.checking availability of 'name' in a given string input by an user..

inputstr = input("Write any word/sentence you wish\n")

if "name" in inputstr:
    print("Yes")
else:
    print("No")




#6.Checking whether a triangle can be formed with the given side lengths from the user or not..

length1 = float(input("Enter the length of first side of your required triangle\n"))
length2 = float(input("Enter the length of second side of your required triangle\n"))
length3 = float(input("Enter the length of third side of your required triangle\n"))

# converting the input side lengths to integral values(if required)..
l= int(length1)
m=int(length2)
n=int(length3)

if(l+m>n and m+n>l and l+n>m):
    #Sum of any two sides of a triangle is always greater than the third side.
    print("Yes, you can form a triangle with these side lengths")
else:
    print("No, you cannot form a triangle with these side lengths")












