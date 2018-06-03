import tkinter as tk
from tkinter import ttk
import os
class SendToWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        win = tk.Toplevel(self)
        win.transient(self.master)
        win.geometry("640x640")
        win.title("送り先情報入力")
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
        #### check same as address? ####
        self.chkval = tk.BooleanVar()
        self.chkval.set(False)
        win.chk_address = ttk.Checkbutton(win.reg_frame1, text="住所と同様", padding=(0, 10, 10, 1), command=self.__same_as_address1, variable=self.chkval)
        win.chk_address.pack(side='right')
        #### name ####
        win.nameboxlabel = ttk.Label(win.reg_frame2, text="送り先氏名", padding=(106, 10, 3, 10))
        win.nameboxlabel.pack(side="left")
        win.namebox = tk.Entry(win.reg_frame2)
        win.namebox.pack(side="left")
        #### zip code ####
        win.zipcode_label = ttk.Label(win.reg_frame3, text="送り先郵便番号", padding=(82, 10, 3, 10))
        win.zipcode_label.pack(side="left")
        win.zipcode_box1 = tk.Entry(win.reg_frame3, width=7)
        win.zipcode_box1.pack(side="left")
        win.hyphen_label = ttk.Label(win.reg_frame3, text="-", padding=(1, 10, 3, 10))
        win.hyphen_label.pack(side="left")
        win.zipcode_box2 = tk.Entry(win.reg_frame3, width=12)
        win.zipcode_box2.pack(side="left")
        #### address ####
        win.addressboxlabel = ttk.Label(win.reg_frame4, text="送り先住所", padding=(106, 10, 3, 10))
        win.addressboxlabel.pack(side="left")
        win.addressbox = tk.Entry(win.reg_frame4, width=65, textvariable='')
        win.addressbox.pack(side="left")
        win.addressboxlabel2 = ttk.Label(win.reg_frame5, text="番地・号・建物名・部屋番号", padding=(24, 10, 3, 10))
        win.addressboxlabel2.pack(side="left")
        win.addressbox2 = tk.Entry(win.reg_frame5, width=65)
        win.addressbox2.pack(side="left")
        #### tel ####
        win.telboxLabel = ttk.Label(win.reg_frame6, text="送り先電話番号", padding=(82, 10, 3, 10))
        win.telboxLabel.pack(side="left")
        win.telbox = tk.Entry(win.reg_frame6)
        win.telbox.pack(side="left")
        #### ok & close button ####
        win.ok = tk.Button(win.reg_frame7, text="OK", width=5, height=2, padx=44, pady=1)
        win.ok.bind("<ButtonPress>", self.__close_window)
        win.ok.pack()
        #### cancel & close button ####
        win.cancel = tk.Button(win.reg_frame7, text="Cancel", width=5, height=2, padx=44, pady=1)
        win.cancel.bind("<ButtonPress>", self.__close_window)
        win.cancel.pack()
        self.win = win

    def __same_as_address1(self):
        parent_name = self.win.namebox.get()
        parent_zipcode1 = self.win.zipcode_box1.get()
        parent_zipcode2 = self.win.zipcode_box2.get()
        parent_address = self.win.addressbox.get()
        parent_address2 = self.win.addressbox2.get()
        parent_tel = self.win.telbox.get()

        if self.chkval.get() == True:
            if not parent_name:
                self.win.namebox.insert(0, self.master.namebox.get())
            if not parent_zipcode1:
                self.win.zipcode_box1.insert(0, self.master.zipcode_box1.get())
            if not parent_zipcode2:
                self.win.zipcode_box2.insert(0, self.master.zipcode_box2.get())
            if not parent_address:
                self.win.addressbox.insert(0, self.master.addressbox.get())
            if not parent_address2:
                self.win.addressbox2.insert(0, self.master.addressbox2.get())
            if not parent_tel:
                self.win.telbox.insert(0, self.master.telbox.get())

    def __set_additional_form_widgets(self):
        ""
    def __setup_sendto(self, event):
        self.destroy()

    def __close_window(self, event):
        self.destroy()
