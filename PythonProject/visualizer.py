import math

class HeapVisualizer:

    def __init__(self, canvas):

        self.canvas = canvas

        self.display_data = []

        self.comparing = []

        self.swapping = []

        self.bg_color = "#1A1F4B"

        self.line_color = "#C4B5FD"

        self.normal_color = "#8B5CF6"

        self.compare_color = "#EC4899"

        self.swap_color = "#F59E0B"

        self.text_color = "white"

    def show_state(
        self,
        state,
        comparing=None,
        swapping=None
    ):

        self.display_data = state.copy()

        self.comparing = comparing if comparing else []

        self.swapping = swapping if swapping else []

        self.draw()

    def draw(self):

        self.canvas.configure(
            bg=self.bg_color
        )

        self.canvas.delete("all")

        if not self.display_data:
            return

        positions = self.get_positions()

        for i in range(len(self.display_data)):

            if i != 0:

                parent = (i - 1) // 2

                px, py = positions[parent]

                x, y = positions[i]

                self.canvas.create_line(
                    px,
                    py,
                    x,
                    y,
                    width=3,
                    fill=self.line_color
                )

        for i, value in enumerate(self.display_data):

            x, y = positions[i]

            r = 32

            if i in self.swapping:

                color = self.swap_color

            elif i in self.comparing:

                color = self.compare_color

            else:

                color = self.normal_color

            self.canvas.create_oval(
                x - r,
                y - r,
                x + r,
                y + r,
                fill=color,
                outline="white",
                width=2
            )

            self.canvas.create_text(
                x,
                y - 42,
                text=f"[{i}]",
                fill="#CBD5E1",
                font=("Century Gothic", 10, "bold")
            )

            self.canvas.create_text(
                x,
                y,
                text=str(value),
                fill=self.text_color,
                font=("Century Gothic", 18, "bold")
            )

        self.draw_array()

    def get_positions(self):

        positions = {}

        width = int(
            self.canvas.winfo_width()
        )

        if width <= 1:
            width = 1400

        for i in range(len(self.display_data)):

            level = int(
                math.log2(i + 1)
            )

            nodes = 2 ** level

            index = i - (2 ** level - 1)

            spacing = width // (nodes + 1)

            x = spacing * (index + 1)

            y = 100 + level * 110

            positions[i] = (x, y)

        return positions

    def draw_array(self):

        box_size = 60

        spacing = 10

        n = len(self.display_data)

        total_width = (
            n * box_size +
            (n - 1) * spacing
        )

        canvas_width = int(
            self.canvas.winfo_width()
        )

        x_start = (
            canvas_width - total_width
        ) / 2

        y = 540

        for i, value in enumerate(self.display_data):

            x = x_start + i * (
                box_size + spacing
            )

            if i in self.swapping:

                color = self.swap_color

            elif i in self.comparing:

                color = self.compare_color

            else:

                color = self.normal_color

            self.canvas.create_text(
                x + box_size / 2,
                y - 15,
                text=f"[{i}]",
                fill="white",
                font=("Century Gothic", 10)
            )

            self.canvas.create_rectangle(
                x,
                y,
                x + box_size,
                y + box_size,
                fill=color,
                outline="white",
                width=2
            )

            self.canvas.create_text(
                x + box_size / 2,
                y + box_size / 2,
                text=str(value),
                fill="white",
                font=("Century Gothic", 16, "bold")
            )