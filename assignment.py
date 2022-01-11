# 1 .Finding out the average of the three numbers

'''a = int(input("Enter the first number  \n "))
b = int(input("Enter the second number \n "))
c = int(input("Enter the third number \n "))


def average(a,b,c):
    return (a+b+c)/3

k = average(a,b,c)
print("The average of the three numbers you entered is:",k)'''




#2.Computing a person's income tax

# let the gross income be stored in i.
'''i = int(input("Enter your gross income(in dollars) \n "))

# Let the number of dependents be stored in  d.
d = int(input("Enter the number of dependents \n "))

# let the standard deduction amount(in dollars) be stored in j
j = 10000

# The deduction amount(in dollars) corresponding to the number of dependents be stored in k
k = 3000

# The tax rate be stored in Z
Z = 0.2   #  it is given 20%

# function having gross income and number of dependents as two arguments.
def tax(i,d):
    return (i - j - k*d)*0.2  # tax = (taxable income)*tax rate

s = tax(i,d)
print("The tax amount you need to pay is",s)'''




#3 .Storing various data of a student in a list

'''data = list()

Name = input("Enter your name \n")
index = int(input("Enter the index of this data in the list\n "))
data.insert(index,Name)

SID = int(input("Enter the SID \n"))
index = int(input("Enter the index of this data in the list\n "))
data.insert(index,SID)

Gender = input("Enter M for male, F for female and U for other\n")
index = int(input("Enter the index of this data in the list\n "))
data.insert(index,Gender)

Course = input("Enter the course in which you are enrolled \n")
index = int(input("Enter the index of this data in the list\n "))
data.insert(index,Course)

CGPA = float(input("Enter the CGPA you got \n"))
index = int(input("Enter the index of this data in the list\n "))
data.insert(index,CGPA)


print("The information is", data)'''



#4. Adding the marks of 5 students in a list in a sorted manner

'''marks = list()

m1 = int(input("Enter the marks of the first student\n"))
marks.insert(0,m1)

m2 = int(input("Enter the marks of the Second student\n"))
marks.insert(1,m2)

m3 = int(input("Enter the marks of the Third student\n"))
marks.insert(2,m3)

m4 = int(input("Enter the marks of the Fourth student\n"))
marks.insert(3,m4)

m5 = int(input("Enter the marks of the Fifth student\n"))
marks.insert(4,m5)

print(f"The marks list is {sorted(marks)}")'''


#5.a
"""colors = ["Red","Green","White","Black","Pink","Yellow"]
# in order to remove an element at a particular index,we will use function 'pop()'...
colors.pop(3)

print(colors)"""

#5.b
colors = ["Red","Green","White","Black","Pink","Yellow"]

'''colors.pop(3)
colors.insert(3,"Purple")
colors.pop(4)

print(colors)'''





