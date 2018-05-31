import tkinter as tk
import tkinter.ttk as ttk
import modules.customer_listbox as customer_listbox
import modules.button_events as button_events
import os

OUT_CSV = "customer.csv"

class __CustomerDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('顧客管理テスト')

        # instance variables
        self.customers = []
        self.csv = ""

        # set view
        self.pack()
        self.read_csv()
        self.set_list()
        self.set_form_widgets()

    def set_form_widgets(self):
        # tabs
        self.notebook = ttk.Notebook(width=900, height=500)
        self.reg_tab = tk.Frame(self.notebook)
        self.lst_tab = tk.Frame(self.notebook)
        self.notebook.add(self.reg_tab, text="顧客情報登録", padding=2)
        self.notebook.add(self.lst_tab, text="顧客一覧", padding=2)
        self.notebook.pack()
        ### sub widgets ###
        self.reg_frame = tk.Frame(self.reg_tab, padx=10, pady=20)
        self.reg_frame.pack(fill=tk.BOTH)
        self.list_frame = tk.Frame(self.reg_tab, padx=10)
        self.list_frame.pack(fill=tk.BOTH)
        #### name ####
        self.nameboxlabel = ttk.Label(self.reg_frame, text="氏名", padding=(1, 10, 3, 10))
        self.nameboxlabel.pack(side="left")
        self.namebox = tk.Entry(self.reg_frame)
        self.namebox.pack(side="left")
        #### tel ####
        self.telboxLabel = ttk.Label(self.reg_frame, text="電話番号", padding=(15, 10, 3, 10))
        self.telboxLabel.pack(side="left")
        self.telbox = tk.Entry(self.reg_frame)
        self.telbox.pack(side="left")
        #### address ####
        self.addressboxlabel = ttk.Label(self.reg_frame, text="住所", padding=(15, 10, 3, 10))
        self.addressboxlabel.pack(side="left")
        self.addressbox = tk.Entry(self.reg_frame)
        self.addressbox.pack(side="left")
        #### prev order ####
        self.prev_order_label = ttk.Label(self.reg_frame, text="前回の注文", padding=(15, 10, 3, 10))
        self.prev_order_label.pack(side="left")
        self.prev_order_box = tk.Entry(self.reg_frame, width=30)
        self.prev_order_box.pack(side="left")
        #### reg button ####
        self.button_frame = tk.Frame(self.reg_tab, pady=8)
        self.button_frame.pack(fill=tk.BOTH)
        self.register = tk.Button(self.button_frame, text="登録", width=5, height=2, padx=44, pady=1)
        self.register.bind("<ButtonPress>", button_events.bev)
        self.register.pack()
        ### /sub widgets ###
        # for list tab
        
    def read_csv(self):
        crnt_dir = os.path.dirname(os.path.abspath(__file__))
        target_file_path = "../"
        self.csv = os.path.join(crnt_dir, target_file_path)
        if not os.path.exists(self.csv + OUT_CSV):
            self.__write_header()

        f = open(self.csv + OUT_CSV, 'r')
        # read header info
        str = f.readline()
        while str:
            str = f.readline()
            self.customers.append(str)
        f.close()
    
    def set_list(self):
        ""

    def __write_header(self):
        f = open(self.csv + OUT_CSV, 'w')
        f.write("氏名,電話番号,住所,前回の注文")
        f.close()

root = tk.Tk()
root.geometry("946x540")
dialog = __CustomerDialog(master=root)