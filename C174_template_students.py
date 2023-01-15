from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random

root = Tk()
root.title("Connecting Jobs - 2")
root.geometry("1000x500")
root.configure(background = "#0047ab")

#-----Logo_Img-----#
img = ImageTk.PhotoImage(Image.open("image5.png"))
logo_img = Label(root)
logo_img["image"] = img
logo_img.place(relx = 0.7, rely = 0.5, anchor = CENTER)

#-----Dr_Lbl-----#
lbl_dr = Label(root, text = "Doctor : ", font = ("Brush Script MT", 15, "bold"), bg = "#0047ab", fg = "white")
lbl_dr.place(relx = 0.1, rely = 0.3, anchor = CENTER)

#-----IT_Lbl-----#
lbl_it = Label(root, text = "IT Professtional : ", font = ("Brush Script MT", 15, "bold"), bg = "#0047ab", fg = "white")
lbl_it.place(relx = 0.1, rely = 0.6, anchor = CENTER)

#-----Chemical_Lbl-----#
lbl_chemical = Label(root, text = "Chemical Engineer : ", font = ("Brush Script MT", 15, "bold"), bg = "#0047ab", fg = "white")
lbl_chemical.place(relx = 0.1, rely = 0.9, anchor = CENTER)

#-----Dr_IB-----#
ib_dr = Entry(root)
ib_dr.place(relx = 0.1, rely = 0.1, anchor = CENTER)

#-----IT_IB-----#
ib_it = Entry(root)
ib_it.place(relx = 0.1, rely = 0.4, anchor = CENTER)

#-----Chemical_IB-----#
ib_chemical = Entry(root)
ib_chemical.place(relx = 0.1, rely = 0.7, anchor = CENTER)

#-----Selected_Dr_Lbl-----#
lbl_selected_dr = Label(root, font = ("times", 12, "bold"), bg = "#0047ab", fg = "white")
lbl_selected_dr.place(relx = 0.3, rely = 0.3, anchor = CENTER)

#-----Selected_IT_Lbl-----#
lbl_selected_it = Label(root, font = ("times", 12, "bold"), bg = "#0047ab", fg = "white")
lbl_selected_it.place(relx = 0.3, rely = 0.6, anchor = CENTER)

#-----Selected_Chemical_Lbl-----#
lbl_selected_chemical = Label(root, font = ("times", 12, "bold"), bg = "#0047ab", fg = "white")
lbl_selected_chemical.place(relx = 0.3, rely = 0.9, anchor = CENTER)

class Parent():
    
    def Dr(dr_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0, 3)
        lbl_selected_dr["text"] = dr_name + " has been alloted to " + hospital_list[random_hospital] + "."
            
    def Software_Engineer(it_name):
        it_company_list = ["I Code", "Web Access", "Dotcom Services", "ATOS"]
        random_it_company = random.randint(0, 3)
        lbl_selected_it["text"] = it_name + " has been alloted to " + it_company_list[random_it_company] + "."
        
    def Chemical_Engineer(chemical_name):
        company_list = ["Amul", "Cadbury", "Flipkart"]
        random_company = random.randint(0, 2)
        lbl_selected_chemical["text"] = chemical_name + " has been alloted to " + company_list[random_company] + "."
            
class Child1(Parent):
    
    def __init__(self):
        print("This is Child Class.")
        
    def get_dr(self):
        name = ib_dr.get()
        Parent.Dr(name)
        
class Child2(Parent):
    
    def __init__(self):
        print("This is Child Class.")
        
    def get_it(self):
        name = ib_it.get()
        Parent.Software_Engineer(name)
        
class Child3(Parent):
    
    def __init__(self):
        print("This is Child Class.")
        
    def get_chemical(self):
        name = ib_chemical.get()
        Parent.Chemical_Engineer(name)
        
child1_obj = Child1()
child2_obj = Child2()
child3_obj = Child3()

btn_dr = Button(root, text = "Show the Hospital Alloted", command = child1_obj.get_dr, bg = "#0047ab", relief = FLAT, fg = "white")
btn_dr.place(relx = 0.1, rely = 0.2, anchor = CENTER)

btn_it = Button(root, text = "Show the IT Company Alloted", command = child2_obj.get_it, bg = "#0047ab", relief = FLAT, fg = "white")
btn_it.place(relx = 0.1, rely = 0.5, anchor = CENTER)

btn_chemical = Button(root, text = "Show the Chemical Company Alloted", command = child3_obj.get_chemical, bg = "#0047ab", relief = FLAT, fg = "white")
btn_chemical.place(relx = 0.1, rely = 0.8, anchor = CENTER)

root.mainloop()