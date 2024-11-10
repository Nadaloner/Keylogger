from pynput.keyboard import Key,Listener 
def premuto(key):
    try:
        print(f"Tasto premuto{key.char}")
    except:
        print(f"Tasto speciale premuto{key}")

def rilasciato(key):
    print(f"Tasto rilasciato{key}")
    if key==Key.esc:             #se tasto premuto ESC si stoppa 
        return False
    

with Listener(on_press=premuto, on_release=rilasciato) as listener:
    listener.join()