# Libraries
from tkinter import *
from PIL import ImageTk, Image

win = Tk()

#Windows Setup
win.geometry('800x600') # window size
win.resizable(width=False, height=False) # set the window not resizable
win.title("EAT ME LECIOUS") # window title
win.iconbitmap(r'resources\waffle.ico') # window icon

#Functions
def coffee_func():
    #fastfood
    c_compute1 = int(cspin_box1.get()) * 15
    c_compute2 = int(cspin_box2.get()) * 18
    c_compute3 = int(cspin_box3.get()) * 20
    c_compute4 = int(cspin_box4.get()) * 25

    total_compute = c_compute1 + c_compute2 + c_compute3 + c_compute4

    ctotal_label.config(text=total_compute)

def fastfood_func():
    #fastfood
    b_compute1 = int(bspin_box1.get()) * 15
    b_compute2 = int(bspin_box2.get()) * 25
    b_compute3 = int(bspin_box3.get()) * 60
    b_compute4 = int(bspin_box4.get()) * 80

    total_compute = b_compute1 + b_compute2 + b_compute3 + b_compute4

    btotal_label.config(text=total_compute)

def vegetable_func():
    #vegetable
    v_compute1 = int(vspin_box1.get()) * 15
    v_compute2 = int(vspin_box2.get()) * 34
    v_compute3 = int(vspin_box3.get()) * 40
    v_compute4 = int(vspin_box4.get()) * 10

    total_compute = v_compute1 + v_compute2 + v_compute3 + v_compute4

    vtotal_label.config(text=total_compute)

def coffee(): # destroy all frame on main frame
    for frame in main_frame.winfo_children():
        frame.destroy()

    #second page frame
    cframe = Frame(main_frame,  highlightbackground='black', highlightthickness=2, bg="#524c4c")
    cframe.pack(pady=70)
    cframe.pack_propagate(False)
    cframe.configure(width=730, height=500)

    #global var
    global c1
    global c2
    global c3
    global c4
    global ctotal_label
    global cspin_box1
    global cspin_box2
    global cspin_box3
    global cspin_box4

    #load image
    c_menu1= Image.open("resources/img/coffee/coffee_black.png")
    c_menu2= Image.open("resources/img/coffee/coffee_blangka.png")
    c_menu3= Image.open("resources/img/coffee/coffee_barako.png")
    c_menu4= Image.open("resources/img/coffee/coffee_3and1.png")

    #Resize the Image using resize method
    resized_image1= c_menu1.resize((100,100), Image.ANTIALIAS)
    resized_image2= c_menu2.resize((100,100), Image.ANTIALIAS)
    resized_image3= c_menu3.resize((100,100), Image.ANTIALIAS)
    resized_image4= c_menu4.resize((100,100), Image.ANTIALIAS)
    c1 = ImageTk.PhotoImage(resized_image1)
    c2 = ImageTk.PhotoImage(resized_image2)
    c3 = ImageTk.PhotoImage(resized_image3)
    c4 = ImageTk.PhotoImage(resized_image4)

    #labels
    c_title = Label(main_frame, text="SELECT YOUR COFFEE ORDER", font='Helvetica 30 bold', fg="#aec240")
    ctotal_label = Label(main_frame, text="0", font='Times 20 bold', width=4, height=1, bg="#524c4c")

    #coffee icon
    coffee_black = Label(cframe, image=c1, bg="#524c4c")
    coffee_blangka = Label(cframe, image=c2, bg="#524c4c")
    coffee_barako = Label(cframe, image=c3, bg="#524c4c")
    coffee_3and1 = Label(cframe, image=c4, bg="#524c4c")

    #coffee label
    coffee_black_label = Label(cframe, text="Coffee Black", font='Times 15 bold', bg="#524c4c")
    coffee_blangka_label = Label(cframe, text="Coffee Blangka", font='Times 15 bold', bg="#524c4c")
    coffee_barako_label = Label(cframe, text="Coffee Barako", font='Times 15 bold', bg="#524c4c")
    coffee_3and1_label = Label(cframe, text="Coffee 3 & 1", font='Times 15 bold', bg="#524c4c")

    #coffee price
    coffee_black_price = Label(cframe, text="15", font='Times 15 bold', bg="#524c4c")
    coffee_blangka_price = Label(cframe, text="18", font='Times 15 bold', bg="#524c4c")
    coffee_barako_price = Label(cframe, text="20", font='Times 15 bold', bg="#524c4c")
    coffee_3and1_price = Label(cframe, text="25", font='Times 15 bold', bg="#524c4c")

    #spinbox
    cspin_box1 = Spinbox(cframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    cspin_box2 = Spinbox(cframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    cspin_box3 = Spinbox(cframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    cspin_box4 = Spinbox(cframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")

    #button
    btn_main = Button(main_frame, command=page2, text="MENU", font='Times 15 bold', bg="#aec240")
    cbtn_compute = Button(main_frame, command=coffee_func, text="Compute", font='Times 15 bold', bg="green")

    #labets set position
    c_title.place(x=100, y=50)
    coffee_black.place(x=40, y=25)
    coffee_blangka.place(x=40, y=125)
    coffee_barako.place(x=40, y=225)
    coffee_3and1.place(x=40, y=325)

    coffee_black_label.place(x=200, y=50)
    coffee_blangka_label.place(x=200, y=150)
    coffee_barako_label.place(x=200, y=250)
    coffee_3and1_label.place(x=200, y=350)

    coffee_black_price.place(x=550, y=50)
    coffee_blangka_price.place(x=550, y=150)
    coffee_barako_price.place(x=550, y=250)
    coffee_3and1_price.place(x=550, y=350)


    ctotal_label.place(x=675, y=540)

    #button set position
    btn_main.place(x=360, y=540)
    cbtn_compute.place(x=570, y=540)

    #spinbox set position
    cspin_box1.place(x=600, y=50)
    cspin_box2.place(x=600, y=150)
    cspin_box3.place(x=600, y=250)
    cspin_box4.place(x=600, y=350)

def burger(): # destroy all frame on main frame
    for frame in main_frame.winfo_children():
        frame.destroy()

    #second page frame
    bframe = Frame(main_frame,  highlightbackground='black', highlightthickness=2, bg="#524c4c")
    bframe.pack(pady=70)
    bframe.pack_propagate(False)
    bframe.configure(width=730, height=500)

    #global varb
    global b1
    global b2
    global b3
    global b4
    global btotal_label
    global bspin_box1
    global bspin_box2
    global bspin_box3
    global bspin_box4

    #load image
    b_menu1= Image.open("resources/img/fastfood/small.png")
    b_menu2= Image.open("resources/img/fastfood/chessy.png")
    b_menu3= Image.open("resources/img/fastfood/medium.png")
    b_menu4= Image.open("resources/img/fastfood/overload.png")

    #Resize the Image using resize method
    resized_image1= b_menu1.resize((100,100), Image.ANTIALIAS)
    resized_image2= b_menu2.resize((100,100), Image.ANTIALIAS)
    resized_image3= b_menu3.resize((100,100), Image.ANTIALIAS)
    resized_image4= b_menu4.resize((100,100), Image.ANTIALIAS)
    b1 = ImageTk.PhotoImage(resized_image1)
    b2 = ImageTk.PhotoImage(resized_image2)
    b3 = ImageTk.PhotoImage(resized_image3)
    b4 = ImageTk.PhotoImage(resized_image4)

    #labels
    b_title = Label(main_frame, text="SELECT YOUR FASTFOOD ORDER", font='Helvetica 30 bold', fg="#aec240")
    btotal_label = Label(main_frame, text="0", font='Times 20 bold', width=4, height=1, bg="#524c4c")

    #burder icon
    small = Label(bframe, image=b1, bg="#524c4c")
    chessy = Label(bframe, image=b2, bg="#524c4c")
    medium = Label(bframe, image=b3, bg="#524c4c")
    overload = Label(bframe, image=b4, bg="#524c4c")

    #vegetable label
    small_label = Label(bframe, text="Tiny Burder", font='Times 15 bold', bg="#524c4c")
    chessy_label = Label(bframe, text="Chessy Burger", font='Times 15 bold', bg="#524c4c")
    medium_label = Label(bframe, text="Satong Burger", font='Times 15 bold', bg="#524c4c")
    overload_label = Label(bframe, text="Overload Burger", font='Times 15 bold', bg="#524c4c")

    #vegetable price
    small_price = Label(bframe, text="15", font='Times 15 bold', bg="#524c4c")
    chessy_price = Label(bframe, text="25", font='Times 15 bold', bg="#524c4c")
    medium_price = Label(bframe, text="60", font='Times 15 bold', bg="#524c4c")
    overload_price = Label(bframe, text="80", font='Times 15 bold', bg="#524c4c")

    #spinbox
    bspin_box1 = Spinbox(bframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    bspin_box2 = Spinbox(bframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    bspin_box3 = Spinbox(bframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    bspin_box4 = Spinbox(bframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")

    #button
    btn_main = Button(main_frame, command=page2, text="MENU", font='Times 15 bold', bg="#aec240")
    bbtn_compute = Button(main_frame, command=fastfood_func, text="Compute", font='Times 15 bold', bg="green")

    #labets set position
    b_title.place(x=60, y=50)
    small.place(x=40, y=25)
    chessy.place(x=40, y=125)
    medium.place(x=40, y=225)
    overload.place(x=40, y=325)

    small_label.place(x=200, y=50)
    chessy_label.place(x=200, y=150)
    medium_label.place(x=200, y=250)
    overload_label.place(x=200, y=350)

    small_price.place(x=550, y=50)
    chessy_price.place(x=550, y=150)
    medium_price.place(x=550, y=250)
    overload_price.place(x=550, y=350)


    btotal_label.place(x=675, y=540)

    #button set position
    btn_main.place(x=360, y=540)
    bbtn_compute.place(x=570, y=540)

    #spinbox set position
    bspin_box1.place(x=600, y=50)
    bspin_box2.place(x=600, y=150)
    bspin_box3.place(x=600, y=250)
    bspin_box4.place(x=600, y=350)

def vegetable(): # destroy all frame on main frame
    for frame in main_frame.winfo_children():
        frame.destroy()

    #second page frame
    vframe = Frame(main_frame,  highlightbackground='black', highlightthickness=2, bg="#524c4c")
    vframe.pack(pady=70)
    vframe.pack_propagate(False)
    vframe.configure(width=730, height=500)

    #global var
    global v1
    global v2
    global v3
    global v4
    global vtotal_label
    global vspin_box1
    global vspin_box2
    global vspin_box3
    global vspin_box4

    #load image
    v_menu1= Image.open("resources/img/vegetable/ampalaya.png")
    v_menu2= Image.open("resources/img/vegetable/kalabasa.png")
    v_menu3= Image.open("resources/img/vegetable/sitaw.png")
    v_menu4= Image.open("resources/img/vegetable/talong.png")

    #Resize the Image using resize method
    resized_image1= v_menu1.resize((100,100), Image.ANTIALIAS)
    resized_image2= v_menu2.resize((100,100), Image.ANTIALIAS)
    resized_image3= v_menu3.resize((100,100), Image.ANTIALIAS)
    resized_image4= v_menu4.resize((100,100), Image.ANTIALIAS)
    v1 = ImageTk.PhotoImage(resized_image1)
    v2 = ImageTk.PhotoImage(resized_image2)
    v3 = ImageTk.PhotoImage(resized_image3)
    v4 = ImageTk.PhotoImage(resized_image4)

    #labels
    v_title = Label(main_frame, text="SELECT YOUR VEGETABLE ORDER", font='Helvetica 30 bold', fg="#aec240")
    vtotal_label = Label(main_frame, text="0", font='Times 20 bold', width=4, height=1, bg="#524c4c")

    #vegetable icon
    ampalaya = Label(vframe, image=v1, bg="#524c4c")
    kalabasa = Label(vframe, image=v2, bg="#524c4c")
    sitaw = Label(vframe, image=v3, bg="#524c4c")
    talong = Label(vframe, image=v4, bg="#524c4c")

    #vegetable label
    ampalaya_label = Label(vframe, text="Ampalaya", font='Times 15 bold', bg="#524c4c")
    kalabasa_label = Label(vframe, text="Kalabasa", font='Times 15 bold', bg="#524c4c")
    sitaw_label = Label(vframe, text="Sitaw", font='Times 15 bold', bg="#524c4c")
    talong_label = Label(vframe, text="Talong", font='Times 15 bold', bg="#524c4c")

    #vegetable price
    ampalaya_price = Label(vframe, text="15", font='Times 15 bold', bg="#524c4c")
    kalabasa_price = Label(vframe, text="34", font='Times 15 bold', bg="#524c4c")
    sitaw_price = Label(vframe, text="40", font='Times 15 bold', bg="#524c4c")
    talong_price = Label(vframe, text="10", font='Times 15 bold', bg="#524c4c")

    #spinbox
    vspin_box1 = Spinbox(vframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    vspin_box2 = Spinbox(vframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    vspin_box3 = Spinbox(vframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")
    vspin_box4 = Spinbox(vframe, from_=0, to=50, font='Times 15 bold', width=5, bg="#524c4c")

    #button
    btn_main = Button(main_frame, command=page2, text="MENU", font='Times 15 bold', bg="#aec240")
    vbtn_compute = Button(main_frame, command=vegetable_func, text="Compute", font='Times 15 bold', bg="green")

    #labets set position
    v_title.place(x=50, y=50)
    ampalaya.place(x=40, y=25)
    kalabasa.place(x=40, y=125)
    sitaw.place(x=40, y=225)
    talong.place(x=40, y=325)

    ampalaya_label.place(x=200, y=50)
    kalabasa_label.place(x=200, y=150)
    sitaw_label.place(x=200, y=250)
    talong_label.place(x=200, y=350)

    ampalaya_price.place(x=550, y=50)
    kalabasa_price.place(x=550, y=150)
    sitaw_price.place(x=550, y=250)
    talong_price.place(x=550, y=350)

    vtotal_label.place(x=675, y=540)

    #button set position
    btn_main.place(x=360, y=540)
    vbtn_compute.place(x=570, y=540)

    #spinbox set position
    vspin_box1.place(x=600, y=50)
    vspin_box2.place(x=600, y=150)
    vspin_box3.place(x=600, y=250)
    vspin_box4.place(x=600, y=350)




#second frame
def page2(): # destroy all frame on main frame
    for frame in main_frame.winfo_children():
        frame.destroy()

    #global var
    global rez_std1
    global rez_std2
    global rez_std3

    #second page frame
    frame2 = Frame(main_frame,  highlightbackground='black', highlightthickness=2, bg="#524c4c")
    frame2.pack(pady=70)
    frame2.pack_propagate(False)
    frame2.configure(width=730, height=500)

    #load image
    stand1= Image.open("resources/img/food_stands1.png")
    stand2= Image.open("resources/img/food_stands2.png")
    stand3= Image.open("resources/img/food_stands3.png")

    #Resize the Image using resize method
    resized_image1= stand1.resize((200,310), Image.ANTIALIAS)
    resized_image2= stand2.resize((200,310), Image.ANTIALIAS)
    resized_image3= stand3.resize((200,310), Image.ANTIALIAS)
    rez_std1 = ImageTk.PhotoImage(resized_image1)
    rez_std2 = ImageTk.PhotoImage(resized_image2)
    rez_std3 = ImageTk.PhotoImage(resized_image3)
    
    #labels
    p2_title = Label(main_frame, text="SELECT FOOD STANDS", font='Helvetica 30 bold', fg="#aec240")
    p2_std1 = Label(frame2, text="vegetable", font='Times 15 bold', fg="green", bg="#524c4c")
    p2_std2 = Label(frame2, text="Burger", font='Times 15 bold', fg="orange", bg="#524c4c")
    p2_std3 = Label(frame2, text="Coffe", font='Times 15 bold', fg="yellow", bg="#524c4c")


    #img button
    btn_std1 = Button(frame2, command=vegetable, image=rez_std1, bg="green")
    btn_std2 = Button(frame2, command=burger, image=rez_std2, bg="orange")
    btn_std3 = Button(frame2, command=coffee, image=rez_std3, bg="yellow")

    #button
    btn_main = Button(main_frame, command=quit, text="EXIT", font='Times 15 bold', bg="red")

    #labets set position
    p2_title.place(x=165, y=50)
    p2_std1.place(x=65, y=380)
    p2_std2.place(x=320, y=380)
    p2_std3.place(x=580, y=380)

    #img button set position
    btn_std1.place(x=10, y=50)
    btn_std2.place(x=250, y=50)
    btn_std3.place(x=500, y=50)

    #button set position
    btn_main.place(x=360, y=540)





#main frame
main_frame = Frame(win,  highlightbackground='black', highlightthickness=2, bg="#6715bf")
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=800, height=600)

#load image
d1= Image.open("resources/img/home_d1.png")
d2= Image.open("resources/img/home_d2.png")
d3= Image.open("resources/img/home_d3.png")

#Resize the Image using resize method
resized_image1= d1.resize((200,310), Image.ANTIALIAS)
resized_image2= d2.resize((200,310), Image.ANTIALIAS)
resized_image3= d3.resize((200,200), Image.ANTIALIAS)
rez_d1 = ImageTk.PhotoImage(resized_image1)
rez_d2 = ImageTk.PhotoImage(resized_image2)
rez_d3 = ImageTk.PhotoImage(resized_image3)

#labels
h_title = Label(main_frame, text="Welcome to Eat Me Lecious\n Food Stands", font='Helvetica 30 bold', fg="#aec240", bg="#6715bf")
 
#img label
home_d1 = Label(main_frame, image=rez_d1, bg="#6715bf")
home_d2 = Label(main_frame, image=rez_d2, bg="#6715bf")
home_d3 = Label(main_frame, image=rez_d3, bg="#6715bf")

#button
h_menu_btn = Button(main_frame, command=page2, text="menu", font='Times 10 bold', bg="green", width=10, height=3 )

#labets set position
h_title.place(x=140, y=150)

#img label set position
home_d1.place(x=0, y=350)
home_d2.place(x=570, y=300)
home_d3.place(x=400, y=250)

#buttons set position
h_menu_btn.place(x=345, y=350)


win.mainloop()

