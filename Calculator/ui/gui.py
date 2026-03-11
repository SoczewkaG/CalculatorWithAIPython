import tkinter as tk

class CalculatorGUI:

    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.controller = controller
    
        self.history = tk.Label(self.root,text="",anchor="e",font=("Arial", 12),bg="white")
        self.history.grid(row=0, column=0, columnspan=4, sticky="we")
        self.history.config(text = "0")

        self.display_var = tk.StringVar()
        self.display = tk.Entry(self.root, width=20,  font=("Arial", 24), justify="right", textvariable=self.display_var, state="readonly")
        self.display.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.create_buttons()


    def run(self):
        self.root.mainloop()


    def add_digit(self, digit):
        current = self.display_var.get()
        self.display_var.set(current + digit)


    def clear(self):
        self.display.delete(0, tk.END)


    def calculate(self):
        expression = self.display.get()
        self.history.config(text=expression)

        result = self.controller.calculate(expression)

        self.display.delete(0, tk.END)
        self.display_var.set(result)

    def create_buttons(self):
        buttons = [
            ("7",2,0), ("8",2,1), ("9",2,2), (" / ",2,3),
            ("4",3,0), ("5",3,1), ("6",3,2), (" * ",3,3),
            ("1",4,0), ("2",4,1), ("3",4,2), (" - ",4,3),
            ("0",5,0), (" . ",5,1), ("=",5,2), (" + ",5,3)
        ]

        for (text,row,col) in buttons:

            if text == "=":
                command = self.calculate
            else:
                command = lambda t=text: self.add_digit(t)

            button = tk.Button(
                self.root,
                text=text,
                width=5,
                height=2,
                font=("Arial",18),
                command=command
            )

            button.grid(row=row, column=col, padx=5, pady=5)