import tkinter as tk
from modules import dialog

root = tk.Tk()
root.geometry("946x540")

d = dialog.CustomerDialog(master=root)
d.mainloop()
