import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
from modules import data_table as table
from modules import sendto_window as swin
import os
import re

CSV_HEADER = "お客様氏名,郵便番号,住所,電話番号,送り先情報"
COLUMN_WIDTH_LIST = [115, 95, 300, 125]
OUT_CSV = "customer.csv"

class CustomerDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # TODO: change it later...!
        self.master.title('顧客管理テスト')

        # instance variables
        self.customers = []
        self.tree = None
        crnt_dir = os.path.abspath('./data/')
        self.csv = os.path.join(crnt_dir, OUT_CSV)

        # set view
        self.pack()
        self.__first_open()
        self.__read_csv()
        self.__set_frame()
        self.__set_treeview()
        self.__set_form_widgets()

    def __set_frame(self):
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
        self.list_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.list_frame.pack(fill=tk.BOTH)
        self.search_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.search_frame.pack(fill=tk.BOTH)
        self.tree_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.tree_frame.pack(fill=tk.BOTH)
        self.removebutton_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.removebutton_frame.pack(fill=tk.BOTH)
        self.button_frame = tk.Frame(self.reg_tab, pady=8)
        self.button_frame.pack(fill=tk.BOTH)

    def __set_form_widgets(self):
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
        #### search form ####
        self.searchLabel = ttk.Label(self.search_frame, text="氏名で検索", padding=(115, 10, 3, 10))
        self.searchLabel.pack(side="left")
        self.searchBox = tk.Entry(self.search_frame)
        self.searchBox.pack(side="left", padx=20)
        self.search = tk.Button(self.search_frame, text="検索", width=4, height=1, padx=14, pady=1)
        self.search.bind("<ButtonPress>", self.__search_by_name)
        self.search.pack(side="left")
        #### order details button ####
        self.sendto = tk.Button(self.button_frame, text="送り先情報を入力する", width=5, height=2, padx=44, pady=1)
        self.sendto.bind("<ButtonPress>", self.__search)
        self.sendto.pack()
        #### reg button ####
        self.register = tk.Button(self.button_frame, text="登録", width=5, height=2, padx=44, pady=1)
        self.register.bind("<ButtonPress>", self.__write_csv)
        self.register.pack()
        ### delete button ###
        self.remove = tk.Button(self.removebutton_frame, text="削除", width=5, height=2, padx=44, pady=1)
        self.remove.bind("<ButtonPress>", self.__remove_record)
        self.remove.pack()
        ### /sub widgets ###

    # maybe unnecessary func...
    def __set_list(self):
        pass
        #self.listbox = listbox.CustomerListBox(self, key={'frame': self.list_frame})
        #self.listbox.pack()

    def __set_treeview(self):
        self.tree = table.DataTable(self, key={ \
            'frame': self.tree_frame, \
            'size': 4, \
            'column_width': COLUMN_WIDTH_LIST, \
            'headings': ['お客様氏名', '郵便番号', '住所', '電話番号'], \
            'data': self.customers \
        })
        self.tree.pack()

    def __first_open(self):
        crnt_dir = os.path.abspath('./')
        path = os.path.join(crnt_dir, 'data')
        if not os.path.isdir(path):
            os.mkdir(path)

    def __read_csv(self):
        crnt_dir = os.path.abspath('./data/')
        csv = os.path.join(crnt_dir, OUT_CSV)
        if not os.path.exists(self.csv):
            self.__write_header()

        f = open(csv, 'r')
        # read header info
        f.readline()
        lines = f.readlines()
        for str in lines:
            # delete unknown last empty items...
            if str == '\n':
                continue
            self.customers.append(str.split(','))
        f.close()

    ##### events #####
    def __open_sendto_window(self, event):
        swin.SendToWindow(self)

    def __write_csv(self, event):
        #if ():
        #    mbox.showwarning('', '情報が不足しています。')
        #    return
        # write file
        str = "\n" + \
            self.namebox.get() + "," + \
            self.zipcode_box1.get() + "-" + self.zipcode_box2.get() + "," + \
            self.addressbox.get() + "　" + self.addressbox2.get() + "," + \
            self.telbox.get()
        f = open(self.csv, 'a')
        f.write(str)
        f.close()

        # append to list
        record = re.sub('\n|\r\n|\r', '', str).split(',')
        self.customers.append(record)
        self.tree.insert("", "end", values=(record))
        # delete all input
        self.namebox.delete(0, tk.END)
        self.zipcode_box1.delete(0, tk.END)
        self.zipcode_box2.delete(0, tk.END)
        self.addressbox.delete(0, tk.END)
        self.addressbox2.delete(0, tk.END)
        self.telbox.delete(0, tk.END)

    def __write_header(self):
        f = open(self.csv, 'w')
        f.write(CSV_HEADER)
        f.close()

    def __remove_record(self, event):
        if (self.tree is None or not self.tree.focus()):
            return
        # delete & rewrite self.customers
        delete_index = self.tree.index(self.tree.focus())
        del self.customers[delete_index]
        self.tree.delete(self.tree.focus())
        self.__write_header()
        f = open(self.csv, 'a')
        g = (d for d in self.customers)
        for line in g:
            str = ','.join(line)
            f.write('\n' + str)
        f.close()

    def __search_by_name(self, event):
        ""
