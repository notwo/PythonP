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
        # for register tab
        self.reg_form_frame = tk.Frame(self.reg_tab)
        self.reg_form_frame.pack(fill=tk.BOTH)
        ### sub widgets ###
        self.nameBoxLabel = tk.Label(self.reg_form_frame, text="氏名")
        self.nameBoxLabel.pack(side="left")
        self.nameBox = tk.Entry(self.reg_form_frame)
        self.nameBox.pack()
        self.telBoxLabel = tk.Label(self.reg_form_frame, text="電話番号")
        self.telBoxLabel.pack(side="left")
        self.telBox = tk.Entry(self.reg_form_frame)
        self.telBox.pack()
        self.addressBoxLabel = tk.Label(self.reg_form_frame, text="住所")
        self.addressBoxLabel.pack(side="left")
        self.addressBox = tk.Entry(self.reg_form_frame)
        self.addressBox.pack()
        self.register = tk.Button(self.reg_form_frame, text="登録",)
        self.register.bind("<ButtonPress>", button_events.bev)
        self.register.pack(side="right")
        ### /sub widgets ###
        # for list tab
        


root = tk.Tk()
root.geometry("1024x640")
dialog = CustomerDialog(master=root)