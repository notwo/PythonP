import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
import re
import zenhan
from lib import util

class SendToWindow(tk.Frame):
    def __init__(self, master=None, **key):
        self.customer_csv = None
        self.add_to_csv = key.get('key').get('add_to_csv')
        self.use_datatable = key.get('key').get('use_datatable')
        self.same_input_data = key.get('key').get('same_input_data')
        self.sequential_state = key.get('key').get('sequential_state')
        if self.use_datatable or self.add_to_csv:
            self.customer_csv = key.get('key').get('customer_csv')
        if self.use_datatable:
            self.data = key.get('key').get('data')
            self.searched_data = key.get('key').get('searched_data')
            self.datatable = key.get('key').get('datatable')
            self.record_index = self.datatable.focus()
            self.record_tel_index = key.get('key').get('record_tel_index')
            self.sendto_record_size = key.get('key').get('sendto_record_size')
            self.main_tree = key.get('key').get('main_tree')
        self.util = util.Util()

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

        # multiple sendto input variables
        self.sendto_collection = []



    def open(self, base_input):
        # initialize toplevel window
        super().__init__(None)
        win = tk.Toplevel(self)
        win.transient(self.master)
        win.geometry("640x740")
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
        #### ok button ####
        win.ok = tk.Button(win.reg_frame10, text="送り先登録", width=5, height=2, padx=44, pady=1)
        win.ok.bind("<ButtonPress>", self.__setup_sendto_input)
        win.ok.pack()
        #### sequential register button ####
        win.sequential_ok = tk.Button(win.reg_frame10, text="送り先を連続登録", width=5, height=2, padx=44, pady=1, state=self.sequential_state)
        win.sequential_ok.bind("<ButtonPress>", self.__setup_sequential_sendto_input)
        win.sequential_ok.pack()
        #### cancel & close button ####
        win.cancel = tk.Button(win.reg_frame10, text="キャンセル", width=5, height=2, padx=44, pady=1)
        win.cancel.bind("<ButtonPress>", self.__close_window)
        win.cancel.pack()
        self.win = win



    # copy base data to sendto
    def __same_as_address1(self):
        if self.chkval.get() == True:
            if self.same_input_data:
                self.win.namebox.delete(0, tk.END)
                self.win.namebox.insert(0, self.same_input_data['name'])
                self.win.namekanabox.delete(0, tk.END)
                self.win.namekanabox.insert(0, self.same_input_data['name_kana'])
                self.win.zipcode_box1.delete(0, tk.END)
                self.win.zipcode_box1.insert(0, self.same_input_data['zipcode1'])
                self.win.zipcode_box2.delete(0, tk.END)
                self.win.zipcode_box2.insert(0, self.same_input_data['zipcode2'])
                self.win.addressbox.delete(0, tk.END)
                self.win.addressbox.insert(0, self.same_input_data['address1'])
                self.win.addressbox2.delete(0, tk.END)
                self.win.addressbox2.insert(0, self.same_input_data['address2'])
                self.win.telbox.delete(0, tk.END)
                self.win.telbox.insert(0, self.same_input_data['tel'])
            elif self.main_tree:
                main_record = self.main_tree.item(self.main_tree.focus())['values']
                name = main_record[0].split('（')
                zipcode = main_record[1].split('-')
                address = main_record[2].split('　')
                tel = main_record[3]
                if str(tel) != '' and str(tel)[0] != '0':
                    tel = '0' + str(tel)
                self.win.namebox.delete(0, tk.END)
                self.win.namebox.insert(0, name[0])
                self.win.namekanabox.delete(0, tk.END)
                self.win.namekanabox.insert(0, self.util.delete_last_str(name[1], '|'))
                self.win.zipcode_box1.delete(0, tk.END)
                self.win.zipcode_box1.insert(0, zipcode[0])
                self.win.zipcode_box2.delete(0, tk.END)
                self.win.zipcode_box2.insert(0, zipcode[1])
                self.win.addressbox.delete(0, tk.END)
                self.win.addressbox.insert(0, address[0])
                self.win.addressbox2.delete(0, tk.END)
                self.win.addressbox2.insert(0, address[1])
                self.win.telbox.delete(0, tk.END)
                self.win.telbox.insert(0, tel)



    def sendto_collection_input(self):
        return self.sendto_collection



    def reset_sendto_collection_input(self):
        self.sendto_collection = []



    def sendto_window_input(self):
        return {
            'name': self.name, \
            'name_kana': self.namekana, \
            'zipcode1': self.zipcode1, \
            'zipcode2': self.zipcode2, \
            'address1': self.address1, \
            'address2': self.address2, \
            'tel': self.tel, \
            'date': re.sub('\n|\r\n|\r', '', self.date), \
            'order': re.sub('\n|\r\n|\r', '', self.order), \
        }



    def reset_window_input(self):
        self.name = ''
        self.namekana = ''
        self.zipcode1 = ''
        self.zipcode2 = ''
        self.address1 = ''
        self.address2 = ''
        self.tel = ''
        self.date = ''
        self.order = ''



    def __reset_form_input(self):
        self.win.namebox.delete(0, tk.END)
        self.win.namekanabox.delete(0, tk.END)
        self.win.zipcode_box1.delete(0, tk.END)
        self.win.zipcode_box2.delete(0, tk.END)
        self.win.addressbox.delete(0, tk.END)
        self.win.addressbox2.delete(0, tk.END)
        self.win.telbox.delete(0, tk.END)
        self.win.datebox.delete(0, tk.END)
        self.win.orderbox.delete(0, tk.END)



    #
    ##### events #####
    #

    def __setup_sendto_input(self, event, sequential=False):
        # validate
        if not self.__validate_input():
            mbox.showwarning('', '未入力の項目があります。')
            return

        # set instance val from window input
        self.__update_input()

        # datatable work
        if self.use_datatable:
            if self.add_to_csv:
                self.__add_datatable()
            else:
                self.__update_csv()
                self.__update_datatable()

        # close window
        if sequential:
            self.__register_sendto_collection()
        else:
            self.destroy()



    def __setup_sequential_sendto_input(self, event):
        # 'disabled' state but dont make an effect for some reason, so we must explicitly check its status
        if self.win.sequential_ok['state'] == tk.DISABLED:
            return
        self.__setup_sendto_input(event=None, sequential=True)



    def __register_sendto_collection(self):
        # memorize all sendto input
        self.sendto_collection.append('/'.join([ \
            self.name + '（' + self.namekana + '）', \
            self.zipcode1 + '-' + self.zipcode2, \
            self.address1 + '　' + self.address2, \
            self.tel, \
            self.date, \
            self.order \
        ]))
        self.__reset_form_input()



    def __validate_input(self):
        if self.win.namebox.get().replace(',', '') == '' or \
            self.win.namekanabox.get().replace(',', '') == '' or \
            self.win.zipcode_box1.get().replace(',', '') == '' or \
            self.win.zipcode_box2.get().replace(',', '') == '' or \
            self.win.addressbox.get().replace(',', '') == '' or \
            self.win.addressbox2.get().replace(',', '') == '' or \
            self.win.telbox.get().replace(',', '') == '' or \
            self.win.datebox.get().replace(',', '') == '':
            return False
        return True



    def __update_input(self):
        self.name = self.win.namebox.get().replace(',', '')
        self.namekana = zenhan.h2z(self.win.namekanabox.get().replace(',', ''))
        self.zipcode1 = self.win.zipcode_box1.get().replace(',', '')
        self.zipcode2 = self.win.zipcode_box2.get().replace(',', '')
        self.address1 = self.win.addressbox.get().replace(',', '')
        self.address2 = self.win.addressbox2.get().replace(',', '')
        self.tel = self.win.telbox.get()
        self.date = self.win.datebox.get().replace(',', '')
        self.order = self.win.orderbox.get().replace(',', '')



    def __input_record(self):
        input = self.sendto_window_input()
        new_record = []
        new_record.append(input['name'] + '（' + input['name_kana'] + '）')
        new_record.append(input['zipcode1'] + '-' + input['zipcode2'])
        new_record.append(input['address1'] + '　' + input['address2'])
        new_record.append(input['tel'])
        new_record.append(input['date'])
        new_record.append(input['order'])
        return new_record



    #
    # update data
    #
    def __update_csv(self):
        if not self.datatable:
            return
        change_target_record_index = self.datatable.focus()
        change_target_record = self.datatable.item(change_target_record_index)['values']
        main_record = self.main_tree.item(self.main_tree.focus())['values']
        if len(main_record) < 5:
            return
        children = self.datatable.get_children()
        self.datatable.delete(*children)
        main_record = self.util.change_all_records_to_str_in_array_without_newline(array=main_record)
        main_record = ','.join(main_record)
        tel = change_target_record[self.record_tel_index]
        if str(tel)[0] != '0':
            tel = '0' + str(tel)
            change_target_record[self.record_tel_index] = tel
        change_target_record = self.util.change_all_records_to_str_in_array_without_newline(array=change_target_record)
        new_record = self.__input_record()
        sendto_record = main_record.split(',')[4]
        new_sendto_record = []
        g = (d for d in sendto_record.split('|'))
        for record_str in g:
            record = record_str.split('/')
            if change_target_record == record:
                new_sendto_record.append('/'.join(new_record))
                self.datatable.insert("","end",values=new_record)
            else:
                new_sendto_record.append('/'.join(record))
                self.datatable.insert("","end",values=record)
        # make deep copy of self.data.
        data_for_update = self.data[:]

        # update
        g = (d for d in data_for_update)
        for line in g:
            _line = self.util.change_all_records_to_str_in_array_without_newline(array=line)
            sendto_line = _line[-1]
            if sendto_record == sendto_line:
                index_for_update = self.data.index(line)
                self.data[index_for_update][-1] = '|'.join(new_sendto_record)
                if self.data[index_for_update][-1][-1] != '\n':
                    self.data[index_for_update][-1] += '\n'
                self.customer_csv.write_header()
                self.customer_csv.write_all_data(self.data)
        self.searched_data = self.data[:]



    def __update_datatable(self):
        self.main_tree.delete(*self.main_tree.get_children())
        for record in self.data:
            self.main_tree.insert("","end",values=(record))



    #
    # add data
    #
    def __add_datatable(self):
        if self.main_tree is None or self.datatable is None:
            return
        record_index = self.main_tree.focus()
        main_record = self.main_tree.item(record_index)['values']
        tel = main_record[self.record_tel_index]
        if str(tel)[0] != '0':
            tel = '0' + str(tel)
            main_record[self.record_tel_index] = tel
        selected_base_record = main_record[:4]
        new_sendto_record = self.__input_record()
        new_main_record = ','.join(main_record)
        # todo: fix magic number
        if len(main_record) >= 5:
            new_main_record = new_main_record.replace('\n', '') + '|' + '/'.join(new_sendto_record) + '\n'
        else:
            new_main_record = new_main_record.replace('\n', '') + ',' + '/'.join(new_sendto_record) + '\n'
        self.datatable.insert("","end",values=new_sendto_record)
        self.main_tree.delete(*self.main_tree.get_children())
        data_for_add = self.data[:]
        g = (d for d in data_for_add)
        for line in g:
            # compare representative data in array
            if line[0] == main_record[0]:
                index = self.data.index(line)
                self.data[index] = new_main_record.split(',')
                self.searched_data = self.data[:]
                self.customer_csv.write_header()
                self.customer_csv.write_all_data(self.data)
                break
        for record in self.data:
            base_record = record[:4]
            iid = self.main_tree.insert("","end",values=(record))
            if selected_base_record == base_record and self.main_tree.exists(iid):
                self.main_tree.focus(iid)
                self.main_tree.selection_set(iid)



    def __close_window(self, event):
        self.reset_sendto_collection_input()
        self.destroy()
