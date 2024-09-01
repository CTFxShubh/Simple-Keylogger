# PRODIGY_CS_Task-04
## Simple Keylogger

# Overview

This project is a basic keylogger program written in Python that captures and logs keystrokes from the user's keyboard. The keylogger runs in the background and logs all keypresses into a text file for review later. It demonstrates how keyloggers work but should only be used for ethical purposes with full permission from the owner of the device.

# Features

Logs keystrokes: Captures and records all keys pressed on the keyboard.
Saves to a file: The recorded keystrokes are saved in a text file (`keylogs.txt`).
Runs in the background: Once started, the keylogger works in the background, logging all keyboard activities.

# Requirements
To run this keylogger, you need:

Python 3.x

Python library: `pynput`

# Installation

1. Clone the repository:

```bash
git clone https://github.com/CTFxShubh/PRODIGY_CS_Task-04.git
cd simple-keylogger
```

2. Install the required Python library:

Install the `pynput` library using `pip`:

```bash
pip install pynput
```

# Usage 

1. Run the keylogger:

After installing the required library, run the Python script:

```bash
python Simple_keylogger.py
```

2. Logging keystrokes:

Once the keylogger starts, it will log every key pressed on the keyboard and save them in the `keylogs.txt` file in the same directory.

3. Stopping the keylogger:

To stop the keylogger, press `Ctrl + C` in the terminal or manually close the program.

# Ethical Considerations

Keylogging can be a highly invasive technique and should only be used for ethical purposes, such as:

-> Monitoring your own devices: Only log keystrokes on systems you own or have explicit permission to monitor.

-> Educational purposes: Learning and understanding how keyloggers work and the risks associated with them.

Unauthorized usage of keyloggers is illegal and unethical. Always ensure that you have full consent from the device's owner before using this or any keylogging software.

# Example

Here's an example of how the keystrokes are logged in `keylogs.txt`:

![Screenshot 2024-09-01 183219](https://github.com/user-attachments/assets/2fede18d-c171-42ef-94a1-1d209bd1b8b8)

# Disclaimer

This software is provided for educational purposes. The misuse of keylogging software can lead to severe legal consequences. Ensure that you have permission to use this tool.

# License

This project is licensed under the MIT License - see the `LICENSE` file for details.
