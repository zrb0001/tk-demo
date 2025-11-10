import math
import random
import tkinter as tk
from words import encouraging_words


class TipWindow:
    def __init__(self, root, window_id, max_windows):
        self.window_id = window_id
        self.max_windows = max_windows
        self.root = None
        root.after(1000, lambda: self.run(root))

    def run(self, root):
        self.root = tk.Toplevel(root)
        self.root.configure(bg='pink')
        self.__set_position()
        self.__set_words()

    def __set_position(self):
        scale = 20
        t = self.window_id * (2 * math.pi / self.max_windows)
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        screen_x = int(self.root.winfo_screenwidth() // 2 + x * scale)
        screen_y = int(self.root.winfo_screenheight() // 2 - y * scale)
        self.root.geometry(f"240x64+{screen_x}+{screen_y}")

    def __set_words(self):
        if self.window_id == 1:
            self.label = tk.Label(self.root, text=f"总有人间一两风，填我十万八千梦", font=("Arial", 12), bg='pink')
        else:
            self.label = tk.Label(self.root, text=f"{random.choice(encouraging_words)}", font=("Arial", 12), bg='pink')
        self.label.pack()