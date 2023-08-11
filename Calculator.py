import tkinter as tk
import math

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C", "sqrt", "pow", "mod")
]

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(buttons_frame, text=button_text, font=("Arial", 16), padx=20, pady=10)
        button.grid(row=i, column=j, sticky="nsew")
        button.bind("<Button-1>", on_button_click)

# Additional mathematical functions

def square_root():
    try:
        expression = entry.get()
        result = math.sqrt(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def power():
    try:
        expression = entry.get()
        result = eval(expression) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def modulus():
    try:
        expression = entry.get()
        result = eval(expression) % 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

sqrt_button = tk.Button(buttons_frame, text="√", font=("Arial", 16), padx=20, pady=10, command=square_root)
sqrt_button.grid(row=4, column=1, sticky="nsew")

power_button = tk.Button(buttons_frame, text="^2", font=("Arial", 16), padx=20, pady=10, command=power)
power_button.grid(row=4, column=2, sticky="nsew")

mod_button = tk.Button(buttons_frame, text="%", font=("Arial", 16), padx=20, pady=10, command=modulus)
mod_button.grid(row=4, column=3, sticky="nsew")

root.mainloop()
