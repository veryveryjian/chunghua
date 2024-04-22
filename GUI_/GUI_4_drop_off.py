import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

def load_file(data_container, label, sheet_combobox):
    file_path = filedialog.askopenfilename(
        initialdir="~/Desktop", title="Select file",
        filetypes=(("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if file_path:
        label.config(text=f"File: {file_path}")
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
                data_container["dataframe"] = df
                update_fields(data_container["fields"], df)
                sheet_combobox['values'] = ['N/A']
                sheet_combobox.current(0)
                sheet_combobox.config(state='disabled')
            else:
                dfs = pd.read_excel(file_path, sheet_name=None)
                sheets = list(dfs.keys())
                data_container["dataframes"] = dfs
                update_fields(data_container["fields"], dfs[sheets[0]])
                sheet_combobox['values'] = sheets
                sheet_combobox.current(0)
                sheet_combobox.config(state='readonly')
                data_container["current_sheet"] = sheets[0]
                data_container["dataframe"] = dfs[sheets[0]]
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

def update_sheet(data_container, sheet_name):
    if sheet_name in data_container["dataframes"]:
        df = data_container["dataframes"][sheet_name]
        data_container["dataframe"] = df
        update_fields(data_container["fields"], df)

def update_fields(field_combobox, df):
    fields = list(df.columns)
    field_combobox['values'] = fields
    field_combobox.current(0)

def join_data():
    if data1.get("dataframe") is None or data2.get("dataframe") is None:
        messagebox.showerror("Error", "Please load both files first.")
        return
    field_name1 = data1["fields"].get()
    field_name2 = data2["fields"].get()
    try:
        result = pd.merge(data1["dataframe"], data2["dataframe"], how='left', left_on=field_name1, right_on=field_name2)
        display_data(result)  # Display the result in the GUI
        save_path = os.path.join(os.path.expanduser("~/Desktop"), "join_data.xlsx")
        result.to_excel(save_path, index=False)
        messagebox.showinfo("Success", f"Data joined successfully. Saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to join data: {e}")

def display_data(df):
    # Clear the previous tree view contents
    for i in tree.get_children():
        tree.delete(i)
    # Define new columns in the tree view
    tree["columns"] = list(df.columns)
    tree["displaycolumns"] = list(df.columns)
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="w")
    # Insert new data rows into the tree view
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

root = tk.Tk()
root.title("Data Joiner")
root.geometry("800x600")

data1 = {"dataframe": None, "dataframes": None, "fields": ttk.Combobox(root), "sheet": ttk.Combobox(root)}
data2 = {"dataframe": None, "dataframes": None, "fields": ttk.Combobox(root), "sheet": ttk.Combobox(root)}

# Setup Treeview for displaying DataFrame
tree = ttk.Treeview(root)
tree.pack(expand=True, fill="both")

load1_button = ttk.Button(root, text="Load Data 1", command=lambda: load_file(data1, file1_label, data1["sheet"]))
load1_button.pack()
file1_label = ttk.Label(root, text="No file loaded for Data 1")
file1_label.pack()
data1["fields"].pack()
data1["sheet"].pack()
data1["sheet"].bind("<<ComboboxSelected>>", lambda event: update_sheet(data1, data1["sheet"].get()))

load2_button = ttk.Button(root, text="Load Data 2", command=lambda: load_file(data2, file2_label, data2["sheet"]))
load2_button.pack()
file2_label = ttk.Label(root, text="No file loaded for Data 2")
file2_label.pack()
data2["fields"].pack()
data2["sheet"].pack()
data2["sheet"].bind("<<ComboboxSelected>>", lambda event: update_sheet(data2, data2["sheet"].get()))

join_button = ttk.Button(root, text="Join", command=join_data)
join_button.pack()

root.mainloop()
