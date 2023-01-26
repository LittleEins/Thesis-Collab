# Libraries
from tkinter import *
from PIL import ImageTk, Image
import csv
window = Tk()

#Windows Setup
window.geometry('800x600') # windowdow size
window.resizable(width=0, height=0) # set the windowdow not resizable
window.title("Fruit Stands v.0.1.1") # windowdow title
window.iconbitmap(r'src\app.ico') # windowdow icon

#Constants
bg_default = '#d87644'
bg_btn = '#be4a2f'
bg_light = '#e4a672'
bg_grass = '#5fc14c'
bg_error = '#e43b44'
no_img = Image.open('src/img/error.png')

info = "Please choose your preferred \nfood stand: "
len_info = len(info)
#Functions
def home():
        main_frame.pack()
        global npc_res,npc_res2,border_res
        npc_img = Image.open("src/img/npc.png")
        npc_img2 = Image.open("src/img/npc2.png")
        border_img = Image.open("src/img/border.png")

        resize_npc = npc_img.resize((300,300))
        resize_npc2 = npc_img2.resize((300,300))
        resize_border = border_img.resize((800,100))

        npc_res = ImageTk.PhotoImage(resize_npc)
        npc_res2 = ImageTk.PhotoImage(resize_npc2)
        border_res = ImageTk.PhotoImage(resize_border)
        
        npc = Label(main_frame,image=npc_res,bg=bg_default)
        npc2 = Label(main_frame,image=npc_res2,bg=bg_default)
        border = Label(main_frame,image=border_res,bg=bg_default)

        title = Label(main_frame, width = 25, height = 1,text = 'Python Project',
        font='Courier 25 bold',relief=SUNKEN,fg='white',bg=bg_btn)

        title.place(x=150,y=100)
        border.place(x=0,y=500)
        npc.place(x=0,y=200)
        npc2.place(x=500,y=200)
        menu_btn.place(x=345,y=300)

def clean_area():#Used to remove widgets in main_frame
    for frame in main_frame.winfo_children():
        frame.destroy()
    print("Frame destroyed succesfully")
def check():
    print("Working!")
def check_stocks():
    hasError = 0
    if int(box1.get()) > int(stocks[0]):
        hasError += 1
        box1.config(bg=bg_error)
        total.config(text="Not Enough")
    if int(box2.get()) > int(stocks[1]):
        hasError += 1
        box2.config(bg=bg_error)
        total.config(text="Not Enough")
    if int(box3.get()) > int(stocks[2]):
        hasError += 1
        box3.config(bg=bg_error)
        total.config(text="Not Enough")
    if int(box4.get()) > int(stocks[3]):
        hasError += 1
        box4.config(bg=bg_error)
        total.config(text="Not Enough")
    if int(box5.get()) > int(stocks[4]):
        hasError += 1
        box5.config(bg=bg_error)
        total.config(text="Not Enough")
    if hasError >= 1:
        return 0
def reset_stats():
    box1.config(bg='white')
    box2.config(bg='white')
    box3.config(bg='white')
    box4.config(bg='white')
    box5.config(bg='white')
    total.config(bg=bg_default)

def calcu():
    print("Calc working!")
    try:
        if(check_stocks()!=0):
            num1 = int(box1.get()) * int(value[0])
            num2 = int(box2.get()) * int(value[1])
            num3 = int(box3.get()) * int(value[2])
            num4 = int(box4.get()) * int(value[3])
            num5 = int(box5.get()) * int(value[4])

            sum = num1+num2+num3+num4+num5
            total.config(text=sum)
            reset_stats()
    except:
        total.config(bg=bg_error,text="ERROR")
def item1():
    global item01
    try:
        item_img = Image.open(source[0])
        item_res = item_img.resize((100,100))
    except:
        item_res = no_img.resize((100,100))
    item01 = ImageTk.PhotoImage(item_res)
    img_lbl.config(image=item01)
    item_name.config(text=name[0])
    menu_info.config(text=description[0])
def item2():
    global item02
    try:
        item_img = Image.open(source[1])
        item_res = item_img.resize((100,100))
    except:
        item_res = no_img.resize((100,100))
    item02 = ImageTk.PhotoImage(item_res)
    img_lbl.config(image=item02)
    item_name.config(text=name[1])
    menu_info.config(text=description[1])
def item3():
    global item03
    try:
        item_img = Image.open(source[2])
        item_res = item_img.resize((100,100))
    except:
        item_res = no_img.resize((100,100))
    item03 = ImageTk.PhotoImage(item_res)
    img_lbl.config(image=item03)
    item_name.config(text=name[2])
    menu_info.config(text=description[2])
def item4():
    global item04
    try:
        item_img = Image.open(source[3])
        item_res = item_img.resize((100,100))
    except:
        item_res = no_img.resize((100,100))
    item04 = ImageTk.PhotoImage(item_res)
    img_lbl.config(image=item04)
    item_name.config(text=name[3])
    menu_info.config(text=description[3])
def item5():
    global item05
    try:
        item_img = Image.open(source[4])
        item_res = item_img.resize((100,100))
    except:
        item_res = no_img.resize((100,100))
    item05 = ImageTk.PhotoImage(item_res)
    img_lbl.config(image=item05)
    item_name.config(text=name[4])
    menu_info.config(text=description[4])

def display_csv(dictreader):
    display = Frame(main_frame,bg=bg_light,width=650, height=340)
    display.place(x=80,y=200)
    r = 0
    global name,value,stocks,description,source
    name=[]
    value=[]
    stocks=[]
    source = []
    description = []
    global box1,box2,box3,box4,box5,total
    for row in dictreader:
        name.append(row['Name'])
        value.append(row['Value'])
        stocks.append(row['Stocks'])
        description.append(row['Description'])
        source.append(row['Source'])
    #Labels
    label1 = Label(display, width = 25, height = 1,text = 'Name',
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_btn)
    label1.place(x=50,y=10)
    label2 = Label(display, width = 10, height = 1,text = 'Value',
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_btn)
    label2.place(x=275,y=10)
    label3 = Label(display, width = 10, height = 1,text = 'Stocks',
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_btn)
    label3.place(x=375,y=10)
    label4 = Label(display, width = 11, height = 1,text = 'Input',
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_btn)
    label4.place(x=475,y=10)
    #Loops to create the table
    for i in range(0,len(name)):
        label_name = Label(display, width = 25, height = 1,text = name[i],
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_default)
        label_value = Label(display, width = 10, height = 1,text = value[i],
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_default)
        label_stocks = Label(display, width = 10, height = 1,text = stocks[i],
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_default)

        if r == 0:
            label_name.place(x=50,y=40)
            label_value.place(x=275,y=40)
            label_stocks.place(x=375,y=40)
            
        else:
            label_name.place(x=50,y=35*(r+1))
            label_value.place(x=275,y=35*(r+1))
            label_stocks.place(x=375,y=35*(r+1))
            
        r += 1 #index/counter
    #Global Spinbox
    box1 = Spinbox(display, command=item1,width=9, from_=0, to=stocks[0],
    font='Courier 14 bold', bg='white',justify=CENTER)
    box2 = Spinbox(display, width=9, from_=0, to=stocks[1],
    font='Courier 14 bold', bg='white',justify=CENTER)
    box3 = Spinbox(display, width=9, from_=0, to=stocks[2],
    font='Courier 14 bold', bg='white',justify=CENTER)
    box4 = Spinbox(display, width=9, from_=0, to=stocks[3],
    font='Courier 14 bold', bg='white',justify=CENTER)
    box5 = Spinbox(display, width=9, from_=0, to=stocks[4],
    font='Courier 14 bold', bg='white',justify=CENTER)

    #Spinbox Placements
    box1.place(x=480,y=40)
    box2.place(x=480,y=35*(1+1))
    box3.place(x=480,y=35*(2+1))
    box4.place(x=480,y=35*(3+1))
    box5.place(x=480,y=35*(4+1))
    
    #Total Area
    total_lbl = Label(display, width = 10, height = 1,text = "TOTAL",
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_btn)
    total_lbl.place(x=480,y=35*(5+1))
    total = Label(display, width = 10, height = 1,text = "0",
        font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_default)
    total.place(x=480,y=35*(5+1))
    calc = Button(display,bg=bg_default,text="Calculate",
    font='Courier 14 bold', justify=CENTER)
    calc.config(command=calcu)
    calc.place(x=480,y=35*(6+1))

    #Item photo
    global itemImg,img_lbl
    item_img = Image.open("src/img/0.png")
    item_res = item_img.resize((100,100))
    itemImg = ImageTk.PhotoImage(item_res)
    img_lbl = Button(main_frame,bg=bg_default,image=itemImg)
    img_lbl.place(x=625,y=75)

    #Item Description 
    info1 = Button(display,bg=bg_default,text="Info",
    font='Courier 10 bold', justify=CENTER)
    info2 = Button(display,bg=bg_default,text="Info",
    font='Courier 10 bold', justify=CENTER)
    info3 = Button(display,bg=bg_default,text="Info",
    font='Courier 10 bold', justify=CENTER)
    info4 = Button(display,bg=bg_default,text="Info",
    font='Courier 10 bold', justify=CENTER)
    info5 = Button(display,bg=bg_default,text="Info",
    font='Courier 10 bold', justify=CENTER)
    #Item Description Configs
    info1.config(command=item1)
    info2.config(command=item2)
    info3.config(command=item3)
    info4.config(command=item4)
    info5.config(command=item5)
    #Item Description Placements
    info1.place(x=0,y=40)
    info2.place(x=0,y=35*(1+1))
    info3.place(x=0,y=35*(2+1))
    info4.place(x=0,y=35*(3+1))
    info5.place(x=0,y=35*(4+1))

    #Top UI
    global menu_info,item_name
    item_name = Label(main_frame,text="Item Name",width=15,
    font='Courier 12 bold',relief=GROOVE,fg='white',bg=bg_default)
    item_name.place(x=300,y=114)
    menu_info = Label(main_frame,text="Please click Info for Item description.",width=len_info,
    font='Courier 12',relief=SUNKEN,fg='white',bg=bg_default)
    menu_info.place(x=214-len_info,y=140)


        
def fruit():
    clean_area()
    print("Fruit function called successfully")
    menu_frame = Frame(main_frame,bg='#be4a2f',width=800, height=500)
    menu_frame.pack(pady=50,padx=50)
    with open('src/fruits.csv', 'r') as file:
        dictreader = csv.DictReader(file,delimiter=';')
        display_csv(dictreader)
    #back_button
    global back
    back_img = Image.open("src/img/back.png")
    back_resize = back_img.resize((50,50))
    back = ImageTk.PhotoImage(back_resize)
    back_btn = Button(menu_frame,bg=bg_default,image=back,text="Home")
    #Config
    back_btn.config(command=menu)
    #Placements
    back_btn.place(x=50,y=50)
    #Labels
    menu_lbl = Label(menu_frame,text='Fruit Stand',width=14,font='Courier 25 bold',relief=SUNKEN,fg='white',bg=bg_default)
    #Menu Label
    menu_lbl.place(x=200,y=20)

def vegetable():
    clean_area()
    print("Vegetable function called successfully")
    menu_frame = Frame(main_frame,bg='#be4a2f',width=800, height=500)
    menu_frame.pack(pady=50,padx=50)
    with open('src/vegetable.csv', 'r') as file:
        dictreader = csv.DictReader(file,delimiter=';')
        display_csv(dictreader)
    #back_button
    global back
    back_img = Image.open("src/img/back.png")
    back_resize = back_img.resize((50,50))
    back = ImageTk.PhotoImage(back_resize)
    back_btn = Button(menu_frame,bg=bg_default,image=back,text="Home")
    #Config
    back_btn.config(command=menu)
    #Placements
    back_btn.place(x=50,y=50)
    #Labels
    menu_lbl = Label(menu_frame,text='Vegetable Stand',width=17,font='Courier 25 bold',relief=SUNKEN,fg='white',bg=bg_default)
    #Menu Label
    menu_lbl.place(x=175,y=20)

def foods():
    clean_area()
    print("Foods function called successfully")
    menu_frame = Frame(main_frame,bg='#be4a2f',width=800, height=500)
    menu_frame.pack(pady=50,padx=50)
    with open('src/foods.csv', 'r') as file:
        dictreader = csv.DictReader(file,delimiter=';')
        display_csv(dictreader)
    #back_button
    global back
    back_img = Image.open("src/img/back.png")
    back_resize = back_img.resize((50,50))
    back = ImageTk.PhotoImage(back_resize)
    back_btn = Button(menu_frame,bg=bg_default,image=back,text="Home")
    #Config
    back_btn.config(command=menu)
    #Placements
    back_btn.place(x=50,y=50)
    #Labels
    menu_lbl = Label(menu_frame,text='Foods Stand',width=17,font='Courier 25 bold',relief=SUNKEN,fg='white',bg=bg_default)
    #Menu Label
    menu_lbl.place(x=175,y=20)

def menu():
    clean_area()
    print("Menu function called successfully")
    global img1,img2,img3,img4
    menu_frame = Frame(main_frame,bg='#be4a2f',width=800, height=500)
    menu_frame.pack(pady=50,padx=50)

    #Images
    stand1 = Image.open("src/img/stand1.png")
    stand2 = Image.open("src/img/stand2.png")
    stand3 = Image.open("src/img/stand3.png")
    home_img = Image.open("src/img/home.png")

    resize_img1 = stand1.resize((200,300))
    resize_img2 = stand2.resize((200,300))
    resize_img3 = stand3.resize((200,300))
    home_resize = home_img.resize((50,50))

    img1 = ImageTk.PhotoImage(resize_img1)
    img2 = ImageTk.PhotoImage(resize_img2)
    img3 = ImageTk.PhotoImage(resize_img3)
    img4 = ImageTk.PhotoImage(home_resize)

    #buttons
    button1 = Button(menu_frame,bg=bg_grass,image=img1,text="Fruits")
    button2 = Button(menu_frame,bg=bg_grass,image=img2,text="Vegetable")
    button3 = Button(menu_frame,bg=bg_grass,image=img3,text="Foods")
    home_btn = Button(menu_frame,bg=bg_default,image=img4,text="Home")
    #commands
    button1.config(command=fruit)
    button2.config(command=vegetable)
    button3.config(command=foods)
    home_btn.config(command=quit)
    
    #Labels
    menu_lbl = Label(menu_frame,text='Food Stand',width=14,font='Courier 25 bold',relief=SUNKEN,fg='white',bg=bg_default)
    menu_info = Label(menu_frame,text=info,width=len_info,font='Courier 12 bold',relief=SUNKEN,fg='white',bg=bg_default)
    
    stand1_lbl = Label(menu_frame,text='Fruits',width=14,font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_default)
    stand2_lbl = Label(menu_frame,text='Vegetable',width=14,font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_default)
    stand3_lbl = Label(menu_frame,text='Foods',width=14,font='Courier 14 bold',relief=SUNKEN,fg='white',bg=bg_default)

    #Placements
    home_btn.place(x=50,y=50)
    button1.place(x=20,y=140)
    button2.place(x=245,y=140)
    button3.place(x=470,y=140)
    #Menu Label
    menu_lbl.place(x=200,y=20)
    menu_info.place(x=170-len_info,y=75)
    #Stand Labels
    stand1_lbl.place(x=40, y=400)
    stand2_lbl.place(x=265, y=400)
    stand3_lbl.place(x=490, y=400)


#Frames
main_frame = Frame(window,bg=bg_default,width=800,height=600)


#Buttons
menu_btn = Button(main_frame,command=menu,text="Start",font='Courier 20 bold',bg=bg_light,fg='white')

#Function call
home()
#Windows loop
window.mainloop()
