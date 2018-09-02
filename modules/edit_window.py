import tkinter as tk
from tkinter import ttk
import os
import zenhan

class EditWindow(tk.Frame):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.record = key.get('key').get('record')
        self.data = key.get('key').get('data')
        self.index = key.get('key').get('record_index')
        self.customer_csv = key.get('key').get('customer_csv')
        self.datatable = key.get('key').get('datatable')
        self.sendto_record_size = key.get('key').get('sendto_record_size')

        win = tk.Toplevel(self)
        win.transient(self.master)
        win.geometry("640x640")
        win.title("顧客情報編集")
        win.grab_set()
        self.__set_form_widgets(win)

    def __set_form_widgets(self, win):
        #### frame ####
        win.reg_frame1 = tk.Frame(win, padx=10, pady=2)
        win.reg_frame1.pack(fill=tk.BOTH)
        win.reg_frame2 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame2.pack(fill=tk.BOTH)
        win.reg_frame3 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame3.pack(fill=tk.BOTH)
        win.reg_frame4 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame4.pack(fill=tk.BOTH)
        win.reg_frame5 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame5.pack(fill=tk.BOTH)
        win.reg_frame6 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame6.pack(fill=tk.BOTH)
        win.reg_frame7 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame7.pack(fill=tk.BOTH)
        #### name ####
        name = self.record[0].split('（')
        win.nameboxlabel = ttk.Label(win.reg_frame1, text="氏名", padding=(138, 10, 3, 10))
        win.nameboxlabel.pack(side="left")
        win.namebox = tk.Entry(win.reg_frame1)
        win.namebox.pack(side="left")
        win.namebox.insert(0, name[0])
        #### name kana ####
        win.namekanaboxlabel = ttk.Label(win.reg_frame2, text="氏名(フリガナ))", padding=(96, 10, 3, 10))
        win.namekanaboxlabel.pack(side="left")
        win.namekanabox = tk.Entry(win.reg_frame2)
        win.namekanabox.pack(side="left")
        win.namekanabox.insert(0, name[1].replace('）', ''))
        #### zip code ####
        zipcode = self.record[1].split('-')
        win.zipcode_label = ttk.Label(win.reg_frame3, text="郵便番号", padding=(113, 10, 3, 10))
        win.zipcode_label.pack(side="left")
        win.zipcode_box1 = tk.Entry(win.reg_frame3, width=7)
        win.zipcode_box1.pack(side="left")
        win.zipcode_box1.insert(0, zipcode[0])
        win.hyphen_label = ttk.Label(win.reg_frame3, text="-", padding=(1, 10, 3, 10))
        win.hyphen_label.pack(side="left")
        win.zipcode_box2 = tk.Entry(win.reg_frame3, width=12)
        win.zipcode_box2.pack(side="left")
        win.zipcode_box2.insert(0, zipcode[1])
        #### address ####
        address = self.record[2].split('　')
        win.addressboxlabel = ttk.Label(win.reg_frame4, text="住所", padding=(137, 10, 3, 10))
        win.addressboxlabel.pack(side="left")
        win.addressbox = tk.Entry(win.reg_frame4, width=65, textvariable='')
        win.addressbox.pack(side="left")
        win.addressbox.insert(0, address[0])
        win.addressboxlabel2 = ttk.Label(win.reg_frame5, text="番地・号・建物名・部屋番号", padding=(24, 10, 3, 10))
        win.addressboxlabel2.pack(side="left")
        win.addressbox2 = tk.Entry(win.reg_frame5, width=65)
        win.addressbox2.pack(side="left")
        win.addressbox2.insert(0, address[1])
        #### tel ####
        win.telboxLabel = ttk.Label(win.reg_frame6, text="電話番号", padding=(113, 10, 3, 10))
        win.telboxLabel.pack(side="left")
        win.telbox = tk.Entry(win.reg_frame6)
        win.telbox.pack(side="left")
        tel = self.record[3]
        if str(tel)[0] != '0':
            tel = '0' + str(tel)
        win.telbox.insert(0, tel)
        #### ok & close button ####
        win.ok = tk.Button(win.reg_frame7, text="更新する", width=5, height=2, padx=44, pady=1)
        win.ok.bind("<ButtonPress>", self.__setup_input)
        win.ok.pack()
        #### cancel & close button ####
        win.cancel = tk.Button(win.reg_frame7, text="キャンセル", width=5, height=2, padx=44, pady=1)
        win.cancel.bind("<ButtonPress>", self.__close_window)
        win.cancel.pack()
        self.win = win

    def __setup_input(self, event):
        self.__update_datatable()
        self.__update_csv()

    def __update_datatable(self):
        idx_tmp = int(self.index[1:], 16)
        idx = self.__specify_idx(idx_tmp)
        name = self.win.namebox.get() + '（' + zenhan.h2z(self.win.namekanabox.get()) + '）'
        zipcode = self.win.zipcode_box1.get() + '-' + self.win.zipcode_box2.get()
        address = self.win.addressbox.get() + '　' + self.win.addressbox2.get()
        tel = self.win.telbox.get()
        if len(self.data[idx]) >= self.sendto_record_size:
            sendto = self.data[idx][-1]
            self.data[idx] = [name, zipcode, address, tel, sendto]
        else:
            self.data[idx] = [name, zipcode, address, tel]

        # delete all data and set sorted data
        self.master.delete(*self.master.get_children())
        g = (d for d in self.data)
        for v in g:
            self.master.insert("","end",values=(v))
        self.destroy()

    def __update_csv(self):
        self.customer_csv.write_header()
        self.customer_csv.write_all_data(self.data)

    def __specify_idx(self, idx_tmp):
        if idx_tmp > len(self.data):
            if idx_tmp % len(self.data) == 0:
                idx = len(self.data) - 1
            else:
                idx = idx_tmp % len(self.data) - 1
        else:
            idx = idx_tmp - 1
        return idx

    def __close_window(self, event):
        self.destroy()
