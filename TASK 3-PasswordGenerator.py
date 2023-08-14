import tkinter as tk
import random
import string

def generate_password():
    try:
        username = username_entry.get()
        password_length = int(length_entry.get())

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))

        result_text.delete(1.0, tk.END)  
        result_text.insert(tk.END, f"{password}")
        result_text.config(fg="Green")

    except ValueError:
        result_text.insert(tk.END, f"Invalid Input")
        result_text.config(fg="Red")
    

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("650x350+300+100")
root.config(background="Purple")
root.resizable(0,0)

# Title of the window
window_title = tk.Label(root, text="Password Generator",font=("Ink Free",20,"bold"),fg="Black",background="Purple")
window_title.grid(row=0,column=1,pady=9)

# Username input
username_label = tk.Label(root, text="Username:",font=("Comic Sans MS",14),background="Purple",fg="White")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(root,justify="center",font=("Comic Sans MS",14),highlightcolor="#7393B3")
username_entry.grid(row=1,column=1,pady=5,sticky="Snew")


# Password length input
length_label = tk.Label(root, text="Password Length:",font=("Comic Sans MS",14),background="Purple",fg="White")
length_label.grid(row=2, column=0)
length_entry = tk.Entry(root,justify="center",font=("Comic Sans MS",14))
length_entry.grid(row=2, column=1,pady=1)

# Generated result pad
result_label = tk.Label(root, text="Generated Password:",font=("Comic Sans MS",14),background="Purple",fg="White")
result_label.grid(row=12, column=0)

# Result text pad to display the generated password
result_text = tk.Text(root, height=1, width=20, wrap=tk.WORD,font=("Comic Sans MS",14))
result_text.grid(row=12, column=1,pady=1)

# Generate button
generate_button = tk.Button(root, cursor='hand2',text="Generate Password", command=generate_password,font=("Comic Sans MS",14))
generate_button.grid(row=8, column=1,pady=10)

# Reset button
reset_button = tk.Button(root, cursor="hand2",text="Reset", command=reset_fields,font=("Comic Sans MS",14))
reset_button.grid(row=10, column=1,pady=10)

root.mainloop()
