class HeapAnimation:

    def __init__(
        self,
        root,
        visualizer,
        update_operation_callback
    ):

        self.root = root
        self.visualizer = visualizer
        self.update_operation = (
            update_operation_callback
        )

    def run(
        self,
        states,
        speed,
        on_finish=None
    ):

        def schedule_step(i):

            if i >= len(states):

                if on_finish:

                    self.root.after(
                        speed,
                        on_finish
                    )

                return

            step = states[i]

            self.visualizer.show_state(
                step["before"],
                step.get(
                    "comparing",
                    []
                ),
                step.get(
                    "swapping",
                    []
                )
            )

            self.update_operation(
                step.get(
                    "operation",
                    ""
                )
            )

            self.root.after(
                speed,
                lambda:
                schedule_step(i + 1)
            )

        schedule_step(0)