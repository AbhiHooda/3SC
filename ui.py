import json
import tkinter as tk
from tkinter import ttk, messagebox
import requests


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("API Data Display")

        # Create input fields
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.inputs = []
        self.headers = ['userName', 'merchantName', 'amount', 'currency', 'productId', 'quantity']
        for i in range(1, 7):
            label = ttk.Label(self.input_frame, text=f"{self.headers[i - 1]}")
            label.grid(row=i - 1, column=0, padx=(0, 5))
            entry = ttk.Entry(self.input_frame)
            entry.grid(row=i - 1, column=1)
            self.inputs.append(entry)

        # Submit button
        submit_button = ttk.Button(self.input_frame, text="Submit", command=self.call_api)
        submit_button.grid(row=6, column=0, columnspan=2, pady=(10, 0))

        # Table
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.table = ttk.Treeview(self.table_frame,
                                  columns=(
                                      "Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6",
                                      "Column 7"))
        self.table.heading("#0", text="ID")
        self.table.heading("Column 1", text="userName")
        self.table.heading("Column 2", text="merchantName")
        self.table.heading("Column 3", text="amount")
        self.table.heading("Column 4", text="currency")
        self.table.heading("Column 5", text="productId")
        self.table.heading("Column 6", text="quantity")
        self.table.heading("Column 7", text="date")
        self.table.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="w")

        # Search bar
        self.search_frame = ttk.Frame(self.root)
        self.search_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        search_label = ttk.Label(self.search_frame, text="Search:")
        search_label.grid(row=0, column=0, padx=(0, 5))
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1)
        search_button = ttk.Button(self.search_frame, text="Search", command=self.search_api)
        search_button.grid(row=0, column=2, padx=(5, 0))

    def call_api(self):
        # Implement your API call logic here using self.inputs to get input values
        # Update the table with API response
        inp = [entry.get() for entry in self.inputs]
        url = 'http://localhost:8080/create'
        myobj = {'userName': str(inp[0]), 'merchantName': str(inp[1]), 'amount': str(inp[2]),
                 'currency': str(inp[3]), 'productId': str(inp[4]), 'quantity': str(inp[5])}
        # print(myobj)
        x = requests.post(url, json=myobj)
        # print (x.text)
        messagebox.showinfo('Message', f'{x.text}')
        self.update_table()

    def search_api(self):
        tx = self.search_entry.get()
        url = f'http://localhost:8080/search?tid={tx}'
        print(url)
        info = requests.get(url)
        print('here')
        # # print(json.loads(info.text))
        # print(list(info.json()))
        # for ll in info.json():
        #     print(ll)

        self.update_table(info.json())

    def update_table(self, data=[]):
        # Implement logic to update the table with API response
        # This could involve fetching data and populating the table
        # For demonstration, updating the table with sample data
        info = []
        if len(data) == 0:
            url = 'http://localhost:8080/fetchAllsearch'
            x = requests.get(url)
            info = x.json()
        else:
            info = data

        self.table.delete(*self.table.get_children())
        for row in info:
            self.table.insert("", "end", values=row)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
