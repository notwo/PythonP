import tkinter as tk
from tkinter import ttk

class SendToWindow(tk.Frame):
    def __init__(self, master=None, **key):
        #super().__init__(master)
        self.customer_csv = None
        self.add_to_csv = key.get('key').get('add_to_csv')
        self.use_datatable = key.get('key').get('use_datatable')
        if self.use_datatable or self.add_to_csv:
            self.customer_csv = key.get('key').get('customer_csv')
        if self.use_datatable:
            self.data = key.get('key').get('data')
            self.datatable = key.get('key').get('datatable')
            self.record_index = self.datatable.focus()
            self.record_tel_index = key.get('key').get('record_tel_index')
            self.sendto_record_size = key.get('key').get('sendto_record_size')
            self.main_tree = key.get('key').get('main_tree')

        # instance variables
        self.name = ''
        self.namekana = ''
        self.zipcode1 = ''
        self.zipcode2 = ''
        self.address1 = ''
        self.address2 = ''
        self.tel = ''
        self.date = ''
        self.order = ''

    def open(self, base_input):
        super().__init__(None)
        win = tk.Toplevel(self)
        win.transient(self.master)
        win.geometry("640x640")
        win.title("送り先情報入力")
        win.grab_set()
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
        win.reg_frame10 = tk.Frame(win, padx=10, pady=10)
        win.reg_frame10.pack(fill=tk.BOTH)
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
        win.namebox.insert(0, base_input['name'])
        #### name kana ####
        win.namekanaboxlabel = ttk.Label(win.reg_frame3, text="送り先氏名(フリガナ)", padding=(64, 10, 3, 10))
        win.namekanaboxlabel.pack(side="left")
        win.namekanabox = tk.Entry(win.reg_frame3)
        win.namekanabox.pack(side="left")
        win.namekanabox.insert(0, base_input['name_kana'])
        #### zip code ####
        win.zipcode_label = ttk.Label(win.reg_frame4, text="送り先郵便番号", padding=(82, 10, 3, 10))
        win.zipcode_label.pack(side="left")
        win.zipcode_box1 = tk.Entry(win.reg_frame4, width=7)
        win.zipcode_box1.pack(side="left")
        win.zipcode_box1.insert(0, base_input['zipcode1'])
        win.hyphen_label = ttk.Label(win.reg_frame4, text="-", padding=(1, 10, 3, 10))
        win.hyphen_label.pack(side="left")
        win.zipcode_box2 = tk.Entry(win.reg_frame4, width=12)
        win.zipcode_box2.pack(side="left")
        win.zipcode_box2.insert(0, base_input['zipcode2'])
        #### address ####
        win.addressboxlabel = ttk.Label(win.reg_frame5, text="送り先住所", padding=(106, 10, 3, 10))
        win.addressboxlabel.pack(side="left")
        win.addressbox = tk.Entry(win.reg_frame5, width=65, textvariable='')
        win.addressbox.pack(side="left")
        win.addressbox.insert(0, base_input['address1'])
        win.addressboxlabel2 = ttk.Label(win.reg_frame6, text="番地・号・建物名・部屋番号", padding=(24, 10, 3, 10))
        win.addressboxlabel2.pack(side="left")
        win.addressbox2 = tk.Entry(win.reg_frame6, width=65)
        win.addressbox2.pack(side="left")
        win.addressbox2.insert(0, base_input['address2'])
        #### tel ####
        win.telboxLabel = ttk.Label(win.reg_frame7, text="送り先電話番号", padding=(82, 10, 3, 10))
        win.telboxLabel.pack(side="left")
        win.telbox = tk.Entry(win.reg_frame7)
        win.telbox.pack(side="left")
        tel = base_input['tel']
        if str(tel) != '' and str(tel)[0] != '0':
            tel = '0' + str(tel)
        win.telbox.insert(0, tel)
        #### date ####
        win.dateboxLabel = ttk.Label(win.reg_frame8, text="日付", padding=(138, 10, 3, 10))
        win.dateboxLabel.pack(side="left")
        win.datebox = tk.Entry(win.reg_frame8)
        win.datebox.pack(side="left")
        win.datebox.insert(0, base_input['date'])
        #### order ####
        win.orderboxLabel = ttk.Label(win.reg_frame9, text="注文内容", padding=(115, 10, 3, 10))
        win.orderboxLabel.pack(side="left")
        win.orderbox = tk.Entry(win.reg_frame9, width=65)
        win.orderbox.pack(side="left")
        win.orderbox.insert(0, base_input['order'])
        #### ok & close button ####
        win.ok = tk.Button(win.reg_frame10, text="OK", width=5, height=2, padx=44, pady=1)
        win.ok.bind("<ButtonPress>", self.__setup_sendto_input)
        win.ok.pack()
        #### cancel & close button ####
        win.cancel = tk.Button(win.reg_frame10, text="Cancel", width=5, height=2, padx=44, pady=1)
        win.cancel.bind("<ButtonPress>", self.__close_window)
        win.cancel.pack()
        self.win = win

    # copy base data to sendto
    def __same_as_address1(self):
        if self.chkval.get() == True:
            self.win.namebox.insert(0, self.master.namebox.get())
            self.win.namekanabox.insert(0, self.master.namekanabox.get())
            self.win.zipcode_box1.insert(0, self.master.zipcode_box1.get())
            self.win.zipcode_box2.insert(0, self.master.zipcode_box2.get())
            self.win.addressbox.insert(0, self.master.addressbox.get())
            self.win.addressbox2.insert(0, self.master.addressbox2.get())
            self.win.telbox.insert(0, self.master.telbox.get())

    def sendto_window_input(self):
        return {
            'name': self.name, \
            'name_kana': self.namekana, \
            'zipcode1': self.zipcode1, \
            'zipcode2': self.zipcode2, \
            'address1': self.address1, \
            'address2': self.address2, \
            'tel': self.tel, \
            'date': self.date, \
            'order': self.order, \
        }

    ##### events #####
    def __setup_sendto_input(self, event):
        self.__update_input()
        if self.use_datatable:
            self.__update_csv()
            if self.add_to_csv:
                self.__add_datatable()
            else:
                self.__update_datatable()
        self.destroy()

    def __update_input(self):
        self.name = self.win.namebox.get()
        self.namekana = self.win.namekanabox.get()
        self.zipcode1 = self.win.zipcode_box1.get()
        self.zipcode2 = self.win.zipcode_box2.get()
        self.address1 = self.win.addressbox.get()
        self.address2 = self.win.addressbox2.get()
        self.tel = self.win.telbox.get()
        self.date = self.win.datebox.get()
        self.order = self.win.orderbox.get()

    #
    # update data
    #
    def __update_datatable(self):
        self.main_tree.delete(*self.main_tree.get_children())
        for record in self.data:
            self.main_tree.insert("","end",values=(record))

    def __update_csv(self):
        if not self.datatable:
            return
        children = self.datatable.get_children()
        if not self.datatable.exists(children):
            return
        old_record = self.datatable.item(children)
        if not old_record:
            return
        self.datatable.delete(*children)
        new_record = []
        name = self.name + '（' + self.namekana + '）'
        new_record.append(name)
        zip_code = self.zipcode1 + '-' + self.zipcode2
        new_record.append(zip_code)
        address = self.address1 + '　' + self.address2
        new_record.append(address)
        new_record.append(self.tel)
        new_record.append(self.date)
        new_record.append(self.order)
        self.datatable.insert("","end",values=new_record)
        # make deep copy of self.data.
        data_for_update = self.data[:]

        # update
        g = (d for d in data_for_update)
        for line in g:
            old_record_values = old_record['values']
            old_record_values = list(map(lambda d: str(d), old_record_values))
            tel = old_record_values[self.record_tel_index]
            sendto_data = line[-1]
            # check either sendto_data is empty or not.
            if not sendto_data:
                continue

            # check either line includes sendto_data or not.
            sendto_ary = sendto_data.split('/')
            if len(sendto_ary) < self.sendto_record_size:
                continue

            # fix tel if there isnt '0' in the head.
            if str(tel)[0] != '0':
                tel = '0' + str(tel)
                old_record_values[self.record_tel_index] = tel
                old_record_values = list(map(lambda d: str(d), old_record_values))
            if old_record_values == sendto_ary:
                index_for_update = self.data.index(line)
                self.data[index_for_update][-1] = '/'.join(new_record)
                self.customer_csv.write_header()
                self.customer_csv.write_all_data(self.data)

    #
    # add data
    #
    def __add_csv(self):
        pass

    def __add_datatable(self):
        pass

    def __close_window(self, event):
        self.destroy()
