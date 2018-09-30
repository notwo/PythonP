import tkinter as tk
from tkinter import ttk
from modules import edit_window as ewin
from modules import sendto_window as swin

class DataTable(ttk.Treeview):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.sort_mode = []
        self.use_datatable = True
        self.frame = key.get('key').get('frame')
        ttk.Treeview.__init__(self, self.frame)
        self.data = key.get('key').get('data')
        height = key.get('key').get('height')
        self.searched_data = key.get('key').get('searched_data')
        self.size = key.get('key').get('size')
        column_width = key.get('key').get('column_width')
        self.search_on = key.get('key').get('search_on')
        self.headings = key.get('key').get('headings')
        self.show_directly = key.get('key').get('show_directly')
        self.record_tel_index = key.get('key').get('record_tel_index')
        self.customer_csv = key.get('key').get('customer_csv')
        self.sendto_length = key.get('key').get('sendto_length')
        self.sendto_tree = key.get('key').get('sendto_tree')
        if len(column_width) != self.size or len(self.headings) != self.size:
            return
        self["columns"] = list(range(1, self.size + 1))
        not_display_last_column = key.get('key').get('not_display_last_column')
        if not_display_last_column:
            self["displaycolumns"] = list(range(1, self.size))
        self["show"] = "headings"
        self["height"] = height
        for num in range(0, self.size):
            self.column(num + 1, width=column_width[num], minwidth=30)
            self.heading(num + 1, text=self.headings[num], command=self.__sort)
            self.sort_mode.append('asc')
        if self.show_directly:
            for record in self.data:
                self.insert("","end",values=(record))
        self.main_tree = None
        # set each row's event
        self.bind('<Double-1>', self.__open_edit)
        if self.show_directly:
            self.bind('<Button-1>', self.__show_sendto)

    def pass_tree(self, tree):
        self.main_tree = tree



    def delete_selected_record(self):
        self.delete(self.focus())



    def update_searched_data(self, sdata):
        self.searched_data = sdata[:]



    ##### events #####
    def __open_edit(self, event):
        DATATABLE_POSITION_Y_BORDER = 700
        # specify clicked window
        record_index = self.focus()
        if record_index:
            y = int(self.winfo_geometry().split('x')[0])
            if y > DATATABLE_POSITION_Y_BORDER:
                y = self.winfo_pointery() - self.winfo_rooty()
                record_index = self.identify_row(y)
                record = self.item(record_index)['values']
                tmp_sendto_name = record[0].split('（')
                sendto_name = tmp_sendto_name[0]
                sendto_namekana = tmp_sendto_name[1].replace('）', '')
                tmp_zip_code = record[1].split('-')
                sendto_zipcode1 = tmp_zip_code[0]
                sendto_zipcode2 = tmp_zip_code[1]
                tmp_address = record[2].split('　')
                sendto_address1 = tmp_address[0]
                sendto_address2 = tmp_address[1]
                sendto_tel = record[3]
                sendto_date = record[4]
                sendto_order = record[5]

                swin_for_update = swin.SendToWindow(self, key={ \
                    'customer_csv': self.customer_csv, \
                    'data': self.data, \
                    'searched_data': self.searched_data, \
                    'use_datatable': self.use_datatable, \
                    'datatable': self, \
                    'record_tel_index': self.record_tel_index, \
                    'sendto_record_size': self.size, \
                    'main_tree': self.main_tree, \
                    'sequential_state': tk.DISABLED, \
                })
                swin_for_update.open({
                    'name': sendto_name, \
                    'name_kana': sendto_namekana, \
                    'zipcode1': sendto_zipcode1, \
                    'zipcode2': sendto_zipcode2, \
                    'address1': sendto_address1, \
                    'address2': sendto_address2, \
                    'tel': sendto_tel, \
                    'date': sendto_date, \
                    'order': sendto_order, \
                })
            else:
                record = self.item(record_index)['values']
                ewin.EditWindow(self, key={ \
                    'customer_csv': self.customer_csv, \
                    'record': record, \
                    'data': self.data, \
                    'searched_data': self.searched_data, \
                    'record_index': record_index, \
                    'datatable': self, \
                    'sendto_record_size': self.size, \
                    'record_tel_index': self.record_tel_index, \
                })



    def __show_sendto(self, event):
        y = self.winfo_pointery() - self.winfo_rooty()
        record_index = self.identify_row(y)
        # if cant get index, skip it.
        if not (record_index or self.sendto_length):
            return
        record = self.item(record_index)['values']
        self.sendto_tree.delete(*self.sendto_tree.get_children())
        if len(record) >= self.sendto_length:
            # with sendto
            sendto_values = record[self.sendto_length - 1].split('|')
            if sendto_values:
                g = (d for d in sendto_values)
                for v in g:
                    self.sendto_tree.insert("","end",values=(v.split('/')))
        else:
            # without sendto
            self.sendto_tree.delete(*self.sendto_tree.get_children())



    def __sort(self):
        if not self.search_on:
            return
        # sorted data
        val = []
        hash_for_sort = {}

        # specify clicked header and sort
        x = self.winfo_pointerx() - self.winfo_rootx()
        column = self.identify_column(x)
        sort_num = int(column[1:])

        # change sort mode
        if self.sort_mode[sort_num - 1] == 'asc':
            self.sort_mode[sort_num - 1] = 'desc'
        else:
            self.sort_mode[sort_num - 1] = 'asc'

        g = (d for d in self.searched_data)
        for row in g:
            v = row[sort_num - 1]
            hash_for_sort[v] = row
            val.append(v)
        if (self.sort_mode[sort_num - 1] == 'asc'):
            val.sort()
        else:
            val.sort(reverse=True)

        # delete all data and set sorted data
        g2 = (d for d in val)
        self.delete(*self.get_children())
        for v in g2:
            self.insert("","end",values=(hash_for_sort[v]))
