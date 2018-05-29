import tkinter

class CustomerListBox(tkinter.Listbox):
    def __init__(self, master, **key):
        self.frame = tkinter.Frame(master)
        
