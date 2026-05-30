import tkinter as tk

def create_controls(app):

    app.controls = tk.Frame(
        app.root,
        bg="#0F172A"
    )

    app.controls.pack(
        pady=10,
        fill="x"
    )

    app.control_buttons = tk.Frame(
        app.controls,
        bg="#0F172A"
    )

    app.control_buttons.pack()

    app.entry = tk.Entry(
        app.control_buttons,
        width=35,
        font=("Century Gothic", 16),
        bd=3,
        relief="ridge"
    )

    app.entry.pack(
        side="left",
        padx=10,
        pady=10,
        ipady=5
    )

    app.build_btn = tk.Button(
        app.control_buttons,
        text="Build Heap",
        command=app.build,
        font=("Century Gothic", 14, "bold"),
        width=13,
        height=2
    )

    app.build_btn.pack(side="left", padx=5)

    app.insert_btn = tk.Button(
        app.control_buttons,
        text="Insert",
        command=app.insert,
        font=("Century Gothic", 14, "bold"),
        width=13,
        height=2
    )

    app.insert_btn.pack(side="left", padx=5)

    app.delete_btn = tk.Button(
        app.control_buttons,
        text="Delete Root",
        command=app.delete,
        font=("Century Gothic", 14, "bold"),
        width=13,
        height=2
    )

    app.delete_btn.pack(side="left", padx=5)

    app.reset_btn = tk.Button(
        app.control_buttons,
        text="Reset",
        command=app.reset,
        font=("Century Gothic", 14, "bold"),
        width=13,
        height=2
    )

    app.reset_btn.pack(side="left", padx=5)

    app.speed_label = tk.Label(
        app.control_buttons,
        text="Speed(ms):",
        bg="#0F172A",
        fg="white",
        font=("Century Gothic", 12, "bold")
    )

    app.speed_label.pack(side="left", padx=10)

    app.speed_entry = tk.Entry(
        app.control_buttons,
        width=8,
        font=("Century Gothic", 12)
    )

    app.speed_entry.insert(0, "1000")

    app.speed_entry.pack(
        side="left",
        padx=5,
        ipady=4
    )

    app.speed_btn = tk.Button(
        app.control_buttons,
        text="Set Speed",
        command=app.set_speed,
        font=("Century Gothic", 14, "bold"),
        width=13,
        height=2
    )

    app.speed_btn.pack(side="left", padx=5)

