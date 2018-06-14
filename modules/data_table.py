from tkinter import ttk

class DataTable(ttk.Treeview):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.frame = key.get('key').get('frame')
        ttk.Treeview.__init__(self, self.frame)

        self.data = key.get('key').get('data')
        size = key.get('key').get('size')
        column_width = key.get('key').get('column_width')
        headings = key.get('key').get('headings')
        if len(column_width) != size or len(headings) != size:
            return
        self["columns"] = list(range(1, size + 1))
        self["show"] = "headings"
        for num in range(0, size):
            self.column(num + 1, width=column_width[num])
            self.heading(num + 1, text=headings[num], command=self.__sort)
        for record in self.data:
            self.insert("","end",values=(record))
        # set each row's event
        self.bind('<Double-1>', self.__open_edit)

    def __open_edit(self, event):
        record_index = self.focus()
        if record_index:
            record = self.item(record_index)['values']

    def __sort(self):
        x = self.winfo_pointerx() - self.winfo_rootx()
        print(self.identify_column(x))
        g = (d for d in self.data)
        for row in g:
            print(row)
