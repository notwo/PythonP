import tkinter as tk
from tkinter import ttk
from modules import customer_listbox
from modules import sendto_window as swin
import os

OUT_CSV = "customer.csv"

class CustomerDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # TODO: change it later...!
        self.master.title('顧客管理テスト')

        # instance variables
        self.customers = []
        self.csv = ""

        # set view
        self.pack()
        self.__read_csv()
        self.__set_list()
        self.__set_form_widgets()

    def __set_form_widgets(self):
        # tabs
        self.notebook = ttk.Notebook(width=900, height=500)
        self.reg_tab = tk.Frame(self.notebook)
        self.lst_tab = tk.Frame(self.notebook)
        self.notebook.add(self.reg_tab, text="顧客情報登録", padding=2)
        self.notebook.add(self.lst_tab, text="顧客一覧", padding=2)
        self.notebook.pack()
        ### frame ###
        self.reg_frame = tk.Frame(self.reg_tab, padx=10, pady=10)
        self.reg_frame.pack(fill=tk.BOTH)
        self.reg_frame2 = tk.Frame(self.reg_tab, padx=10, pady=10)
        self.reg_frame2.pack(fill=tk.BOTH)
        self.reg_frame3 = tk.Frame(self.reg_tab, padx=10, pady=10)
        self.reg_frame3.pack(fill=tk.BOTH)
        self.reg_frame4 = tk.Frame(self.reg_tab, padx=10, pady=10)
        self.reg_frame4.pack(fill=tk.BOTH)
        self.reg_frame5 = tk.Frame(self.reg_tab, padx=10, pady=10)
        self.reg_frame5.pack(fill=tk.BOTH)
        self.list_frame = tk.Frame(self.reg_tab, padx=10)
        self.list_frame.pack(fill=tk.BOTH)
        #### name ####
        self.nameboxlabel = ttk.Label(self.reg_frame, text="お客様氏名", padding=(175, 10, 3, 10))
        self.nameboxlabel.pack(side="left")
        self.namebox = tk.Entry(self.reg_frame)
        self.namebox.pack(side="left")
        #### zip code ####
        self.zipcode_label = ttk.Label(self.reg_frame2, text="郵便番号", padding=(185, 10, 3, 10))
        self.zipcode_label.pack(side="left")
        self.zipcode_box1 = tk.Entry(self.reg_frame2, width=7)
        self.zipcode_box1.pack(side="left")
        self.hyphen_label = ttk.Label(self.reg_frame2, text="-", padding=(1, 10, 3, 10))
        self.hyphen_label.pack(side="left")
        self.zipcode_box2 = tk.Entry(self.reg_frame2, width=12)
        self.zipcode_box2.pack(side="left")
        #### address ####
        self.addressboxlabel = ttk.Label(self.reg_frame3, text="住所", padding=(209, 10, 3, 10))
        self.addressboxlabel.pack(side="left")
        self.addressbox = tk.Entry(self.reg_frame3, width=65)
        self.addressbox.pack(side="left")
        self.addressboxlabel2 = ttk.Label(self.reg_frame4, text="番地・号・建物名・部屋番号", padding=(96, 10, 3, 10))
        self.addressboxlabel2.pack(side="left")
        self.addressbox2 = tk.Entry(self.reg_frame4, width=65)
        self.addressbox2.pack(side="left")
        #### tel ####
        self.telboxLabel = ttk.Label(self.reg_frame5, text="電話番号", padding=(185, 10, 3, 10))
        self.telboxLabel.pack(side="left")
        self.telbox = tk.Entry(self.reg_frame5)
        self.telbox.pack(side="left")
        #### order details button ####
        self.button_frame = tk.Frame(self.reg_tab, pady=8)
        self.button_frame.pack(fill=tk.BOTH)
        self.sendto = tk.Button(self.button_frame, text="送り先情報を入力する", width=5, height=2, padx=44, pady=1)
        self.sendto.bind("<ButtonPress>", self.__open_sendto_window)
        self.sendto.pack()
        #### reg button ####
        self.register = tk.Button(self.button_frame, text="登録", width=5, height=2, padx=44, pady=1)
        self.register.bind("<ButtonPress>", self.reg_handler)
        self.register.pack()
        ### /sub widgets ###
        # for list tab

    def __read_csv(self):
        crnt_dir = os.path.dirname(os.path.abspath(__file__))
        target_file_path = "../"
        self.csv = os.path.join(crnt_dir, target_file_path)
        if not os.path.exists(self.csv + OUT_CSV):
            self.__write_header()

        f = open(self.csv + OUT_CSV, 'r')
        # read header info
        str = f.readline()
        while str:
            str = f.readline()
            self.customers.append(str)
        f.close()
    
    def __set_list(self):
        ""

    ##### events #####
    def __open_sendto_window(self, event):
        swin.SendToWindow(self)

    def reg_handler(self, event):
        ""

    def __write_header(self):
        f = open(self.csv + OUT_CSV, 'w')
        f.write("お客様氏名,郵便番号,住所,電話番号,送り先情報")
        f.close()
