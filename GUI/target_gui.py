from tkinter import *
import pandas as pd
import pickle
import sys
import os

global i
#import ScrolledText
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

root = Tk()
root.geometry("900x600")
root.title("Target Marketing")

# cluster
Cluster = ['Best Customers','Loyal Customers','Big Spenders','Promising Customers','Customers Needing Attention','At Risk Customers','Cannot lose these customers','Lost Customers','Lost Inconsequential Customers']
UniqueCats = list(data['Sub-Category'].unique())
catLabel = Label(root,text='Select a Cluster')
catLabel.place(relx = 0.03, rely = 0.09)

cat = StringVar(root)
cat.set(Cluster[0])
catDropdown = OptionMenu(root,cat,*Cluster)
catDropdown.place(relx = 0.13, rely = 0.08)

l1 = Label(root,text='-'*300)
l1.place(relx = 0, rely = 0.18)

bp = Label(root,text='Customer ID - Best Categories',width=25,relief='ridge')
bp.place(relx = 0.1, rely = 0.21)

offerLabel = Label(root,text='Offers: ')
offerLabel.place(relx = 0.05, rely = 0.55)

# sub categories
subLabel = Label(root,text='Select Sub-Category')
subLabel.place(relx = 0.55, rely = 0.09)

sub = StringVar(root)
sub.set(UniqueCats[0])
subDropdown = OptionMenu(root,sub,*UniqueCats)
subDropdown.place(relx = 0.68, rely = 0.08)

cc = Label(root,text='Customer ID',width=20,relief='ridge')
cc.place(relx = 0.68, rely = 0.21)

tc = Label(root,text='Total Customers in the category:',width=35)
tc.place(relx = 0.53, rely = 0.7)

def getproduct():
    global uniquep
    global listbox2
    uniquep = set()    
    
    listbox1 = Listbox(root, width = 30)
    listbox2 = Listbox(root, width = 30, height = 10)
    listbox2.place(relx = 0.1, rely = 0.55) 
    i = 1
    
    print(cat.get())
    if cat.get() == 'Best Customers':
        for key in Best_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Best_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Best_Customers.values())
    
    if cat.get() == 'Loyal Customers':
        for key in Loyal_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Loyal_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Loyal_Customers.values())
    
    if cat.get() == 'Big Spenders':
        for key in Bigspenders:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Bigspenders[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep = set(Bigspenders.values())
    
    if cat.get() == 'Promising Customers':
        for key in Promising_Customers:
            listbox1.insert(END,'{}. {}'.format(i, key, Promising_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Promising_Customers.values())
    
    
    if cat.get() == 'Customers Needing Attention':
        for key in Customers_Needing_Attention:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Customers_Needing_Attention[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Customers_Needing_Attention.values())    
    
    if cat.get() == 'At Risk Customers':
        for key in At_Risk_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, At_Risk_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(At_Risk_Customers.values())
    
    if cat.get() == 'Cannot lose these customers':
        for key in Cannot_lose_these_customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Cannot_lose_these_customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Cannot_lose_these_customers.values())
    
    if cat.get() == 'Lost Customers':
        for key in Lost_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Lost_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
            uniquep.clear()
        uniquep.clear()
        uniquep = set(Lost_Customers.values())
    
    if cat.get() == 'Lost Inconsequential Customers':
        for key in Lost_Inconsequential_Customers:
            listbox1.insert(END,'{}. {} - {}'.format(i, key, Lost_Inconsequential_Customers[key]))
            #listbox2.insert(END, '{}. {}'.format(i, ))
            i +=1
        uniquep.clear()
        uniquep = set(Lost_Inconsequential_Customers.values())
        
    listbox1.place(relx = 0.20, rely = 0.4, anchor = "center")  

    for i in uniquep:
        listbox2.insert(END, i)
    listbox2.forget()    

def getcustomer():
    print(sub.get())
    i = 1
    global cust
    global p
    
    cust = []
    listbox3 = Listbox(root, width = 30, height = 15)
    listbox4 = Listbox(root, height = 0, width = 3)
    listbox4.place(relx = 0.78, rely = 0.7)
    
    if sub.get() == UniqueCats[0]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[0]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[1]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[1]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[2]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[2]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[3]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[3]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[4]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[4]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[5]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[5]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[6]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[6]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[7]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[7]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
    
    if sub.get() == UniqueCats[8]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[8]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)            
    if sub.get() == UniqueCats[9]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[9]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
    if sub.get() == UniqueCats[10]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[10]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)            
    if sub.get() == UniqueCats[11]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[11]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
     
    if sub.get() == UniqueCats[12]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[12]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[13]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[13]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)            
    if sub.get() == UniqueCats[14]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[14]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)            
    if sub.get() == UniqueCats[15]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[15]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)
                
    if sub.get() == UniqueCats[16]:
        cust.clear()
        for key,val in Custid.items():
            if val == UniqueCats[16]:      
                listbox3.insert(END, '{}. {}'.format(i, key))
                i +=1
                cust.append(key)  
    p = len(cust)
    #listbox4.destroy()
    #listbox4 = Listbox(root, height = 0, width = 0)
    #listbox4.place(relx = 0.78, rely = 0.7)
    listbox4.insert(END, p)      
    listbox3.place(relx = 0.75, rely = 0.47, anchor = "center")


 
clb= Button(root,text="Select",command= getproduct, width = 10)
clb.place(relx = 0.37, rely = 0.08)

slb= Button(root,text="Select", command = getcustomer, width = 10)
slb.place(relx = 0.81, rely = 0.08)

sp = Button(root, text = "Send Promotions", width = 20)
sp.place(relx = 0.12, rely = 0.85)

sp1 = Button(root, text = "Send Promotions", width = 20)
sp1.place(relx = 0.7, rely = 0.85)

root.mainloop()


