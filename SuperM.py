from tkinter import *
from tkinter import messagebox # أظهار الرسائل او الاشعارات
from PIL import Image, ImageTk
import webbrowser # من أجل التعامل مع المتصفح
import os # التعامل مع مسارات النظام
import sys 

pro = Tk()
pro.geometry('800x450+280+190')
pro.resizable(False,False)
pro.title('SUPER MARKET')
pro.iconbitmap('C:\\Desktop\\project_python\\supermarket_management_accounting_project_with_invoices_and_saving\\image\\icon2.ico')

title = Label(pro,text="Super Market System",fg="#0B2F3A",bg="#DBA901",font=("tajwal",16,"bold"))
title.pack(fill=X) 

F1 = Frame(pro,width=230,height=420,bg="#0B2F3A")
F1.place(x=570,y=30)

Title1 = Label(F1,text="مشروع: سوبر ماركت",bg="#0B2F3A",fg="#fff",font=('Traditional',15,'bold'))
Title1.place(x=45,y=10)

Title2 = Label(F1,text="المبرمج: عبدالله نبيل",bg="#0B2F3A",fg="#fff",font=('Cairo',15,'bold'))
Title2.place(x=55,y=50)

Title3 = Label(F1,text="وسائل الاتصال بنا",bg="#0B2F3A",fg="#fff",font=('Almarai',15,'bold'))
Title3.place(x=65,y=90)

# ----------------------------------------------------------

# Function Button
u1 = 'https://www.facebook.com'
u2 = 'https://web.telegram.org'
u3 = 'https://www.youtube.com'

def Open1():
    webbrowser.open_new(u1)

def Open2():
    webbrowser.open_new(u2)

def Open3():
    webbrowser.open_new(u3)

def about1():
    messagebox.showinfo('المطور','عبدالله نبيل')

def about2():
    messagebox.showinfo('المشروع','مشروع سوبر ماركت')

def log():
    user = En1.get()
    password = En2.get()
    if user == 'abood' and password == '123':
        messagebox.showinfo('تسجيل الدخول','تم تسجيل الدخول بنجاح')
    else :
        messagebox.showerror('تسجيل الدخول','اسم المستخدم أو كلمة المرور خاطئة')

# ----------------------------------------------------------

B1 = Button(F1,text="حسابنا على الفيس بوك",width=16,fg="black",bg="#DBA901",font=('Almarai',15,'bold'),command=Open1)
B1.place(x=14,y=130)

B2 = Button(F1,text="حسابنا على التليجرام",width=16,fg="black",bg="#DBA901",font=('Almarai',15,'bold'),command=Open2)
B2.place(x=14,y=177)

B3 = Button(F1,text="قناتنا على يوتيوب",width=16,fg="black",bg="#DBA901",font=('Almarai',15,'bold'),command=Open3)
B3.place(x=14,y=225)

B4 = Button(F1,text="لمحة عن المطور",width=16,fg="black",bg="#DBA901",font=('Almarai',15,'bold'),command=about1)
B4.place(x=14,y=272)

B5 = Button(F1,text="لمحة عن المشروع",width=16,fg="black",bg="#DBA901",font=('Almarai',15,'bold'),command=about2)
B5.place(x=14,y=318)

B6 = Button(F1,text="أغلاق البرنامج",width=16,fg="black",bg="#DBA901",font=('Almarai',15,'bold'),command=quit)
B6.place(x=14,y=365)

photo = PhotoImage(file="C:\\Desktop\\project_python\\supermarket_management_accounting_project_with_invoices_and_saving\\image\\super_market.png")
imo = Label(pro,image=photo)
imo.place(x=104,y=34,width=380,height=272)

F2 = Frame(pro,width=570,height=120,bg="#0B2F3A")
F2.place(x=0,y=330)

# تغيير حجم الصورة باستخدام PIL
original_image = Image.open('C:\\Desktop\\project_python\\supermarket_management_accounting_project_with_invoices_and_saving\\image\\man.png')
resized_image = original_image.resize((110, 110), Image.LANCZOS) # تغيير الحجم إلى 55x55
photo1 = ImageTk.PhotoImage(resized_image)

imo1 = Label(pro,image=photo1)
imo1.place(x=460,y=335,width=110,height=110)

L1 = Label(F2,text="أسم المستخدم",fg="gold",bg="#0B2F3A",font=('tajawal',15,'bold'))
L1.place(x=345,y=25)

L2 = Label(F2,text="كلمة المرور",fg="gold",bg="#0B2F3A",font=('tajawal',15,'bold'))
L2.place(x=345,y=70)

En1 = Entry(F2,font=('tajawal',15,'bold'),justify='center')
En1.place(x=115,y=25)

En2 = Entry(F2,font=('tajawal',15,'bold'),justify='center',show='*')
En2.place(x=115,y=70)

B = Button(F2,text="تسجيل الدخول",bg="#DBA901",fg="black",font=('tajawal',15,'bold'),bd=2,command=log)
B.place(x=9,y=25,width=100,height=74)

pro.mainloop()