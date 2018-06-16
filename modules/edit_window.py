import tkinter as tk
from tkinter import ttk
import os

class EditWindow(tk.Frame):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.record = key.get('key').get('record')
        self.data = key.get('key').get('data')
        self.index = key.get('key').get('index')

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
        win.reg_frame8 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame8.pack(fill=tk.BOTH)
        win.reg_frame9 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame9.pack(fill=tk.BOTH)
        #### name ####
        win.nameboxlabel = ttk.Label(win.reg_frame2, text="氏名", padding=(138, 10, 3, 10))
        win.nameboxlabel.pack(side="left")
        win.namebox = tk.Entry(win.reg_frame2)
        win.namebox.pack(side="left")
        win.namebox.insert(0, self.record[0])
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
        win.telbox.insert(0, self.record[3])
        #### ok & close button ####
        win.ok = tk.Button(win.reg_frame9, text="更新する", width=5, height=2, padx=44, pady=1)
        win.ok.bind("<ButtonPress>", self.__update_datatable)
        win.ok.pack()
        #### cancel & close button ####
        win.cancel = tk.Button(win.reg_frame9, text="キャンセル", width=5, height=2, padx=44, pady=1)
        win.cancel.bind("<ButtonPress>", self.__close_window)
        win.cancel.pack()
        self.win = win

    def __update_datatable(self, event):
        idx_tmp = int(self.index[1:], 16)
        idx = self.__specify_idx(idx_tmp)
        name = self.win.namebox.get()
        zipcode = self.win.zipcode_box1.get() + '-' + self.win.zipcode_box2.get()
        address = self.win.addressbox.get() + '　' + self.win.addressbox2.get()
        tel = self.win.telbox.get()
        self.data[idx] = [name, zipcode, address, tel]

        # delete all data and set sorted data
        self.master.delete(*self.master.get_children())
        g = (d for d in self.data)
        for v in g:
            self.master.insert("","end",values=(v))
        self.destroy()

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
