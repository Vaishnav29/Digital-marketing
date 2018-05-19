from tkinter import *
import pickle
global fur
global q
fur = sorted(pickle.load(open("fur1.p", "rb")))
off = sorted(pickle.load(open("off1.p", "rb")))
tec = sorted(pickle.load(open("tec1.p", "rb")))
product = pickle.load(open("Product_Recommendation.p", "rb"))
data = pickle.load(open("4yrsBMW.p", "rb"))
data = data[:370]


root = Tk()
root.title("Personalized Experience (Product Recommendation)")
root.configure(background='RoyalBlue3')
root.geometry("900x600")
root.resizable(0,0)



def doprintfur(val):
    
    print(fu.get())
    #listb = Listbox(root, width = 40, height = 15)
    
    for i in range(len(data['d_product'])):
        if data['d_product'][i] == fu.get():
            print(i)
            Recommendations=[]
            for u in range(len(product[i])):
                if (product[i]['score'][u] > 0):
                    Recommendations.append(product[i]['item2'][u])
            print("\n\n Recommendations for",data['d_product'][i]," \n",Recommendations[:5])
    listb1.delete(0, END)
    listb1.insert(END, 'Selected product :')
    listb1.insert(END, '{}'.format(fu.get()))
    b = 1
    Recommendations= sorted(Recommendations[:5])
    for a in Recommendations[:5]:
        listb1.insert(END, '{}. {}'.format(b, a))
        b+=1
            
def doprintoff(val):
    
    print(of.get())
    #listb = Listbox(root, width = 40, height = 15)
    
    for i in range(len(data['d_product'])):
        if data['d_product'][i] == of.get():
            print(i)
            Recommendations=[]
            for u in range(len(product[i])):
                if (product[i]['score'][u] > 0):
                    Recommendations.append(product[i]['item2'][u])
            print("\n\n Recommendations for",data['d_product'][i]," \n",Recommendations[:5])
    listb2.delete(0, END)
    listb2.insert(END, 'Selected product :')
    listb2.insert(END, '{}'.format(of.get()))
    b = 1
    Recommendations= sorted(Recommendations[:5])
    for a in Recommendations[:5]:
        listb2.insert(END, '{}. {}'.format(b, a))
        b+=1


def doprinttec(val):
    global Recommendations
    Recommendations = []
    print(te.get())
    #listb = Listbox(root, width = 40, height = 15)
    
    for i in range(len(data['d_product'])):
        if data['d_product'][i] == te.get():
            print(i)
            for u in range(len(product[i])):
                if (product[i]['score'][u] > 0):
                    Recommendations.append(product[i]['item2'][u])
            print("\n\n Recommendations for",data['d_product'][i]," \n",Recommendations[:5])
    listb3.delete(0, END)
    listb3.insert(END, 'Selected product :')
    listb3.insert(END, '{}'.format(te.get()))
    b = 1
    Recommendations= sorted(Recommendations[:5])
    for a in Recommendations[:5]:
        listb3.insert(END, '{}. {}'.format(b, a))
        b+=1

Label(root,  text='|'*50, wraplength=1 , background='RoyalBlue3').place(relx = 0.34, rely = 0)
      
Label(root,  text='|'*50, wraplength=1 , background='RoyalBlue3').place(relx = 0.665, rely = 0)

toprec = Label(root, text = 'Top 5 recommendations for the selected \n furniture product : ', background='RoyalBlue3', fg = 'white')
toprec.place(relx = 0.05, rely = 0.33)

Label(root, text = 'Top 5 recommendations for the selected \n office product : ', background='RoyalBlue3', fg = 'white').place(relx = 0.365, rely = 0.33)

Label(root, text = 'Top 5 recommendations for the selected \n technology product : ', background='RoyalBlue3', fg = 'white').place(relx = 0.695, rely = 0.33)

           
listb1 = Listbox(root, width = 40, height = 8)
listb1.place(relx = 0.05, rely = 0.4)

listb2 = Listbox(root, width = 40, height = 8)
listb2.place(relx = 0.37, rely = 0.4)

listb3 = Listbox(root, width = 40, height = 8)
listb3.place(relx = 0.7, rely = 0.4)

furLabel = Label(root,text='Furniture Products : ', background='RoyalBlue3', fg = 'white')
furLabel.place(relx = 0.05, rely = 0.09)

fu = StringVar(root)
fu.set(fur[0])
furDropdown = OptionMenu(root, fu,*fur, command=doprintfur)
furDropdown.configure(width = '30', anchor = 'w')
furDropdown.place(relx = 0.05, rely = 0.12)

offLabel = Label(root,text='Office Products : ', background='RoyalBlue3', fg = 'white')
offLabel.place(relx = 0.37, rely = 0.09)

of = StringVar(root)
of.set(off[0])
offDropdown = OptionMenu(root, of,*off, command=doprintoff)
offDropdown.configure(width = '30', anchor = 'w')
offDropdown.place(relx = 0.37, rely = 0.12)

tecLabel = Label(root,text='Technology Products : ', background='RoyalBlue3', fg = 'white')
tecLabel.place(relx = 0.70, rely = 0.09)

te = StringVar(root)
te.set(tec[0])
tecDropdown = OptionMenu(root, te,*tec, command=doprinttec)
tecDropdown.configure(width = '30', anchor = 'w')
tecDropdown.place(relx = 0.70, rely = 0.12)

root.mainloop()