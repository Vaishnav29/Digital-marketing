from tkinter import *
from PIL import Image, ImageTk

global image
root = Tk()
root.geometry('1260x700')
root.configure(background='RoyalBlue3')
selectYearLabel = Label(root, text='Select Year',fg='white',background = 'RoyalBlue3')
selectYearLabel.place(relx=0.25,rely=0.75)
Year = [2017,2016,2015,2014]
year = StringVar(root)
year.set(Year[0])
selectYearOM = OptionMenu(root, year, *Year)
selectYearOM.place(relx=0.245,rely=0.78)
def check():
    global image
    y = int(year.get())
    print(y,type(y))
    if(y==2017):
        image = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\11.png")
    elif(y==2016):
        image = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\10.png")
    elif(y==2015):
        image = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\01.png")
    elif(y==2014):
        image = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\00.png")
    showImage()
    
def showImage():
    global image
    resized = image.resize((600,500), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(resized)
    myvar = Label(root, image=tkimage)
    myvar.image = tkimage
    myvar.grid(row=0,column=0)
    
    image1 = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\cust.png")
    resized = image1.resize((650,500), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(resized)
    myvar = Label(root, image=tkimage)
    myvar.image = tkimage
    myvar.grid(row=0,column=1)
button = Button(root,text='Display Graph', command=check)
button.place(relx=0.24,rely=0.9)

# =============================================================================
# 
# for r in range(2):
#     for c in range(2):
#         image = Image.open("C:\\Users\\user\\Desktop\\Screenshots\\" + str(r)+str(c)+".png")
#         resized = image.resize((675,350), Image.ANTIALIAS)
#         tkimage = ImageTk.PhotoImage(resized)
#         myvar = Label(root,image = tkimage)
#         myvar.image = tkimage
#         myvar.grid(row=r,column=c)

# =============================================================================
root.mainloop()