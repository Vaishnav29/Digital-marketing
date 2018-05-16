# Target marketing GUI
from tkinter import *
import pandas as pd
import pickle
import sys
import os
import smtplib
from tkinter import messagebox
global i

# loading dumped datafiles
At_Risk_Customers = pickle.load(open("At_Risk_Customers_cust1.p", "rb"))
Bigspenders = pickle.load(open("Bigspenders_cust1.p", "rb"))
Cannot_lose_these_customers = pickle.load(open("Cannot_lose_these_customers1.p", "rb"))
Customers_Needing_Attention = pickle.load(open("Customers_Needing_Attention_cust1.p", "rb"))
Lost_Customers = pickle.load(open("Lost_Customers1.p", "rb"))
Lost_Inconsequential_Customers = pickle.load(open("Lost_Inconsequential_Customers1.p", "rb"))
Promising_Customers = pickle.load(open("Promising_cust1.p", "rb"))
Best_Customers = pickle.load(open("best_cust1.p", "rb"))
Loyal_Customers= pickle.load(open("loyal_cust1.p", "rb"))
Custid= pickle.load(open("custid.p", "rb"))
data = pickle.load(open("data.p", "rb"))

# window configuration
root = Tk()
root.geometry("900x600")
root.configure(background='#7E85AB')
root.title("Target Marketing")
root.resizable(0,0)

one = ['reddy.vaishnav96@gmail.com']
two = ['premalathanair@gmail.com']
three=['madhuhasareddy@gmail.com']
four =['rahulmonish.mec@gmail.com']
five=['shyamalayadav09@gmail.com']
six=['bhavanatangirala25@gmail.com']
seven = ['shambhavi070695@gmail.com']
eight = ['prasadgautham95@gmail.com']
nine=['madhuhasareddy@gmail.com']
ten =['rahulmonish.mec@gmail.com']
eleven=['shyamalayadav09@gmail.com']
twelve=['bhavanatangirala25@gmail.com']
thirteen = ['reddy.vaishnav96@gmail.com']
fourteen = ['prasadgautham95@gmail.com']
fifteen=['madhuhasareddy@gmail.com']
sixteen =['rahulmonish.mec@gmail.com']
seventeen=['shyamalayadav09@gmail.com']

subcust=[]
subcust=[one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen]

# 
def sendmail():
    print(k)
    global message
    mailids=[]
    mailids = subcust[k]
    for i in range(len(mailids)):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # Authentication
        s.login("musicmetalmania@gmail.com","musicmetalmania123")
        temp = ''
        # message to be sent
        message = "Digital Marketing Welcomes you to our World , You are having offers on our products, so please come and visit our store"
        temp = message
        message += "  because  " 
        message += UniqueCats[k]
        message += " products are on a sale for 50% discount only for you."
        print(message)
       
        # sending the mail
        s.sendmail("musicmetalmania@gmail.com", mailids[i], message)
        message = temp
        print(message)
         
        # terminating the session
        messagebox.showinfo("Status", "Promotions have been sent!!!")
        s.quit()

one1 = ['reddy.vaishnav96@gmail.com']
two1 = ['premalathanair@gmail.com']
three1=['madhuhasareddy@gmail.com']
four1 =['rahulmonish.mec@gmail.com']
five1=['shyamalayadav09@gmail.com']
six1=['bhavanatangirala25@gmail.com']
seven1=['reddy.vaishnav96@gmail.com']
eight1=['prasadgautham95@gmail.com']
nine1=['reddy.vaishnav96@gmail.com']
subcust1=[]
subcust1=[one1,two1,three1,four1,five1,six1,seven1,eight1,nine1]

def sendmail1():
    print(x)
    global message
    mailids=[]
    mailids = subcust1[x]
    r =''
    for i in uniquep:
        r+= ' ' 
        r+= i
        r+=' '
    for i in range(len(mailids)):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # Authentication
        s.login("musicmetalmania@gmail.com","musicmetalmania123")
        temp = ''
        # message to be sent
        message = "Digital Marketing Welcomes you to our World , You are having offers on our products, so please come and visit our store"
        temp = message
        message += "  because  " 
        message += r
        message += " products are on a sale for 25% discount only for you."
        print(message)
       
        # sending the mail
        s.sendmail("musicmetalmania@gmail.com", mailids[i], message)
        message = temp
        print(message)
         
        # terminating the session
        messagebox.showinfo("Status", "Promotions have been sent!!!")
        s.quit()

def getproduct(value):
    global uniquep
    global listbox2
    uniquep = set()  
    global x
    i = 1
    listbox1.delete(0, END)
    print(cat.get())
    if cat.get() == 'Best Customers':
        x = Cluster.index(cat.get())
        for key in Best_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Best_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Best_Customers.values())
    
    if cat.get() == 'Loyal Customers':
        x = Cluster.index(cat.get())
        for key in Loyal_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Loyal_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Loyal_Customers.values())
    
    if cat.get() == 'Big Spenders':
        x = Cluster.index(cat.get())
        for key in Bigspenders:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Bigspenders[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep = set(Bigspenders.values())
    
    if cat.get() == 'Promising Customers':
        x = Cluster.index(cat.get())
        for key in Promising_Customers:
            listbox1.insert(END,'{}. {}'.format(i, key, Promising_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Promising_Customers.values())
    
    
    if cat.get() == 'Customers Needing Attention':
        x = Cluster.index(cat.get())
        for key in Customers_Needing_Attention:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Customers_Needing_Attention[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Customers_Needing_Attention.values())    
    
    if cat.get() == 'At Risk Customers':
        x = Cluster.index(cat.get())
        for key in At_Risk_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, At_Risk_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(At_Risk_Customers.values())
    
    if cat.get() == 'Cannot lose these customers':
        x = Cluster.index(cat.get())
        for key in Cannot_lose_these_customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Cannot_lose_these_customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Cannot_lose_these_customers.values())
    
    if cat.get() == 'Lost Customers':
        x = Cluster.index(cat.get())
        for key in Lost_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Lost_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
            uniquep.clear()
        uniquep.clear()
        uniquep = set(Lost_Customers.values())
    
    if cat.get() == 'Lost Inconsequential Customers':
        x = Cluster.index(cat.get())
        for key in Lost_Inconsequential_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Lost_Inconsequential_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Lost_Inconsequential_Customers.values())
    listbox2.delete(0, END)
    for i in uniquep:
        listbox2.insert(END, i)
    listbox2.forget()    

def getcustomer(value):
    print(sub.get())
    i = 1
    global cust
    global p
    global k
    
    
    cust = []
    listbox3.delete(0, END)
    if sub.get() in UniqueCats:
        k = UniqueCats.index(sub.get())
        print(k)
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[k]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
        #message += UniqueCats[k]       
    
    p = len(cust)
    #listbox4 = Listbox(root, height = 0, width = 0)
    #listbox4.place(relx = 0.78, rely = 0.7)
    listbox4.delete(0, END)
    listbox4.insert(END, p)      

# cluster
listbox1 = Listbox(root, width = 30)
listbox1.place(relx = 0.20, rely = 0.4, anchor = "center")  
listbox2 = Listbox(root, width = 30, height = 10)
listbox2.place(relx = 0.1, rely = 0.55) 

global UniqueCats    
Cluster = ['Best Customers','Loyal Customers','Big Spenders','Promising Customers','Customers Needing Attention','At Risk Customers','Cannot lose these customers','Lost Customers','Lost Inconsequential Customers']
UniqueCats = list(data['Sub-Category'].unique())
catLabel = Label(root,text='Select a Cluster', background='#7E85AB', fg = 'white')
catLabel.place(relx = 0.03, rely = 0.09)

getproduct('val')
cat = StringVar(root)
cat.set(Cluster[0])
catDropdown = OptionMenu(root,cat,*Cluster, command=getproduct)
catDropdown.configure(fg = 'black')
catDropdown.place(relx = 0.13, rely = 0.08)

l1 = Label(root,text='-'*300, background='#7E85AB')
l1.place(relx = 0, rely = 0.18)

bp = Label(root,text='Customer ID - Best Categories',width=25, background='#7E85AB', fg = 'white')
bp.place(relx = 0.1, rely = 0.21)

offerLabel = Label(root,text='Offers: ', background='#7E85AB', fg = 'white')
offerLabel.place(relx = 0.05, rely = 0.55)

# sub categories
listbox3 = Listbox(root, width = 30, height = 15)
listbox3.place(relx = 0.75, rely = 0.47, anchor = "center")
listbox4 = Listbox(root, height = 0, width = 3)
listbox4.place(relx = 0.78, rely = 0.73)

subLabel = Label(root,text='Select Sub-Category', background='#7E85AB', fg = 'white')
subLabel.place(relx = 0.55, rely = 0.09)

getcustomer('val')
sub = StringVar(root)
sub.set(UniqueCats[0])
subDropdown = OptionMenu(root,sub,*UniqueCats,command=getcustomer)
subDropdown.configure(fg = 'black')
subDropdown.place(relx = 0.68, rely = 0.08)

cc = Label(root,text='Customer ID',width=20, background='#7E85AB', fg = 'white')
cc.place(relx = 0.68, rely = 0.21)

tc = Label(root,text='Total Customers in the category:', background='#7E85AB', fg = 'white')
tc.place(relx = 0.58, rely = 0.73)

sp = Button(root, text = "Send Promotions",command= sendmail1 ,width = 20, fg = 'black')
sp.place(relx = 0.12, rely = 0.85)

sp1 = Button(root, text = "Send Promotions",command= sendmail, width = 20, fg = 'black')
sp1.place(relx = 0.7, rely = 0.85)


root.mainloop()
