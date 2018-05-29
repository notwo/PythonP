import tkinter as tk
import tkinter.ttk as ttk
import modules.customer_listbox as customer_listbox
import modules.button_events as button_events

class CustomerDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('顧客管理テスト')
        self.pack()
        self.set_widgets()

    def set_widgets(self):
        # tabs
        self.notebook = ttk.Notebook(width=1000, height=600)
        self.reg_tab = tk.Frame(self.notebook)
        self.lst_tab = tk.Frame(self.notebook)
        self.notebook.add(self.reg_tab, text="顧客情報登録", padding=2)
        self.notebook.add(self.lst_tab, text="顧客一覧", padding=2)
        self.notebook.pack()
        ### sub widgets ###
        #### name ####
        self.namebox_frame = tk.Frame(self.reg_tab, padx=10)
        self.namebox_frame.pack(fill=tk.BOTH)
        self.nameboxlabel = tk.Label(self.namebox_frame, text="氏名")
        self.nameboxlabel.pack(fill="x")
        self.namebox = tk.Entry(self.namebox_frame)
        self.namebox.pack()
        #### tel ####
        self.telbox_frame = tk.Frame(self.reg_tab, padx=10)
        self.telbox_frame.pack(fill=tk.BOTH)
        self.telboxLabel = tk.Label(self.telbox_frame, text="電話番号")
        self.telboxLabel.pack()
        self.telbox = tk.Entry(self.telbox_frame)
        self.telbox.pack()
        #### address ####
        self.addressbox_frame = tk.Frame(self.reg_tab, padx=10)
        self.addressbox_frame.pack(fill=tk.BOTH)
        self.addressboxlabel = tk.Label(self.addressbox_frame, text="住所")
        self.addressboxlabel.pack()
        self.addressbox = tk.Entry(self.addressbox_frame)
        self.addressbox.pack()
        #### reg button ####
        self.reg_button_frame = tk.Frame(self.reg_tab, padx=10)
        self.reg_button_frame.pack(fill=tk.BOTH)
        self.register = tk.Button(self.reg_button_frame, text="登録",)
        self.register.bind("<ButtonPress>", button_events.bev)
        self.register.pack()
        ### /sub widgets ###
        # for list tab
        


root = tk.Tk()
root.geometry("1024x640")
dialog = CustomerDialog(master=root)