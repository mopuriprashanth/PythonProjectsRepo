
from datetime import datetime

name=input("Enter your name:")

list='''
rice Rs 70/kg
sugar Rs 40/kg
wheat Rs 30/kg
colgate Rs 70/each
maggie Rs 50/kg

'''
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

items={
    'rice':20,
    'sugar':40,
    'wheat':30,
    'colgate':70,
    'maggie':50
}
option=int(input("for list of items press 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your itemsp:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,price,items))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is un available")

    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","prashanth",25*"=")
            print(28*" ","yerraguntla")
            print("name:",name,30*" ","date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","THANKS FOR VISITING.....")
            print(75*"-")
