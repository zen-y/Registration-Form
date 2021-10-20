from tkinter import *
from tkinter import messagebox as tkMessageBox

root = Tk()

root.geometry("500x500")
root.title('Registration form')

label_0 =Label(root,text="Registration form", width=20, font=("bold",20))
label_0.place(x=90,y=60)

label_1 =Label(root,text="Full Name", width=20, font=("bold",10))
label_1.place(x=80,y=130)

entry_2=Entry(root)
entry_2.place(x=240,y=130)

label_3 =Label(root,text="Email", width=20, font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

label_4 =Label(root,text="Gender", width=20, font=("bold",10))
label_4.place(x=70,y=230)

gender_var=IntVar()
gender_list = ["Male", "Female"]

Radiobutton(root, text=gender_list[0], padx= 5, variable= gender_var, value=0).place(x=235,y=230)
Radiobutton(root, text=gender_list[1], padx= 20, variable= gender_var, value=1).place(x=290,y=230)

label_5=Label(root,text="Country",width=20, font=("bold",10))
label_5.place(x=70,y=280)

list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

country_var=StringVar()

droplist=OptionMenu(root, country_var, *list_of_country)
droplist.config(width=20)

country_var.set('Select your Country')
droplist.place(x=240,y=280)

label_6=Label(root,text="Qualification", width=20, font=('bold',10))
label_6.place(x=75,y=330)

qualification_var=IntVar()
Checkbutton(root,text="Graduate", variable=qualification_var).place(x=230,y=330)

def process():
    f = open("user-registration-details.txt", "a")

    name = entry_2.get()
    email = entry_3.get()
    gender = gender_list[gender_var.get()]
    country = country_var.get()
    qualification = qualification_var.get()

    content_to_save = "{},{},{},{},{}\n".format(name, email, gender, country, qualification)
    f.write(content_to_save)    
    f.close()

    print("Record saved")

    tkMessageBox.showinfo("Response Box", "Details Saved Successfully")


Button(root, text='Submit', width=20, bg="black", fg='white', command=process).place(x=180,y=380)

root.mainloop()

