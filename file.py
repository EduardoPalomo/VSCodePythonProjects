import tkinter as tk
from tkinter import ttk, filedialog
from faker import Faker
import csv

fake = Faker()

def generate_dummy_data(rows, columns, data_types):
    data = []
    for _ in range(rows):
        row = [getattr(fake, data_type)() for data_type in data_types]
        data.append(row)
    return data

def save_to_csv(data, column_names):
    file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(column_names)
            csv_writer.writerows(data)

def generate_and_save_data():
    rows = int(rows_entry.get())
    columns = int(columns_entry.get())
    data_types = [data_type.get() for data_type in data_types_combobox]
    column_names = [column_name.get() for column_name in column_names_entry]
    data = generate_dummy_data(rows, columns, data_types)
    save_to_csv(data, column_names)

# Create and configure the main application window
app = tk.Tk()
app.title("Dummy Data Generator")
app.geometry("600x400")
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)

# User interface elements
rows_label = ttk.Label(app, text="Number of rows:")
rows_label.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
rows_entry = ttk.Entry(app)
rows_entry.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)

columns_label = ttk.Label(app, text="Number of columns:")
columns_label.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
columns_entry = ttk.Entry(app)
columns_entry.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

data_types_label = ttk.Label(app, text="Data types:")
data_types_label.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)

column_names_label = ttk.Label(app, text="Column names:")
column_names_label.grid(column=2, row=2, padx=10, pady=10, sticky=tk.W)

# Add data type selection for each column
data_types_combobox = []
column_names_entry = []
sample_data_types = [method for method in dir(fake) if not method.startswith('_')]
for i in range(5):  # Maximum 5 columns, increase if needed
    data_type = ttk.Combobox(app, values=sample_data_types, state='readonly')
    data_type.grid(column=1, row=2+i, padx=10, pady=10, sticky=tk.W)
    data_types_combobox.append(data_type)

    column_name = ttk.Entry(app)
    column_name.grid(column=3, row=2+i, padx=10, pady=10, sticky=tk.W)
    column_names_entry.append(column_name)

generate_button = ttk.Button(app, text="Generate and Save CSV", command=generate_and_save_data)
generate_button.grid(column=1, row=7, padx=10, pady=20, sticky=tk.W)

app.mainloop()
