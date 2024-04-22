import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

def load_file():
    file_path = filedialog.askopenfilename(initialdir="~/Desktop", title="Select file",
                                           filetypes=(("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv"), ("All files", "*.*")))
    if file_path:
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)
            display_data(df)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

def display_data(data):
    # Clear existing data in the Treeview
    clear_data()
    # Set the Treeview columns to dataframe column headers
    tree["columns"] = list(data.columns)
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
    # Configure column headings
    for column in tree["columns"]:
        tree.heading(column, text=column)
        tree.column(column, width=120)
    # Insert data rows
    for row in data.to_numpy().tolist():
        tree.insert("", tk.END, values=row)

def clear_data():
    tree.delete(*tree.get_children())

root = tk.Tk()
root.title("Excel and CSV File Viewer")
root.geometry("800x600")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=load_file)

tree = ttk.Treeview(root)
tree.pack(expand=True, fill=tk.BOTH)

root.mainloop()
