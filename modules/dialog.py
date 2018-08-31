import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
from modules import data_table as table
from modules import sendto_window as swin
from modules import customer_csv as csvlib
import re

CSV_HEADER = "お客様氏名,郵便番号,住所,電話番号,送り先情報"
SENDTO_HEADER = "送り先氏名,郵便番号,送り先住所,送り先電話番号,日付,内容"
COLUMN_WIDTH_LIST = [137, 76, 280, 125, 100]
SENDTO_COLUMN_WIDTH_LIST = [137, 76, 280, 95, 72, 130]
RECORD_TEL_INDEX = 3
OUT_CSV = "customer.csv" 

class CustomerDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # TODO: change it later...!
        self.master.title('顧客管理テスト')

        # instance variables
        self.customers = []
        self.searched_customers = []
        self.search_check = None
        self.chkval = None
        self.tree = None
        self.sendto_tree = None
        self.customer_csv = csvlib.CustomerCSV(self, key={
            'filename': OUT_CSV,
            'header': CSV_HEADER
        })
        self.swin_for_registration = None

        # set view
        self.pack()
        self.customer_csv.first_open() # execute if directory dont exists
        self.customers, self.searched_customers = self.customer_csv.read_csv()
        self.__set_frame()
        self.__set_treeview()
        self.__set_form_widgets()

    def __set_frame(self):
        # tabs
        self.notebook = ttk.Notebook(width=940, height=520)
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
        self.reg_frame6 = tk.Frame(self.reg_tab, padx=10, pady=10)
        self.reg_frame6.pack(fill=tk.BOTH)
        self.list_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.list_frame.pack(fill=tk.BOTH)
        self.search_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.search_frame.pack(fill=tk.BOTH)
        self.tree_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.tree_frame.pack(fill=tk.BOTH)
        self.sendto_tree_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.sendto_tree_frame.pack(fill=tk.BOTH)
        self.addsendtobutton_frame = tk.Frame(self.lst_tab, padx=10, pady=10)
        self.addsendtobutton_frame.pack(fill=tk.BOTH)
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
        #### name kana ####
        self.namekanaboxlabel = ttk.Label(self.reg_frame2, text="お客様氏名(フリガナ)", padding=(133, 10, 3, 10))
        self.namekanaboxlabel.pack(side="left")
        self.namekanabox = tk.Entry(self.reg_frame2)
        self.namekanabox.pack(side="left")
        #### zip code ####
        self.zipcode_label = ttk.Label(self.reg_frame3, text="郵便番号", padding=(185, 10, 3, 10))
        self.zipcode_label.pack(side="left")
        self.zipcode_box1 = tk.Entry(self.reg_frame3, width=7)
        self.zipcode_box1.pack(side="left")
        self.hyphen_label = ttk.Label(self.reg_frame3, text="-", padding=(1, 10, 3, 10))
        self.hyphen_label.pack(side="left")
        self.zipcode_box2 = tk.Entry(self.reg_frame3, width=12)
        self.zipcode_box2.pack(side="left")
        #### address ####
        self.addressboxlabel = ttk.Label(self.reg_frame4, text="住所", padding=(209, 10, 3, 10))
        self.addressboxlabel.pack(side="left")
        self.addressbox = tk.Entry(self.reg_frame4, width=65)
        self.addressbox.pack(side="left")
        self.addressboxlabel2 = ttk.Label(self.reg_frame5, text="番地・号・建物名・部屋番号", padding=(96, 10, 3, 10))
        self.addressboxlabel2.pack(side="left")
        self.addressbox2 = tk.Entry(self.reg_frame5, width=65)
        self.addressbox2.pack(side="left")
        #### tel ####
        self.telboxLabel = ttk.Label(self.reg_frame6, text="電話番号", padding=(185, 10, 3, 10))
        self.telboxLabel.pack(side="left")
        self.telbox = tk.Entry(self.reg_frame6)
        self.telbox.pack(side="left")
        #### search form ####
        self.searchLabel = ttk.Label(self.search_frame, text="氏名で検索", padding=(115, 10, 3, 10))
        self.searchLabel.pack(side="left")
        self.searchBox = tk.Entry(self.search_frame)
        self.searchBox.pack(side="left", padx=20)
        self.chkval = tk.BooleanVar()
        self.chkval.set(False)
        self.search_check = ttk.Checkbutton(self.search_frame, text="検索", padding=(0, 10, 10, 1), command=self.__search_by_name, variable=self.chkval)
        self.search_check.pack(side='left')
        #### order details button ####
        self.sendto = tk.Button(self.button_frame, text="送り先情報を入力する", width=5, height=2, padx=44, pady=1)
        self.sendto.bind("<ButtonPress>", self.__open_sendto_window)
        self.sendto.pack()
        #### reg button ####
        self.register = tk.Button(self.button_frame, text="登録", width=5, height=2, padx=44, pady=1)
        self.register.bind("<ButtonPress>", self.__write_csv)
        self.register.pack()
        ### add sendto button ###
        self.addsendto = tk.Button(self.addsendtobutton_frame, text="送り先を追加する", width=5, height=2, padx=44, pady=1)
        self.addsendto.bind("<ButtonPress>", self.__add_sendto)
        self.addsendto.pack()
        ### delete button ###
        self.remove = tk.Button(self.removebutton_frame, text="削除", width=5, height=2, padx=44, pady=1)
        self.remove.bind("<ButtonPress>", self.__remove_record)
        self.remove.pack()
        ### delete sendto button ###
        self.remove_sendto = tk.Button(self.removebutton_frame, text="送り先を削除", width=5, height=2, padx=44, pady=1)
        self.remove_sendto.bind("<ButtonPress>", self.__remove_sendto_record)
        self.remove_sendto.pack()
        ### /sub widgets ###

    # maybe unnecessary func...
    def __set_list(self):
        pass
        #self.listbox = listbox.CustomerListBox(self, key={'frame': self.list_frame})
        #self.listbox.pack()

    def __set_treeview(self):
        self.sendto_tree = table.DataTable(self, key={ \
            'frame': self.sendto_tree_frame, \
            'size': len(SENDTO_HEADER.split(',')), \
            'height': 2, \
            'column_width': SENDTO_COLUMN_WIDTH_LIST, \
            'search_on': False, \
            'headings': SENDTO_HEADER.split(','), \
            'data': self.customers, \
            'customer_csv': self.customer_csv, \
            'record_tel_index': RECORD_TEL_INDEX, \
        })
        self.tree = table.DataTable(self, key={ \
            'frame': self.tree_frame, \
            'size': len(CSV_HEADER.split(',')), \
            'height': 7, \
            'column_width': COLUMN_WIDTH_LIST, \
            'search_on': True, \
            'headings': CSV_HEADER.split(','), \
            'data': self.customers, \
            'searched_data': self.searched_customers, \
            'not_display_last_column': True, \
            'show_directly': True, \
            'sendto_length': len(CSV_HEADER.split(',')), \
            'sendto_tree': self.sendto_tree, \
            'customer_csv': self.customer_csv, \
        })
        self.tree.pack()
        self.sendto_tree.pack()
        self.sendto_tree.pass_tree(self.tree)

    def __validate_input(self):
        if self.namebox.get() == '' or \
            self.namekanabox.get() == '' or \
            self.zipcode_box1.get() == '' or \
            self.zipcode_box2.get() == '' or \
            self.addressbox.get() == '' or \
            self.addressbox2.get() == '' or \
            self.telbox.get() == '':
            return False
        return True

    ##### events #####
    def __open_sendto_window(self, event):
        data = {}
        if not self.swin_for_registration:
            self.swin_for_registration = \
                swin.SendToWindow(self, key={
                    'use_datatable': False, \
                })
            self.swin_for_registration.open(self.__base_input())
        else:
            data = self.swin_for_registration.sendto_window_input()
            self.swin_for_registration.open(self.__base_input(data=data))

    def __write_csv(self, event):
        if not self.__validate_input():
            mbox.showwarning('', '未入力の項目があります。')
            return

        # write file
        str = self.__make_str()
        self.customer_csv.write_record(str)

        # append to list
        record = re.sub('\n|\r\n|\r', '', str).split(',')
        self.customers.append(record)
        self.searched_customers.append(record)
        self.tree.insert("", "end", values=(record))
        self.tree.data = self.customers
        self.tree.searched_data = self.searched_customers
        # delete all input
        self.namebox.delete(0, tk.END)
        self.namekanabox.delete(0, tk.END)
        self.zipcode_box1.delete(0, tk.END)
        self.zipcode_box2.delete(0, tk.END)
        self.addressbox.delete(0, tk.END)
        self.addressbox2.delete(0, tk.END)
        self.telbox.delete(0, tk.END)

    def __base_input(self, empty=False, data={}):
        if empty or len(data) == 0:
            return {
                'name': '', \
                'name_kana': '', \
                'zipcode1': '', \
                'zipcode2': '', \
                'address1': '', \
                'address2': '', \
                'tel': '', \
                'date': '', \
                'order': '', \
            }
        else:
            return {
                'name': data['name'], \
                'name_kana': data['name_kana'], \
                'zipcode1': data['zipcode1'], \
                'zipcode2': data['zipcode2'], \
                'address1': data['address1'], \
                'address2': data['address2'], \
                'tel': data['tel'], \
                'date': data['date'], \
                'order': data['order'], \
            }

    def __make_str(self):
        if self.swin_for_registration is None:
            return ''
        sendto_input = self.swin_for_registration.sendto_window_input()
        str = "\n" + \
            self.namebox.get() + '（' + self.namekanabox.get() + "）," + \
            self.zipcode_box1.get() + "-" + self.zipcode_box2.get() + "," + \
            self.addressbox.get() + "　" + self.addressbox2.get() + "," + \
            self.telbox.get()
        if sendto_input['name'] != '' and sendto_input['name_kana'] != '' and \
            sendto_input['zipcode1'] != '' and sendto_input['zipcode2'] != '' and \
            sendto_input['address1'] != '' and sendto_input['address2'] != '' and \
            sendto_input['tel'] != '' and \
            sendto_input['date'] != '':
            str += "," + \
                sendto_input['name'] + '（' + sendto_input['name_kana'] + '）' + "/" + \
                sendto_input['zipcode1'] + "-" + sendto_input['zipcode2'] + "/" + \
                sendto_input['address1'] + "　" + sendto_input['address2'] + "/" + \
                sendto_input['tel'] + "/" + \
                sendto_input['date'] + "/" + \
                sendto_input['order']
        return str

    def __add_sendto(self, event):
        swin_for_add = swin.SendToWindow(self, key={
            'customer_csv': self.customer_csv, \
            'data': self.customers, \
            'use_datatable': True, \
            'datatable': self.sendto_tree, \
            'record_tel_index': RECORD_TEL_INDEX, \
            'sendto_record_size': len(SENDTO_HEADER.split(',')), \
            'add_to_csv': True, \
            'main_tree': self.tree, \
        })
        swin_for_add.open(self.__base_input(empty=True))

    def __remove_record(self, event):
        if (self.tree is None or not self.tree.focus()):
            return
        if not mbox.askokcancel('askokcancel', '選択中のデータを削除しますがよろしいですか？'):
            return
        # delete & rewrite self.customers
        delete_index = self.tree.index(self.tree.focus())
        del self.customers[delete_index]
        del self.searched_customers[delete_index]
        self.tree.data = self.customers
        self.tree.searched_data = self.searched_customers
        self.tree.delete(self.tree.focus())
        self.customer_csv.write_header()
        self.customer_csv.write_all_data(self.customers)

    def __remove_sendto_record(self, event):
        if (self.tree is None or not self.tree.focus()):
            return
        if (self.sendto_tree is None or not self.sendto_tree.focus()):
            return

        tree_index = self.tree.index(self.tree.focus())
        target_record = self.customers[tree_index]
        if len(target_record) < len(CSV_HEADER.split(',')):
            return
        if not mbox.askokcancel('askokcancel', '選択中の送付先を削除しますがよろしいですか？'):
            return
        selected_sendto_record = self.sendto_tree.item(self.sendto_tree.focus())['values']
        selected_sendto_record = list(map(str, selected_sendto_record))
        # fix tel if there isnt '0' in the head.
        tel = selected_sendto_record[RECORD_TEL_INDEX]
        if str(tel) != '' and str(tel)[0] != '0':
            tel = '0' + str(tel)
            selected_sendto_record[RECORD_TEL_INDEX] = tel
        selected_sendto_record = '/'.join(selected_sendto_record)
        # delete & rewrite self.customers
        sendto_records_str = target_record.pop()
        sendto_records = sendto_records_str.split('|')
        result = ','.join(target_record)
        g = (d for d in sendto_records)
        for sendto_line in g:
            if (selected_sendto_record != sendto_line):
                result += sendto_line + '|'
        if result[-1:] == '|':
            result = result[:-1]
        self.customers[tree_index] = result.split(',')
        # update tree & sendto_tree
        self.tree.delete(*self.tree.get_children())
        for record in self.customers:
            self.tree.insert("","end",values=(record))
        self.sendto_tree.delete(self.sendto_tree.focus())
        # update csv
        self.customer_csv.write_header()
        self.customer_csv.write_all_data(self.customers)

    def __search_by_name(self):
        search_word = self.searchBox.get()
        if not search_word:
            return
        self.tree.delete(*self.tree.get_children())
        g = (d for d in self.customers)
        if self.chkval.get() is True:
            self.searched_customers = []
            for record in self.customers:
                result = re.search(search_word, record[0])
                if result is not None:
                    self.searched_customers.append(record)
                    self.tree.insert("", "end", values=(record))
            self.tree.searched_data = self.searched_customers
        else:
            self.searched_customers = []
            for record in self.customers:
                self.searched_customers.append(record)
                self.tree.insert("", "end", values=(record))
            self.tree.searched_data = self.searched_customers
