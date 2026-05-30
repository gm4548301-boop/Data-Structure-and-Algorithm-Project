import tkinter as tk
from tkinter import messagebox
import random

from minheap import MinHeap
from maxheap import MaxHeap
from visualizer import HeapVisualizer
from animation import HeapAnimation
from execution_panel import ExecutionPanel

class HeapApp:

    def __init__(self, root):

        self.root = root
        self.heap = MinHeap()
        self.animation_speed = 1000

        self.sidebar = tk.Frame(
            root,
            bg="#0B1023",
            width=260
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.title_label = tk.Label(
            self.sidebar,
            text="Heap Visualizer",
            bg="#0B1023",
            fg="white",
            font=("Century Gothic", 20, "bold")
        )
        self.title_label.pack(pady=30)

        self.heap_var = tk.StringVar(value="Min Heap")

        self.heap_dropdown = tk.OptionMenu(
            self.sidebar,
            self.heap_var,
            "Min Heap",
            "Max Heap",
            command=self.change_heap
        )

        self.heap_dropdown.configure(
            font=("Century Gothic", 20),
            bg="#10B981",
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            width=14,
            relief="flat",
            bd=0,
            cursor="hand2"
        )
        self.heap_dropdown.pack(pady=10)

        self.info_frame = tk.Frame(self.sidebar, bg="#1F2937")
        self.info_frame.pack(fill="x", padx=20, pady=30)

        self.execution_panel = ExecutionPanel(
            self.sidebar
        )

        self.info_title = tk.Label(
            self.info_frame,
            text="HEAP INFO",
            bg="#1F2937",
            fg="#C4B5FD",
            font=("Century Gothic", 12, "bold")
        )
        self.info_title.pack(pady=(15, 5))

        self.info_label = tk.Label(
            self.info_frame,
            text="Elements: 0",
            bg="#1F2937",
            fg="white",
            font=("Century Gothic", 20, "bold")
        )
        self.info_label.pack(pady=(5, 5))

        self.main_frame = tk.Frame(root, bg="#111827")
        self.main_frame.pack(fill="both", expand=True)

        self.top_frame = tk.Frame(self.main_frame, bg="#111827")
        self.top_frame.pack(pady=15, fill="x")

        self.entry_label = tk.Label(
            self.top_frame,
            text="Enter numbers separated by spaces",
            bg="#111827",
            fg="#C4B5FD",
            font=("Century Gothic", 12, "bold")
        )
        self.entry_label.pack(anchor="w", padx=10, pady=(0, 8))

        self.input_row = tk.Frame(self.top_frame, bg="#111827")
        self.input_row.pack()

        self.entry = tk.Entry(
            self.top_frame,
            font=("Century Gothic", 18),
            width=35,
            bg="#1F2937",
            fg="white",
            insertbackground="white"
        )
        self.entry.pack(in_=self.input_row, side="left", padx=10, ipady=10)

        button_style = {
            "font": ("Century Gothic", 12, "bold"),
            "fg": "black",
            "width": 12,
            "height": 2,
            "relief": "flat",
            "cursor": "hand2"
        }

        self.build_btn = tk.Button(
            self.top_frame,
            text="Build",
            bg="#22C55E",
            command=self.build,
            **button_style
        )
        self.build_btn.pack(in_=self.input_row, side="left", padx=5)

        self.insert_btn = tk.Button(
            self.top_frame,
            text="Insert",
            bg="#C4B5FD",
            command=self.insert,
            **button_style
        )
        self.insert_btn.pack(in_=self.input_row, side="left", padx=5)

        self.random_btn = tk.Button(
            self.top_frame,
            text="Random",
            bg="#C4B5FD",
            command=self.generate_random,
            **button_style
        )
        self.random_btn.pack(in_=self.input_row, side="left", padx=5)

        self.delete_btn = tk.Button(
            self.top_frame,
            text="Delete",
            bg="#C4B5FD",
            command=self.delete,
            **button_style
        )
        self.delete_btn.pack(in_=self.input_row, side="left", padx=5)

        self.reset_btn = tk.Button(
            self.top_frame,
            text="Reset",
            bg="#C4B5FD",
            command=self.reset,
            **button_style
        )
        self.reset_btn.pack(in_=self.input_row, side="left", padx=5)

        self.canvas = tk.Canvas(
            self.main_frame,
            bg="#1A1F4B",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True, padx=15, pady=15)

        self.speed_label = tk.Label(
            self.main_frame,
            text="Animation Speed (ms)",
            bg="#111827",
            fg="white",
            font=("Century Gothic", 16, "bold")
        )
        self.speed_label.pack()

        self.speed_scale = tk.Scale(
            self.main_frame,
            from_=100,
            to=2000,
            orient="horizontal",
            bg="#111827",
            fg="white",
            highlightthickness=0,
            length=500,
            sliderlength=30,
            width=20,
            command=self.update_speed
        )
        self.speed_scale.set(1000)
        self.speed_scale.pack(fill="x", padx=30)

        self.legend_frame = tk.Frame(self.sidebar, bg="#0B1023")
        self.legend_frame.pack(side="bottom", pady=20)

        legend_style = {
            "bg": "#0B1023",
            "fg": "white",
            "font": ("Century Gothic", 11)
        }

        tk.Label(self.legend_frame, text="🟣 Normal Node", **legend_style).pack(anchor="w")
        tk.Label(self.legend_frame, text="🩷 Comparing", **legend_style).pack(anchor="w")
        tk.Label(self.legend_frame, text="🟠 Swapping", **legend_style).pack(anchor="w")

        self.visualizer = HeapVisualizer(self.canvas)

        self.animation = HeapAnimation(
            self.root,
            self.visualizer,
            self.update_operation
        )

    def update_operation(self, text):

        self.execution_panel.update(
            text
        )

    def update_speed(self, value):
        self.animation_speed = int(value)

    def update_info(self):
        self.info_label.config(text=f"Elements: {len(self.heap.data)}")

    def change_heap(self, selected):

        self.heap = MinHeap() if selected == "Min Heap" else MaxHeap()

        if selected == "Min Heap":
            self.heap_dropdown.config(
                bg="#10B981",
                fg="white",
                activebackground="#059669"
            )
        else:
            self.heap_dropdown.config(
                bg="#EF4444",
                fg="white",
                activebackground="#DC2626"
            )

        self.reset()

    def generate_random(self):
        size = random.randint(5, 10)
        numbers = [str(random.randint(1, 99)) for _ in range(size)]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, " ".join(numbers))

    def build(self):
        try:
            values = list(map(int, self.entry.get().split()))
            self.heap.data = []
            all_states = []

            self.update_operation("Building heap")

            for value in values:
                self.update_operation(f"Inserting {value}")
                states = self.heap.insert(value)
                all_states.extend(states)

            self.animation.run(all_states, self.animation_speed, self.finish_animation)

        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid numbers")

    def insert(self):
        try:
            value = int(self.entry.get())
            self.update_operation(f"Inserting {value}")
            states = self.heap.insert(value)
            self.animation.run(states, self.animation_speed, self.finish_animation)

        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid number")

    def delete(self):
        try:
            index = int(self.entry.get())
            self.update_operation(f"Deleting index {index}")
            states = self.heap.delete_index(index)

            if not states:
                messagebox.showerror("Invalid Index", "Index does not exist")
                return

            self.animation.run(states, self.animation_speed, self.finish_animation)

        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid index")

    def reset(self):

        self.heap.data = []

        self.visualizer.display_data = []

        self.visualizer.comparing = []

        self.visualizer.swapping = []

        self.visualizer.draw()

        self.entry.delete(
            0,
            tk.END
        )

        self.execution_panel.clear()

        self.update_info()

    def finish_animation(self):
        self.visualizer.display_data = self.heap.data.copy()
        self.visualizer.comparing = []
        self.visualizer.swapping = []
        self.visualizer.draw()
        self.update_info()
        self.update_operation("Idle")