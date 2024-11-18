
# File Organizer

File Organizer is a Python-powered desktop application designed to streamline the process of organizing downloaded files into specific folders. With a user-friendly GUI, you can effortlessly transfer files to predefined destinations based on subject or category, saving time and effort.




## Features

- **Graphical User Interface (GUI):** Intuitive interface using Tkinter for ease of use.

- **Subject Selection:** Choose the destination folder from a drop-down menu.

- **File Input:** Add files through a file dialog or drag-and-drop functionality.

- **One-Click Transfer:** Automatically move files to the selected folder with a single click.

- **Customizable Paths:** Easily configure and update folder paths to suit your needs.

- **Error Handling:** Alerts for missing selections or failed transfers.


## How it works

1. Select a subject from the drop-down menu (e.g., "Computer Network").

2. Add files to the transfer queue using the Add Files button.

3. Press the Transfer Files button to organize the selected files into the appropriate folder.
## Installation

1. Clone the repository:

```bash
  git clone https://github.com/Mouri69/File-Organizer
```
2. Navigate to the project directory:

```bash
  cd fileOrganizer
```

3. Run the application:
```bash
  python organizer.py

```
    
## Environment Variables

To run this project, you will need to update the ```SUBJECT_FOLDERS``` dictionary in ```organizer.py``` to match your desired folder structure

```
SUBJECT_FOLDERS = {
    "Computer Network": "E:\Path\To\Folder",
    "Computer Graphics": "E:\Path\To\Folder",
    "Foundation of Information System": "E:\Path\To\Folder",
    "Intelligent System": "E:\Path\To\Folder",
    "Database System": "E:\Path\To\Folder",
}

```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your enhancements.
