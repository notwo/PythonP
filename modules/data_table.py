import tkinter as tk
from tkinter import ttk
from modules import edit_window as ewin
from modules import sendto_window as swin

class DataTable(ttk.Treeview):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.sort_mode = []
        self.update_directly = True
        self.frame = key.get('key').get('frame')
        ttk.Treeview.__init__(self, self.frame)
        self.data = key.get('key').get('data')
        height = key.get('key').get('height')
        self.searched_data = key.get('key').get('searched_data')
        size = key.get('key').get('size')
        column_width = key.get('key').get('column_width')
        self.search_on = key.get('key').get('search_on')
        self.headings = key.get('key').get('headings')
        self.show_directly = key.get('key').get('show_directly')
        self.customer_csv = key.get('key').get('customer_csv')
        self.sendto_length = key.get('key').get('sendto_length')
        self.sendto_tree = key.get('key').get('sendto_tree')
        if len(column_width) != size or len(self.headings) != size:
            return
        self["columns"] = list(range(1, size + 1))
        not_display_last_column = key.get('key').get('not_display_last_column')
        if not_display_last_column:
            self["displaycolumns"] = list(range(1, size))
        self["show"] = "headings"
        self["height"] = height
        for num in range(0, size):
            self.column(num + 1, width=column_width[num], minwidth=30)
            self.heading(num + 1, text=self.headings[num], command=self.__sort)
            self.sort_mode.append('asc')
        if self.show_directly:
            for record in self.data:
                self.insert("","end",values=(record))
        
        # sendto input
        self.sendto_name = ''
        self.sendto_zipcode1 = ''
        self.sendto_zipcode2 = ''
        self.sendto_address1 = ''
        self.sendto_address2 = ''
        self.sendto_tel = ''
        self.sendto_date = ''
        self.sendto_order = ''

        # set each row's event
        self.bind('<Double-1>', self.__open_edit)
        if self.show_directly:
            self.bind('<Button-1>', self.__show_sendto)

    ##### events #####
    def __open_edit(self, event):
        # specify clicked window
        record_index = self.focus()
        if record_index:
            y = int(self.winfo_geometry().split('x')[0])
            if y > 700:
                y = self.winfo_pointery() - self.winfo_rooty()
                record_index = self.identify_row(y)
                record = self.item(record_index)['values']
                self.sendto_name = record[0]
                zip_code = record[1].split('-')
                self.sendto_zipcode1 = zip_code[0]
                self.sendto_zipcode2 = zip_code[1]
                address = record[2].split('　')
                self.sendto_address1 = address[0]
                self.sendto_address2 = address[1]
                self.sendto_tel = record[3]
                self.sendto_date = record[4]
                self.sendto_order = record[5]

                swin.SendToWindow(self, key={ \
                    'customer_csv': self.customer_csv, \
                    'data': self.data, \
                    'update_directly': self.update_directly, \
                    'datatable': self, \
                })
            else:
                record = self.item(record_index)['values']
                ewin.EditWindow(self, key={ \
                    "record": record, \
                    "data": self.data, \
                    "index": record_index, \
                })

    def __show_sendto(self, event):
        y = self.winfo_pointery() - self.winfo_rooty()
        record_index = self.identify_row(y)
        # if cant get index, skip it.
        if not (record_index or self.sendto_length):
            return
        record = self.item(record_index)['values']
        if len(record) >= self.sendto_length:
            val = record[self.sendto_length - 1].split('、')
            self.sendto_tree.delete(*self.sendto_tree.get_children())
            self.sendto_tree.insert("","end",values=(val))
        else:
            self.sendto_tree.delete(*self.sendto_tree.get_children())

    def __sort(self):
        if not self.search_on:
            return
        # sort
        val = []
        hash_for_sort = {}

        x = self.winfo_pointerx() - self.winfo_rootx()
        column = self.identify_column(x)
        sort_num = int(column[1:])
        # change sort mode
        if self.sort_mode[sort_num - 1] == 'asc':
            self.sort_mode[sort_num - 1] = 'desc'
        else:
            self.sort_mode[sort_num - 1] = 'asc'

        # specify clicked header and sort
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
