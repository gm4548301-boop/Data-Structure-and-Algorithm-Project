import tkinter as tk
from ui import HeapApp

root = tk.Tk()

root.title("Heap Visualizer")
root.state("zoomed")
root.resizable(False, False)

app = HeapApp(root)

root.mainloop()