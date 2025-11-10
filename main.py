import tkinter as tk

from window import TipWindow


def draw_window():
    root = tk.Tk()
    root.title(f"Controller")
    root.geometry("150x100")

    num_windows = 64
    for i in range(num_windows):
        window = TipWindow(root, i + 1, num_windows)
        window.run()

    root.mainloop()

if "__main__" == __name__:
    draw_window()