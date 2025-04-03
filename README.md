How to Run the Program on Windows (For Non-Coders)

This guide will help you install everything needed and run the program with just a double-click.

--- STEP - 1

Downloading Python 3.10.6
- Open your web browser and go to: https://www.python.org/downloads/release/python-3106/
- Click on "Windows Installer (64-bit)" to download.

--- STEP - 2

Installing Python 3.10.6
- Open the downloaded file.
- Check the box for "Add Python to PATH" (this is important).
- Click "Install Now" and wait for the installation to complete.
- Restart your computer.
- To verify the installation:
  - Press Windows + R on your keyboard.
  - Type cmd and press Enter.
  - The Command Prompt window will open.
  - Type: python --version
  - It should display: Python 3.10.6

--- STEP - 3

Installing Required Dependencies
- Press Windows + R on your keyboard.
- Type cmd and press Enter.
- The Command Prompt window will open.
- Type the following command and press Enter:
  pip install pandas PyQt5 PySide6
- Wait for the installation to complete.

--- STEP - 4

Running the Program
- Open the program folder.
- Double-click the "RUN_APP_FROM_HERE.bat" file.
- The program will start automatically.

--- STEP - 5

Troubleshooting
- If nothing happens when you run the .bat file, restart your computer and try again.
- If you get a Python error, make sure you installed Python 3.10.6 correctly.
- If a module error appears, manually install dependencies by running:
  pip install pandas PyQt5 PySide6
- If the .bat file still doesn’t work, try running it manually in Command Prompt:
  - Open the program folder.
  - Hold Shift + Right-click inside the folder.
  - Click "Open Command Prompt here" or "Open PowerShell window here."
  - Type: RUN_APP_FROM_HERE.bat
  - Press Enter.

---

Now, after installing Python and dependencies, just double-click the "RUN_APP_FROM_HERE.bat" file, and the program will run—no coding needed!
