from tkinter import ttk

class DataTable(ttk.Treeview):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.frame = key.get('key').get('frame')
        ttk.Treeview.__init__(self, self.frame)

        size = key.get('key').get('size')
        column_width = key.get('key').get('column_width')
        headings = key.get('key').get('headings')
        if len(column_width) != size or len(headings) != size:
            return
        self["columns"] = list(range(1, size + 1))
        self["show"] = "headings"
        for num in range(0, size):
            self.column(num + 1, width=column_width[num])
            self.heading(num + 1, text=headings[num])
        data = key.get('key').get('data')
        for record in data:
            self.insert("","end",values=(record))
        self.bind('<Double-1>', self.__open_edit)

    def __open_edit(self, event):
        record_index = self.focus()
        if record_index:
            record = self.item(record_index)['values']
