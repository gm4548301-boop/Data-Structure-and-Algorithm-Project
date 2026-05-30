import tkinter as tk


class ExecutionPanel:

    def __init__(self, parent):

        self.frame = tk.Frame(
            parent,
            bg="#1F2937"
        )

        self.frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        title = tk.Label(
            self.frame,
            text="LIVE EXECUTION",
            bg="#1F2937",
            fg="#C4B5FD",
            font=("Century Gothic", 12, "bold")
        )

        title.pack(
            pady=(10, 5)
        )

        text_frame = tk.Frame(
            self.frame,
            bg="#1F2937"
        )

        text_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0,10)
        )

        scrollbar = tk.Scrollbar(
            text_frame
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.log = tk.Text(
            text_frame,
            height=22,
            width=35,
            bg="#111827",
            fg="white",
            font=("Consolas", 10),
            wrap="word",
            bd=0,
            yscrollcommand=scrollbar.set
        )

        self.log.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=self.log.yview
        )

    def update(self, text):

        if not text:
            return

        self.log.insert(
            tk.END,
            "• " + text + "\n"
        )

        self.log.see(
            tk.END
        )

    def clear(self):

        self.log.delete(
            "1.0",
            tk.END
        )