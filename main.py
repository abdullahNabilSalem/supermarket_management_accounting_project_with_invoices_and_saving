from tkinter import *
import math # عمليات رياضية
import os # للتعامل مع ملفات النظام   
import random
from tkinter import messagebox

class Super :
    def __init__(self,root):
        self.root = root
        self.root.title("Super Market - سوبر ماركت")
        self.root.geometry("1300x750+100+15") # 1920x1080 
        self.root.iconbitmap('C:\\Desktop\\project_python\\supermarket_management_accounting_project_with_invoices_and_saving\\image\\icon2.ico')
        self.root.resizable(False,False)
        # self.root.configure(background='')
        title = Label(self.root,text="Super Market - سوبر ماركت",font=("times new roman",18,"bold"),bg="#6c757d",fg="#fff",bd=10)
        title.pack(side=TOP,fill=X)

        # متغيرات الحساب الكلي
        self.total_product_account = StringVar() # إجمالي حساب المنتج
        self.homemade_supplies = StringVar() # اللوزام المنزلية
        self.electrical_tools = StringVar() # أدوات الكهرباء

        self.fatora = StringVar()
        self.his_name = StringVar()
        self.his_phone = StringVar()    

        # متغيرات المنتجات الاساسية p1-p16
        self.p1 = IntVar()
        self.p2 = IntVar()
        self.p3 = IntVar()
        self.p4 = IntVar()
        self.p5 = IntVar()
        self.p6 = IntVar()
        self.p7 = IntVar()
        self.p8 = IntVar()
        self.p9 = IntVar()
        self.p10 = IntVar()
        self.p11 = IntVar()
        self.p12 = IntVar()
        self.p13 = IntVar()
        self.p14 = IntVar()
        self.p15 = IntVar()
        self.p16 = IntVar()

        # متغيرات اللوزام المنزلية h1-h16
        self.h1 = IntVar()
        self.h2 = IntVar()
        self.h3 = IntVar()
        self.h4 = IntVar()
        self.h5 = IntVar()
        self.h6 = IntVar()
        self.h7 = IntVar()
        self.h8 = IntVar()
        self.h9 = IntVar()
        self.h10 = IntVar()
        self.h11 = IntVar()
        self.h12 = IntVar()
        self.h13 = IntVar()
        self.h14 = IntVar()
        self.h15 = IntVar()
        self.h16 = IntVar()

        # متغيرات أدوات الكهرباء e1-e14
        self.e1 = IntVar()
        self.e2 = IntVar()
        self.e3 = IntVar()
        self.e4 = IntVar()
        self.e5 = IntVar()
        self.e6 = IntVar()
        self.e7 = IntVar()
        self.e8 = IntVar()
        self.e9 = IntVar()
        self.e10 = IntVar()
        self.e11 = IntVar()
        self.e12 = IntVar()
        self.e13 = IntVar()
        self.e14 = IntVar()

        # متغيرات بيانات المشتري
        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = IntVar()

        x = random.randint(1000,9999)
        self.fatora.set(str(x))

        # ========== Customer Data ==========
        F1 = Frame(self.root,bd=8,bg="#adb5bd",width=338,height=190)
        F1.place(x=962,y=48)

        tit = Label(F1, text='بيانات المشتري', font=('tajawal',15,'bold'),bg="#adb5bd",fg="black")
        tit.place(x=90,y=2)

        his_name = Label(F1,text=":أسم المشتري",font=('tajawal',12,'bold'),bg="#adb5bd",fg="black")
        his_name.place(x=210,y=40)

        his_phone = Label(F1,text=":رقم المشتري",font=('tajawal',12,'bold'),bg="#adb5bd",fg="black")
        his_phone.place(x=215,y=75)

        his_num = Label(F1,text=":رقم الفاتورة",font=('tajawal',12,'bold'),bg="#adb5bd",fg="black")
        his_num.place(x=220,y=110)

        Ent_name = Entry(F1,justify='center',textvariable=self.namo)
        Ent_name.place(x=87,y=49)

        Ent_phone = Entry(F1,justify='center',textvariable=self.phono)
        Ent_phone.place(x=87,y=82)

        Ent_bill = Entry(F1,justify='center',textvariable=self.fatora)
        Ent_bill.place(x=88,y=116)

        btn_customer = Button(F1,text="بحث",font=('tajawal',10),width=10,height=4,bg='#fff')
        btn_customer.place(x=3,y=49)

        # ========== Fatora : bill ==========
        titdd = Label(F1,text="الفواتير",font=('tajawal',15,'bold'),bg="#adb5bd",fg="black")
        titdd.place(x=125,y=135)

        F3 = Frame(self.root,bd=8,bg="#fff",width=338,height=399)
        F3.place(x=962,y=240)

        # Scroll bar for F3 Frame
        scroll_y = Scrollbar(F3,orient=VERTICAL) 
        self.txtarea = Text(F3,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # price
        F4 = Frame(self.root,bd=8,bg="#adb5bd",width=657,height=112)
        F4.place(x=645,y=645)

        hesab = Button(F4,text="الحساب",font=('tajawal',10),width=13,height=1,bg='#fff')
        hesab.place(x=535,y=-2)

        fatora = Button(F4,text="تصدير الفاتورة",font=('tajawal',10),width=13,height=1,bg='#fff') 
        fatora.place(x=535,y=45)

        clear = Button(F4,text="افراغ الحقول",font=('tajawal',10),width=13,height=1,bg='#fff')
        clear.place(x=420,y=-2)
        
        exite = Button(F4,text="أغلاق البرنامج",font=('tajawal',10),width=13,height=1,bg='#fff',command=root.quit) 
        exite.place(x=420,y=45)

        lblo1 = Label(F4,text="حساب الكلي للمنتجات",font=('tajawal',10,'bold'),bg="#adb5bd",fg="black")
        lblo1.place(x=271,y=-2)

        lblo1 = Label(F4,text="حساب اللوازم المنزلية",font=('tajawal',10,'bold'),bg="#adb5bd",fg="black")
        lblo1.place(x=273,y=28)

        lblo1 = Label(F4,text="حساب ادوات الكهرباء",font=('tajawal',10,'bold'),bg="#adb5bd",fg="black")
        lblo1.place(x=275,y=58)

        ento1 = Entry(F4,justify='center',width=24,textvariable=self.total_product_account)
        ento1.place(x=120,y=2)

        ento2 = Entry(F4,justify='center',width=24,textvariable=self.homemade_supplies)
        ento2.place(x=120,y=30)

        ento3 = Entry(F4,justify='center',width=24,textvariable=self.electrical_tools)
        ento3.place(x=120,y=60)

        notes = Button(F4,text="ملاحظات",font=('tajawal',10),width=13,height=3,bg='#fff')
        notes.place(x=10,y=7)

        # ========== Products ==========
        F5 = Frame(self.root,bd=8,bg="#adb5bd",width=318,height=702)
        F5.place(x=0,y=48)

        t = Label(F5,text="المنتجات الاساسية",font=('tajawal',13,'bold'),bg="#adb5bd",fg='black')
        t.place(x=75,y=-3)

        bq1 = Label(F5,text="الرز",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq1.place(x=245,y=40)

        bq2 = Label(F5,text="الزيت",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq2.place(x=228,y=80)

        bq3 = Label(F5,text="الدقيق",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq3.place(x=215,y=120)

        bq4 = Label(F5,text="السكر",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq4.place(x=220,y=160)
        
        bq5 = Label(F5,text="كرتون طماطم",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq5.place(x=180,y=200)

        bq6 = Label(F5,text="فاصوليا",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq6.place(x=208,y=240)

        bq7 = Label(F5,text="عدس",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq7.place(x=225,y=275)

        bq8 = Label(F5,text="معكرونة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq8.place(x=205,y=310)

        bq9 = Label(F5,text="بازلا",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq9.place(x=240,y=350)

        bq10 = Label(F5,text="كرتون تونة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq10.place(x=190,y=390)

        bq11 = Label(F5,text="البيض",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq11.place(x=220,y=430)

        bq12 = Label(F5,text="الحليب الدانو",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq12.place(x=170,y=470)

        bq12 = Label(F5,text="الملح",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq12.place(x=228,y=505)

        bq13 = Label(F5,text="الحمص",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq13.place(x=210,y=545)

        bq13 = Label(F5,text="الشوفان",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq13.place(x=205,y=585)

        bq13 = Label(F5,text="الشعير",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq13.place(x=215,y=620)

        bqent = Entry(F5,justify='center',width=15,textvariable=self.p1)
        bqent.place(x=70,y=48)

        bqent1 = Entry(F5,justify='center',width=15,textvariable=self.p2)
        bqent1.place(x=70,y=85)

        bqent2 = Entry(F5,justify='center',width=15,textvariable=self.p3)
        bqent2.place(x=70,y=125)

        bqent3 = Entry(F5,justify='center',width=15,textvariable=self.p4)
        bqent3.place(x=70,y=165)

        bqent4 = Entry(F5,justify='center',width=15,textvariable=self.p5)
        bqent4.place(x=70,y=205)

        bqent5 = Entry(F5,justify='center',width=15,textvariable=self.p6)
        bqent5.place(x=70,y=245)

        bqent6 = Entry(F5,justify='center',width=15,textvariable=self.p7)
        bqent6.place(x=70,y=280)

        bqent7 = Entry(F5,justify='center',width=15,textvariable=self.p8)
        bqent7.place(x=70,y=315)

        bqent8 = Entry(F5,justify='center',width=15,textvariable=self.p9)
        bqent8.place(x=70,y=355)

        bqent9 = Entry(F5,justify='center',width=15,textvariable=self.p10)
        bqent9.place(x=70,y=395)

        bqent10 = Entry(F5,justify='center',width=15,textvariable=self.p11)
        bqent10.place(x=70,y=435)

        bqent11 = Entry(F5,justify='center',width=15,textvariable=self.p12)
        bqent11.place(x=70,y=475)

        bqent12 = Entry(F5,justify='center',width=15,textvariable=self.p13)
        bqent12.place(x=70,y=515)

        bqent13 = Entry(F5,justify='center',width=15,textvariable=self.p14)
        bqent13.place(x=70,y=555)

        bqent14 = Entry(F5,justify='center',width=15,textvariable=self.p15)
        bqent14.place(x=70,y=595)

        bqent15 = Entry(F5,justify='center',width=15,textvariable=self.p16)
        bqent15.place(x=70,y=630)

        # ========== اللوزام المنزلية ==========
        F6 = Frame(self.root,bd=2,bg="#adb5bd",width=322,height=705)
        F6.place(x=320,y=48)

        t = Label(F6,text="اللوزام المنزلية",font=('tajawal',13,'bold'),bg="#adb5bd",fg='black')
        t.place(x=100,y=2)

        bq14 = Label(F6,text="صحون",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq14.place(x=200,y=40)

        bq15 = Label(F6,text="كؤوس",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq15.place(x=200,y=80)

        bq16 = Label(F6,text="سكين",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq16.place(x=200,y=120)

        bq17 = Label(F6,text="شوكه",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq17.place(x=200,y=160)
        
        bq18 = Label(F6,text="لوح تقطيع",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq18.place(x=200,y=200)

        bq19 = Label(F6,text="ملاعق",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq19.place(x=208,y=240)

        bq20 = Label(F6,text="مقشرة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq20.place(x=200,y=275)

        bq21 = Label(F6,text="فتاحة العلب",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq21.place(x=190,y=310)

        bq22 = Label(F6,text="سلة قمامة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq22.place(x=190,y=350)

        bq23 = Label(F6,text="أكياس",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq23.place(x=190,y=390)

        bq24 = Label(F6,text="وعاء الخلط",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq24.place(x=190,y=430)

        bq25 = Label(F6,text="حفارة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq25.place(x=200,y=470)

        bq26 = Label(F6,text="صينية",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq26.place(x=200,y=505)

        bq27 = Label(F6,text="سلة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq27.place(x=200,y=545)

        bq28 = Label(F6,text="مكنسة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq28.place(x=200,y=585)

        bq29 = Label(F6,text="طنجرة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq29.place(x=200,y=620)

        bqent11 = Entry(F6,justify='center',width=15,textvariable=self.h1)
        bqent11.place(x=70,y=48)

        bqent12 = Entry(F6,justify='center',width=15,textvariable=self.h2)
        bqent12.place(x=70,y=85)

        bqent22 = Entry(F6,justify='center',width=15,textvariable=self.h3)
        bqent22.place(x=70,y=125)

        bqent33 = Entry(F6,justify='center',width=15,textvariable=self.h4)
        bqent33.place(x=70,y=165)

        bqent44 = Entry(F6,justify='center',width=15,textvariable=self.h5)
        bqent44.place(x=70,y=205)

        bqent55 = Entry(F6,justify='center',width=15,textvariable=self.h6)
        bqent55.place(x=70,y=245)

        bqent66 = Entry(F6,justify='center',width=15,textvariable=self.h7)
        bqent66.place(x=70,y=280)

        bqent77 = Entry(F6,justify='center',width=15,textvariable=self.h8)
        bqent77.place(x=70,y=315)

        bqent88 = Entry(F6,justify='center',width=15,textvariable=self.h9)
        bqent88.place(x=70,y=355)

        bqent99 = Entry(F6,justify='center',width=15,textvariable=self.h10)
        bqent99.place(x=70,y=395)

        bqent100 = Entry(F6,justify='center',width=15,textvariable=self.h11)
        bqent100.place(x=70,y=435)

        bqent111 = Entry(F6,justify='center',width=15,textvariable=self.h12)
        bqent111.place(x=70,y=475)

        bqent122 = Entry(F6,justify='center',width=15,textvariable=self.h13)
        bqent122.place(x=70,y=515)

        bqent133 = Entry(F6,justify='center',width=15,textvariable=self.h14)
        bqent133.place(x=70,y=555)

        bqent144 = Entry(F6,justify='center',width=15,textvariable=self.h15)
        bqent144.place(x=70,y=595)

        bqent155 = Entry(F6,justify='center',width=15,textvariable=self.h16)
        bqent155.place(x=70,y=630)

        F7 = Frame(self.root,bd=2,bg="#adb5bd",width=315,height=594)
        F7.place(x=644,y=48)

        t4 = Label(F7,text="ادوات الكهرباء",font=('tajawal',13,'bold'),bg="#adb5bd",fg='black')
        t4.place(x=100,y=2)

        bq26 = Label(F7,text="مكنسة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq26.place(x=200,y=40)

        bq27 = Label(F7,text="تلفزيون",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq27.place(x=200,y=80)

        bq28 = Label(F7,text="غسالة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq28.place(x=207,y=120)

        bq29 = Label(F7,text="مكرويف",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq29.place(x=198,y=160)
        
        bq30 = Label(F7,text="خلاط",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq30.place(x=200,y=200)

        bq31 = Label(F7,text="فرن غاز",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq31.place(x=200,y=240)

        bq32 = Label(F7,text="مقلاه كهرباء",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq32.place(x=170,y=275)

        bq33 = Label(F7,text="مروحة سقف",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq33.place(x=170,y=310)

        bq34 = Label(F7,text="مروحة أرضية",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq34.place(x=170,y=350)

        bq35 = Label(F7,text="تلفزيون 32",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq35.place(x=180,y=390)

        bq36 = Label(F7,text="تلفزيون 43",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq36.place(x=180,y=430)

        bq37 = Label(F7,text="فلتر ماء",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq37.place(x=200,y=470)

        bq37 = Label(F7,text="مكواة",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq37.place(x=200,y=505)

        bq37 = Label(F7,text="كبت",font=('tajawal',15),bg="#adb5bd",fg='black')
        bq37.place(x=200,y=545)

        bqent11 = Entry(F7,justify='center',width=15,textvariable=self.e1)
        bqent11.place(x=70,y=48)

        bqent12 = Entry(F7,justify='center',width=15,textvariable=self.e2)
        bqent12.place(x=70,y=85)

        bqent22 = Entry(F7,justify='center',width=15,textvariable=self.e3)
        bqent22.place(x=70,y=125)

        bqent33 = Entry(F7,justify='center',width=15,textvariable=self.e4)
        bqent33.place(x=70,y=165)

        bqent44 = Entry(F7,justify='center',width=15,textvariable=self.e5)
        bqent44.place(x=70,y=205)

        bqent55 = Entry(F7,justify='center',width=15,textvariable=self.e6)
        bqent55.place(x=70,y=245)

        bqent66 = Entry(F7,justify='center',width=15,textvariable=self.e7)
        bqent66.place(x=70,y=280)

        bqent77 = Entry(F7,justify='center',width=15,textvariable=self.e8)
        bqent77.place(x=70,y=315)

        bqent88 = Entry(F7,justify='center',width=15,textvariable=self.e9)
        bqent88.place(x=70,y=355)

        bqent99 = Entry(F7,justify='center',width=15,textvariable=self.e10)
        bqent99.place(x=70,y=395)

        bqent776 = Entry(F7,justify='center',width=15,textvariable=self.e11)
        bqent776.place(x=70,y=435)

        bqent885 = Entry(F7,justify='center',width=15,textvariable=self.e12)
        bqent885.place(x=70,y=475)

        bqent996 = Entry(F7,justify='center',width=15,textvariable=self.e13)
        bqent996.place(x=70,y=515)

        bqent9965 = Entry(F7,justify='center',width=15,textvariable=self.e14)
        bqent9965.place(x=70,y=555)
        self.welcome()
        
        # Function
    def welcome(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome to Super Market")
        self.txtarea.insert(END,"\n=============================================")
        self.txtarea.insert(END,f"\n\t B.NUM  : {self.fatora.get()}")
        self.txtarea.insert(END,f"\n\t NAME   : {self.his_name.get()}")
        self.txtarea.insert(END,f"\n\t PHONE  : {self.his_phone.get()}")
        self.txtarea.insert(END,"\n=============================================")
        self.txtarea.insert(END,f"\nالسعر\t         العدد\t      المشتريات")
        self.txtarea.insert(END,"\n=============================================")

        

root = Tk()
op = Super(root)
root.mainloop() 