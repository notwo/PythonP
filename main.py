import tkinter as tk
from modules import dialog

root = tk.Tk()
root.geometry("986x640")

d = dialog.CustomerDialog(master=root)
d.mainloop()
