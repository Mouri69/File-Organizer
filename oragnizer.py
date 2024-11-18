import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Configuration for the subject folders
SUBJECT_FOLDERS = {
    "Computer Network": "E:\Path\To\Folder",
    "Computer Graphics": "E:\Path\To\Folder",
    "Foundation of Information System": "E:\Path\To\Folder",
    "Intelligent System": "E:\Path\To\Folder",
    "Database System": "E:\Path\To\Folder",
}

# Function to add files to the listbox
def add_files():
    files = filedialog.askopenfilenames(title="Select Files to Transfer")
    for file in files:
        file_listbox.insert(tk.END, file)

# Function to move files to the selected destination
def transfer_files():
    selected_subject = subject_menu.get()
    if selected_subject not in SUBJECT_FOLDERS:
        messagebox.showerror("Error", "Please select a valid subject.")
        return

    destination_folder = SUBJECT_FOLDERS[selected_subject]
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)  # Create the folder if it doesn't exist

    for idx in range(file_listbox.size()):
        file_path = file_listbox.get(idx)
        try:
            shutil.move(file_path, destination_folder)
        except Exception as e:
            messagebox.showerror("Error", f"Could not move file: {file_path}\n{e}")
            return
    
    file_listbox.delete(0, tk.END)  # Clear the listbox after transfer
    messagebox.showinfo("Success", "Files transferred successfully!")

# GUI Setup
root = tk.Tk()
root.title("File Transfer Organizer")
root.geometry("600x400")

# Drop-down menu for subject selection
ttk.Label(root, text="Select Subject:").pack(pady=5)
subject_menu = ttk.Combobox(root, values=list(SUBJECT_FOLDERS.keys()), state="readonly")
subject_menu.pack(pady=5)

# Listbox to display files to be transferred
ttk.Label(root, text="Files to Transfer:").pack(pady=5)
file_listbox = tk.Listbox(root, selectmode=tk.EXTENDED, width=80, height=10)
file_listbox.pack(pady=5)

# Buttons for adding files and transferring them
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Files", command=add_files)
add_button.grid(row=0, column=0, padx=10)

transfer_button = ttk.Button(button_frame, text="Transfer Files", command=transfer_files)
transfer_button.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()
