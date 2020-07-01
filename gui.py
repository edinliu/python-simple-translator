import tkinter as tk
from tkinter import ttk
import pyautogui

def window_nearby_cursor(window):
    window.update()
    wr = window.winfo_width()  # width for the Tk root
    hr = window.winfo_height()  # height for the Tk root

    # get screen width and height
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen

    loc = pyautogui.position()  # 獲得游標位置

    if (loc.x + wr) > ws:
        x = loc.x - wr
    else:
        x = loc.x
    if (loc.y + hr) > hs:
        y = loc.y - hr
    else:
        y = loc.y

    window.geometry('%dx%d+%d+%d' % (wr, hr, x, y))
def show(vocabulary):
    root = tk.Tk()
    ttk.Label(text=vocabulary,background='powder blue',padding='0',width='10c').pack()
    root.wm_attributes('-topmost', 1)
    root.title("簡易翻譯機~")  # Add a title
    window_nearby_cursor(root)
    root.mainloop()

if __name__ == "__main__":
    show("example")