# Q.1
from tkinter import *
root = Tk()
root.title("GST Calculator")
root.geometry("600x300")

def calculate():
    m1 = int(Original_costentry.get())
    m2= int(Net_Priceentry.get())
    GST_Rate=((m2-m1)*100)/(m1+1)
    Label(text=f"{GST_Rate}",font="arial 15").place(x=250,y=200)

Original_cost = Label(root,text="Original Cost:",font="arial 15")
Net_Price = Label(root,text="Net Price:",font = "arial 15")
Original_cost.place(x=60,y=30)
Net_Price.place(x=60,y=80)

Rate = Label(root,text="Rate:",font="arial 15").place(x=50,y=230)

Original_costinput = IntVar()
Net_Priceinput = IntVar()

Original_costentry = Entry(root,textvariable =Original_costinput,font="arial 15",width=9)
Net_Priceentry = Entry(root,textvariable =Net_Priceinput,font="arial 15",width = 9)

Original_costentry.place(x=250,y=30)
Net_Priceentry.place(x=250,y=90)

Button(text="Calculate",command=calculate,font="arial 15").place(x=370,y=20)
Button(root,command=lambda:exit(),text="Exit",font="arial 15",width=9).place(x=370,y=80)
root.mainloop()


#Q.2
from tkinter import *
from calendar import calendar

root = Tk()
root.title("Calendar")
root.geometry("400x200")

def calender():
    year= int(enter_year.get())
    display_calender=Label(root,text=calendar(year)).place(x=20,y=200)



if __name__== '__main__':
    input_year = Label(root,text="Enter Year",font="arial 15").place(x=50,y=100)
    enter_year = Entry(root,textvariable=input_year,font="arial 15",width=20)
    enter_year.place(x=20,y=140)

    show_calendar= Button(root,text="Show Calendar",command=calender).place(x=50,y=170)
    root.mainloop()


# Q3.

from tkinter import *
root=Tk()
root.geometry("600x4500")
root.title("Calculator")
root.config(bg="black")

expression = ""

def display(item):
    global expression
    expression+=item
    screen.config(text=expression)

def empty():
    global expression
    expression = ""
    screen.config(text=expression)

def output():
    global expression
    result=""
    if expression!="":
        try:
            result=eval(expression)
        except:
            result="error"

    screen.config(text=result)


screen = Label(root,width=60,text="",font= "arial 15")
screen.pack(ipady=15,pady=8)

Button(root,text="C",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Blue",command=lambda:empty()).place(x=10,y=100)
Button(root,text="%",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("%")).place(x=150,y=100)
Button(root,text="/",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("/")).place(x=290,y=100)
Button(root,text="*",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("*")).place(x=450,y=100)

Button(root,text="7",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("7")).place(x=10,y=300)
Button(root,text="8",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("8")).place(x=150,y=300)
Button(root,text="9",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("9")).place(x=290,y=300)
Button(root,text="-",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("-")).place(x=450,y=300)

Button(root,text="4",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("4")).place(x=10,y=500)
Button(root,text="5",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("5")).place(x=150,y=500)
Button(root,text="6",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("6")).place(x=290,y=500)
Button(root,text="+",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("+")).place(x=450,y=500)

Button(root,text="1",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("1")).place(x=10,y=700)
Button(root,text="2",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("2")).place(x=150,y=700)
Button(root,text="3",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Black",command=lambda:display("3")).place(x=290,y=700)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),fg="White",bg="Red",command=lambda:output()).place(x=450,y=700)

root.mainloop()

# Q4.

list = []
no_of_students = int(input("Enter the number of students whose marks need to be stored: "))

for i in range(no_of_students):
        studenti = input("Enter the marks: ")
        list.append(studenti)

def pivot_place(list,first,last):
    pivot= list[first]
    left=first+1
    right=last
    while True:

        while left<=right and list[left]<=pivot:
            left=left+1
        while left<=right and list[right]>=pivot:
            right=right-1
        if right<left:
            break

        else:
            list[left],list[right] = list[right],list[left]

    list[first], list[right] = list[right], list[first]
    return right

def quick_sort(list,first,last):
    if first<last:
        p = pivot_place(list,first,last)
        quick_sort(list,first,p-1)
        quick_sort(list,p+1,last)

length = len(list)
quick_sort(list,0,length-1)
print(list)"""

# Q5.
#a.
"""list = []
no_of_students = int(input("Enter the number of students whose marks need to be stored: "))

for i in range(no_of_students):
        studenti = input("Enter the marks: ")
        list.append(studenti)

def pivot_place(list,first,last):
    pivot= list[first]
    left=first+1
    right=last
    while True:

        while left<=right and list[left]<=pivot:
            left=left+1
        while left<=right and list[right]>=pivot:
            right=right-1
        if right<left:
            break

        else:
            list[left],list[right] = list[right],list[left]

    list[first], list[right] = list[right], list[first]
    return right

def quick_sort(list,first,last):
    if first<last:
        p = pivot_place(list,first,last)
        quick_sort(list,first,p-1)
        quick_sort(list,p+1,last)

length = len(list)
quick_sort(list,0,length-1)
print(list)"""

#b.
"""
pos = 1

def binary_search(list,n):
    l = 0
    u = len(list)-1

    while l<=u:
        mid = (l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u= mid


list =sorted([45,80,47,69,13,14])
n=int(input("Enter the number you want to search\n"))
if  binary_search(list,n)== True:
    print("Found at",pos+1)
else:
    print("Not Found")
