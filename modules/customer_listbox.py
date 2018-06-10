import tkinter as tk

class CustomerListBox(tk.Listbox):
    def __init__(self, master=None, **key):
        super().__init__(master)
        self.frame = key.get('key').get('frame')
        self.yScroll = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.yScroll.pack(side=tk.RIGHT, fill=tk.Y, expand=1)
        self.xScroll = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        self.xScroll.pack(side=tk.BOTTOM, fill=tk.X, expand=1)
        tk.Listbox.__init__(self, self.frame, width=80)
        self.xScroll['command'] = self.xview
        self.yScroll['command'] = self.yview
