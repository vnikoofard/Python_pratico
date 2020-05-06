import tkinter as tk

def conversor():
    temp = y.get()
    celsius = (5/9) * (float(temp)-32)
    x.set(f'{round(celsius,2)} \u2103')
    

window = tk.Tk()
window.title("conversor")
window.resizable(width = False, height = False)

x = tk.StringVar()
x.set("\u2103")

y = tk.DoubleVar()


e1 = tk.Entry(window, width = 10, textvariable = y).grid(row = 0, column = 0)
l1 = tk.Label(window, text = "\u2109").grid(row = 0, column = 1)
b1 = tk.Button(window, text = "\u2192", command = conversor).grid(row = 0, column = 2)
l2 = tk.Label(window, textvariable = x).grid(row = 0, column = 3)

window.mainloop()