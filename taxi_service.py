import random
import math
import os
import pickle
import datetime as dt
sp,dp,carno,='','',''
dist=0.0
def mumbai():
    global sp
    global dp
    global carno
    global dist
    m1=['AH Ansari Chowk', 'Andheri(W)', 'Andheri(E)', 'Bandra', 'Bharat Nagar', 'Dadar', 'Juhu', 'Marol Maroshi', 'Mittal Estate', 'Model Town', 'Santacruz(E)', 'Santacruz(W)', 'Vesave Yari']
    print("LIST OF AVAILABLE STOPS IN MUMBAI")
    for i in range(len(m1)):
        print("-"*45,"\n","[",i,"]"," : ","\t",m1[i])
    m2=1;m3=["1","2","3","4","5","6","7","8","9","10","11","12"]
    while m2:
        print('---------------------------------------------------------------------------------------')
        m4=input("ENTER START:")
        if m4 in m3:
            print("Accepted!");m2=0
        else:
            print("Try Again Using Valid Input Within The Range")
    m5=1;m6=["1","2","3","4","5","6","7","8","9","10","11","12"]
    while m5:
        m7=input("ENTER DESTINATION:")
        if m7==m4:
            print("Start And Stop Can't Be Same");m5=1
        elif m7 in m6:
            print("Accepted!");m5=0
            print('---------------------------------------------------------------------------------------')
        else:
            print("Try Again Using Valid Input Within The Range")
    print("Start Is From:",m1[int(m4)]);sp=m1[int(m4)]
    print("End Is At:",m1[int(m7)]);dp=m1[int(m7)]
    dist=round(abs(((int(m4))-(int(m7)))*9.4),2)
    print('Distance: ',dist,'km')
    
    mn=['MH-02 5567','MH-03 6788','MH-04 0900','MH-05 8611','MH-02 6157']
    carno=random.choice(mn)

def delhi():
    global sp
    global dp
    global carno
    global dist
    d=['KRITI NAGAR','RAJIV CHAUK','DWARKA SECTOR-1','CHANDNI CHOWK','KASHMERE GATE','NEW DELHI','LAJPAT NAGAR','SHASTRI PARK','DELHI JUNCTION RAILWAY STATION','BOTANICAL GARDEN','IGI AIRPORT','OLD DELHI']
    print("LIST OF AVAILABLE STOPS IN DELHI")
    for i in range(len(d)):
        print("-"*45,"\n","[",i,"]"," : ","\t",d[i])
    flag=True
    while flag:
        print('---------------------------------------------------------------------------------------')
        start=input("ENTER START: ")
        if start.isdigit()==True and int(start)<=len(d)-1 and int(start)>=0:
            flag=False
        else:
            print("Please enter a valid input!! ")
    flag1=True
    while flag1:
        stop=input("ENTER DESTINATION: ")
        if stop.isdigit()==True and int(stop)<=len(d)-1 and int(stop)>=0 and start!=stop:
            flag1=False
        else:
            print("Please enter a valid input: ")
    print('---------------------------------------------------------------------------------------')
    print('YOUR STARTING POINT: ',d[int(start)-1],'\nYOUR STOP: ',d[int(stop)-1]);sp=d[int(start)-1];dp=d[int(stop)-1]
    dist=round(abs((int(start)-int(stop))*12.4),2)
    print('Distance: ',dist,'km')
    dn=['DL-01 2145','DL-02 8089','DL-03 6177','DL-04 0001','DL-05 6996']
    carno=random.choice(dn)

def kolkata():
    global sp
    global dp
    global dist
    global carno
    k=["Kavi Shubhash","Shahid Khudiram","Gitanjali","Rabindra Sarobar","Kalighat","Jatin Das Park","Esplanade","Dakhineshwar","Park street"]
    print("LIST OF AVAILABLE STOPS IN KOLKATA")
    for i in range(len(k)):
        print("-"*45,"\n","[",i,"]"," : ","\t",k[i])
    flag=True
    while flag:
        print('---------------------------------------------------------------------------------------')
        start=input("ENTER START: ")
        if start.isdigit()==True and int(start)<=len(k)-1 and int(start)>=0:
            flag=False
        else:
            print("Please enter a valid input!! ")
    flag1=True
    while flag1:
        stop=input("ENTER DESTINATION: ")
        if stop.isdigit()==True and int(stop)<=len(k)-1 and int(stop)>=0 and start!=stop:
            flag1=False
        else:
            print("Please enter a valid input: ")
    print('---------------------------------------------------------------------------------------')
    print('YOUR STARTING POINT: ',k[int(start)-1],'\nYOUR STOP: ',k[int(stop)-1]);sp=k[int(start)-1];dp=k[int(stop)-1]
    dist=round(abs((int(start)-int(stop))*9.5),2)
    print('Distance: ',dist,'km')
    kn=['WB-06 F5977','WB-06 J9203','WB-08 C8566','WB-07 J7789']
    carno=random.choice(kn)
    

def chennai():
    global sp
    global dp
    global dist
    global carno
    c1=["Anna Square","Railway station","Doveton","Kannaigapuram","Mandaveli","CIT Nagar","Sholinganalur","Parry's Corner","Mehta Nagar","Choolai"]
    print("LIST OF AVAILABLE STOPS IN CHENNAI")
    for i in range(len(c1)):
        print("-"*45,"\n","[",i,"]"," : ","\t",c1[i])
    c2=1;c3=["0","1","2","3","4","5","6","7","8","9"]
    while c2:
        print('---------------------------------------------------------------------------------------')
        c4=input("Enter Start:")
        if c4 in c3:
            print("Accepted!");c2=0
        else:
            print("Try Again Using Valid Input Within The Range")
    c5=1;c6=["0","1","2","3","4","5","6","7","8","9"]
    while c5:
        c7=input("Enter Destination:")
        if c7==c4:
            print("Start And Stop Can't Be Same");c5=1
        elif c7 in c6:
            print("Accepted!");c5=0
            print('---------------------------------------------------------------------------------------')
        else:
            print("Try Again Using Valid Input Within The Range")
    print("Start Is From:",c1[int(c4)]);sp=c1[int(c4)]
    print("End Is At:",c1[int(c7)]);dp=c1[int(c7)]
    dist=round(abs(((int(c4))-(int(c7)))*7.2),2)
    print('Distance: ',dist,'km')
    cn=['TN-01 AR 5008','TN-01 BC 7898','TN-01 MR 2997','TN-01 AF 2664','TN-01 DA 4558']
    carno=random.choice(cn)


def city():
    print("1.MUMBAI")
    print("2.DELHI")
    print("3.CHENNAI")
    print("4.KOLKATA")
def choice(choice):
    
    global w
    if choice=='1':
        w=0
        print("Your City: MUMBAI")
        print('---------------------------------------------------------------------------------------')
        mumbai()
    elif choice=='2':
        w=0
        print("Your City: DELHI")
        print('---------------------------------------------------------------------------------------')
        delhi()
    elif choice=='3':
        w=0
        print("Your City: CHENNAI")
        print('---------------------------------------------------------------------------------------')
        chennai()
    elif choice=='4':
        w=0
        print("Your City: KOLKATA")
        print('---------------------------------------------------------------------------------------')
        kolkata()
    else:
        print("*************************************WRONG CHOICE**************************************")
        print("*****************************PLEASE ENTER A VALID INPUT!!******************************")
        city()
w=1

#main_program
a="WELCOME"
r="LET'S START THE JOURNEY"
print(a.center(87,"-"))
print()
print(r.center(87,"-"))
city()
while w!=0:
    b=input("SELECT YOUR CITY(1/2/3/4) : ")
    choice(b)
ctype=''
ctype1=''
xx=0
#vehicle_selection
def vehicle():
    flag=False
    while flag==False:
        Car=[['Swift','ALTO','Celerio','Ignis','Santro','KWID','Tiago','Altroz'],['Ciaz','Elantra','Verna','Xcent','Honda Amaze','Dzire','Tigor',],['Ertiga','Nexon','Vitara Brezza','Creta','Safari','Fortuner','Innova','Duster','Bolero','XUV500','Scorpio'],['Mercedes Benz GLS','Land Rover Range Rover','BMW 7 Series','Mercedes Benz S Class','Mini Cooper','AUDI A3','AUDI Q3','BMW M4','Land Rover Defender']]
        print('---------------------------------------------------------------------------------------')
        print("CHOOSE YOUR RIDE\nMini (Rs.5 per km)\nSedan (Rs.7 per km)\nSUV (Rs.10 per km)\nVIP (Rs.15 per km)\nENTER HERE: ")
        ch=input();global xx;global ctype;global ctype1
        ch=ch.title();ctype=ch
        if ch=='Mini':
            print('---------------------------------------------------------------------------------------')
            print("Choose your car as displayed below:");xx=5
            for i in range (len(Car[0])):
                print(i,':',Car[0][i])
            fl=False
            while fl==False: 
                ch1=input()
                if ch1.isdigit() and int(ch1)<=len(Car[0])-1 and int(ch1)>=0:
                    fl=True
                else:
                    print('PLEASE ENTER A VALID INPUT!!!!')
            print("Vehicle Selected by you : ",Car[0][int(ch1)]);ctype1=Car[0][int(ch1)]
            flag=True
        elif ch=='Sedan':
            print('---------------------------------------------------------------------------------------')
            print("Choose your car as displayed below:");xx=7
            for i in range (len(Car[1])):
                print(i,':',Car[1][i])
            fl=False
            while fl==False: 
                ch1=input()
                if ch1.isdigit() and int(ch1)<=len(Car[1])-1 and int(ch1)>=0:
                    fl=True
                else:
                    print('PLEASE ENTER A VALID INPUT!!!!')
            print("Vehicle Selected by you : ",Car[1][int(ch1)]);ctype1=Car[1][int(ch1)]
            flag=True
        elif ch=='Suv':
            print('---------------------------------------------------------------------------------------')
            print("Choose your car as displayed below:");xx=10
            for i in range (len(Car[2])):
                print(i,':',Car[2][i])
            fl=False
            while fl==False: 
                ch1=input()
                if ch1.isdigit() and int(ch1)<=len(Car[2])-1 and int(ch1)>=0:
                    fl=True
                else:
                    print('PLEASE ENTER A VALID INPUT!!!!')
            print("Vehicle Selected by you : ",Car[2][int(ch1)]);ctype1=Car[2][int(ch1)]
            flag=True
        elif ch=='Vip':
            print('---------------------------------------------------------------------------------------')
            print("Choose your car as displayed below:");xx=15
            for i in range (len(Car[3])):
                print(i,':',Car[3][i])
            fl=False
            while fl==False: 
                ch1=input()
                if ch1.isdigit() and int(ch1)<=len(Car[3])-1 and int(ch1)>=0:
                    fl=True
                else:
                    print('PLEASE ENTER A VALID INPUT!!!!')
            print("Vehicle Selected by you : ",Car[3][int(ch1)]);ctype1=Car[3][int(ch1)]
            flag=True
        else :
            print("Please enter a valid input!!!!")
vehicle()



print('---------------------------------------------------------------------------------------')
cn=input("Enter customer name: ")
x=['Akash Singh', 'Arav Kumar', 'Chaitanya', 'Keshav Jha', 'Pramod Lal', 'Md. Sameer', 'Tausif Ansari', 'Shayan Sheikh', 'Anthony' , 'David J', 'James Harry']
driver=x[random.randint(0,len(x)-1)]
y=['5375055000', '2256908300', '7382762412', '3818778207', '2189431313', '9279858888', '3208669778', '1227171810', '6878296044', '254736782', '2866696817']
dno=random.choice(y)
flag=1
while flag:
    phn=input("Enter your phone number:")
    if len(phn)==10 and phn.isdigit()==True:
        flag=0
    else:
        print("INVALID PHONE NUMBER(must be of 10 digits!!)")
        flag=1
#print("We charge Rs 2.5 per km for AC")
ac=input("Enter 'y' for AC or any other key for non-AC (Additional charge of Rs 2.5 per km will be applied for Ac) : ")
print('Car number : ',carno,type(carno))
print("Starting point : ",sp,type(sp))
print("Stopping point : ",dp,type(dp))
print("Total distance : ",dist,type(dist))
dprice,aprice=0.0,0.0
acc=''
if ac in 'yY':
    dprice=round(dist*xx,2)
    aprice=round(dist*2.5,2)
    acc='AC'
else :
    dprice=round(dist*xx,2)
    aprice=0.0
    acc='NON-AC'
print("Driver's name : ",driver,type(driver))
print("Driver's number : ",dno,type(dno))

d=dt.date.today();tm=dt.datetime.now()
tm=dt.datetime.now()
if tm.hour>12:
    time=str(tm.hour-12)+':'+str(tm.minute)+' PM'
    time2=str(tm.hour-11)+':'+str(tm.minute)+' PM'
else:
    time=str(tm.hour)+':'+str(tm.minute)+' AM';time2=str(tm.hour-11)+':'+str(tm.minute)+' AM'
print("************************************************************************************************************************************************************")
print("*                                                           GOLDEN QUADRILATERAL CAB SERVICES                                                              *")
print("************************************************************************************************************************************************************")
print("NAME OF CUSTOMER:",cn,end='');print(' '*(38-len(cn)),end='');print('                                                                      ___')
print("                                                       ",end='');print('                                               ____......--------''       \ ')
print("NAME OF DRIVER:",driver,end='');print(' '*(40-len(driver)),end='');print("                                         _..-'                                 \--. ")
print("                                                       ",end='');print("                                  -----------------------------_______   \ ")
print("PICKUP POINT:",sp,end='');print(' '*(42-len(sp)),end='');print("                                  \\                                            `\  ) ")
print("                                                       ",end='');print("                                   |\                  `.   || :         :        \ / ")
print("DESTINATION:",dp,end='');print(' '*(42-len(dp)),end='');print("                                   ||                   .   '' `.........'        |/ ")
print("                                                       ",end='');print("                                   ||              .----._ .| -  -   -  .  .     // ")
print("JOURNEY TIME:",(dist*2)," MINS(approximate)",end='');print(' '*(42-24),end='');print("                                   ||            _//     \\||- - . _  _       `\// ")
print("                                                       ",end='');print("                                   |-..-------------.._  ||           \     __| ")
print("TYPE OF CAR:",ctype,end='');print(' '*(43-5),end='');print("                         V        .        U             `-||         _.---'  | ")
print("                                                       ",end='');print("                         |     . '                     .   |\___.--'  |       | ")
print("BILLING DATE:",str(d.day)+'.'+str(d.month)+'.'+str(d.year),end='');print(' '*(42-9),end='');print("                        ( )_-'                     .        \           |    == | ")
print("                                                       ",end='');print("                     .-----.`-.               .            __       ==|     .-.__ ")
print("MODEL OF CAR:",ctype1,end='');print(' '*(42-11),end='');print("             ._     /       \  \         .              .-'    `\       |    /   .-\ ")
print("                                                       ",end='');print("            /::\\  |/---.---.\ .-.  .                  /     _ \      |   /   /   \ ")
print("CAR NO:",carno,end='');print(' '*(48-12),end='');print("           |::::|\ ||||||||||./:::\-_        ..iiii   /     /   \ \     |  /   / -. | ")
print("                                                       ",end='');print("        __.|::::|/ |||||||||||:::::, \ iiiiiiiiiiii  /     / |   \ |    | /   .'d8b\| ")
print("REFRESHMENTS:","YES",end='');print(' '*(42-3),end='');print("      .'    \:://-_|||:G_Q:|||:::::| | iiiiiiiiiiii .     / \| / | |    |/    |   8b| ")
print("                                                       ",end='');print("   .-'       //  \ |||||||||||\::::|/  iiiiiiiiiiii |    .'_ \/\ | |  _-/     | \ `8 ")
print("AC/NON AC:",acc,end='');print(' '*(45-2),end='');print("  /         //    \||||||||||||`--'\\  ii-'       `-.    |  `-   | |-'  |     |\   8 ")
print("                                                       ",end='');print(" |      _   `      |||||||||||=   -'\\-'          _`\  |----() | |    |_    |-().8 ")
print("DISTANCE:",str(dist)+' kms',end='');print(' '*(46-len(str(dist))-4),end='');print(" |_.-' \         ||||||||||/ \--o\/          .-'   `\\ |  _'// | | .-'  `--.|/ .8P ")
print("                                                       ",end='');print("   /    / \        |||||||||(   )-/'         .'        \\\-' /\ /  ''      .-'| //8 ")
print("START TIME:",time,end='');print(' '*(44-len(time)),end='');print("  /    /   \     -\ \|||||||`-'|/          /  d888b.   `\  |/ /  '     .-'|  8/8' ")
print("                                                       ",end='');print("8o,   .     \ -'.-'\   ''''''' |          /.d8P `Q88b   \\\_/  /    .'    \ `88' ")
print("END TIME:",time2,end='');print(' '*(46-len(time2)),end='');print("`OO88o|      =/-'    `-.__/ \        /dP' \   \88\   \\   /  _.'       `--' ") 
print("                                                       ",end='');print("8OO `8888ooo \\                   `------'dP   | /  .88\   `==-'_.' ")
print("TOTAL PRICE:",'Rs.'+str(dprice+aprice),end='');print(' '*(43-5),end='');print("  `888o   `88888oo               _  /    .P    \|    88 `-.___' ")
print("                                                       ",end='');print("  `   `8888ooo  `o8888oooo    __-|   .dP    | / |88  ")
print("                                                       ",end='');print("   \    `-.``888oo._``8888OO8888888oo dP  `-. |   |88")
print("                                                       ",end='');print("    \.          /``8888ooo  OO    `-888 8           |88")
print("                                                       ",end='');print("      `-.___.'      ``8888OO888888ooo 8------(()| 88/")
print("                                                       ",end='');print("                                   |888 8      /\/ /88") 
print("                                                       ",end='');print("                                   |    8     / | /88/")
print("                                                       ",end='');print("                                   |    8    /|  /d8/")
print("                                                       ",end='');print("                                   `    88  /   /d8/")
print("                                                       ",end='');print("                                    \   `88b---888/")
print("                                                       ",end='');print("                                     \   `888888P'")
print("                                                       ",end='');print("                                      `-._.-''')")
print("************************************************************************************************************************************************************")
print("************************************************************************************************************************************************************")




    












        
        
