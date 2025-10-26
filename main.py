import tkinter as tk
from controllers.controller import Controller

def main():
    print("1-main")
    root = tk.Tk()
    print("2-main")
    print("3-main")
    
    controller = Controller(root)
    
    print("4-main")
    root.mainloop()

if __name__ == "__main__":
    print("0-main")
    main()
