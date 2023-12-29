import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(entry_length.get())

    if password_length <= 0:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return

    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    # Display the generated password
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def copy_to_clipboard():
    generated_password = entry_password.get()

    if generated_password:
        window.clipboard_clear()
        window.clipboard_append(generated_password)
        window.update()
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")

# Create main window
window = tk.Tk()
window.title("Random Password Generator")

# Password length input
label_length = tk.Label(window, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Display generated password
# entry_password = tk.Entry(window)
entry_password = tk.Entry(window)
entry_password.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
