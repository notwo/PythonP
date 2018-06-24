from tkinter import ttk
from modules import edit_window as ewin

class DataTable(ttk.Treeview):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.sort_mode = []
        self.frame = key.get('key').get('frame')
        ttk.Treeview.__init__(self, self.frame)

        self.data = key.get('key').get('data')
        self.searched_data = key.get('key').get('searched_data')
        size = key.get('key').get('size')
        column_width = key.get('key').get('column_width')
        self.headings = key.get('key').get('headings')
        if len(column_width) != size or len(self.headings) != size:
            return
        self["columns"] = list(range(1, size + 1))
        self["show"] = "headings"
        for num in range(0, size):
            self.column(num + 1, width=column_width[num])
            self.heading(num + 1, text=self.headings[num], command=self.__sort)
            self.sort_mode.append('asc')
        for record in self.data:
            self.insert("","end",values=(record))
        # set each row's event
        self.bind('<Double-1>', self.__open_edit)

    ##### events #####
    def __open_edit(self, event):
        record_index = self.focus()
        if record_index:
            record = self.item(record_index)['values']
            ewin.EditWindow(self, key={ \
                "record": record, \
                "data": self.data, \
                "index": record_index \
            })

    def __sort(self):
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
