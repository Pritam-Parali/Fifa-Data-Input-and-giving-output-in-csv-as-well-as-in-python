# FIFA 
import csv
import sys
def heading():
    f=open("fifa.csv","a",newline='')
    w=csv.writer(f)
    l=[" AGE","NAME","MATCHES PLAYED","TEAM NAME","HEIGHT","WEIGHT"]
    w.writerow(l)
    f.close()
def data():
    f=open("fifa.csv","a",newline='')
    w=csv.writer(f)
    n=int(input("enter the number of times ::"))
    for x in range(n):
        a=int(input("enter the age of the player   ::    "))
        n=input("enter the name  of the player    ::     ")
        b=int(input("enter the number of matches played   ::    "))
        c=str(input("enter the name of the team  ::     "))
        d=float(input("Enter the height of the player  ::   "))
        e=int(input("Enter the weight of the player  ::   "))
        l=[a,n,b,c,d,e]
        w.writerow(l)
    f.close()
def display():
    f=open("fifa.csv","r",newline='')
    age=csv.reader(f)
    for i in age:
        print(i)
    f.close()
#main programme
while True:
    print("                        FIFA                     ")
    print("MENU \n 1-FIELDNAMES \n 2-INPUT AND WRITE DATA \n 3-DISPLAY \n 4-EXIT")
    ch=int(input("enter your choice  :::   "))
    if ch==1:
        heading()
    if ch==2:
        data()
    if ch==3:
        display()
    if ch==4:
        print('THANK YOU')
        sys.exit()

