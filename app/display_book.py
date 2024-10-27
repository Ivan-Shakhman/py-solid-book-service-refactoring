class DisplayBook:
    DISPLAYED_TYPES = ["console", "reverse"]

    def console_display(self) -> None:
        print(self.content)

    def reverse_display(self) -> None:
        print(self.content[::-1])

    def display(self, display_type: str) -> None:
        if display_type not in self.DISPLAYED_TYPES:
            raise ValueError(f"Unknown display type: {display_type}")

        match display_type:
            case "console":
                self.console_display()

            case "reverse":
                self.reverse_display()
