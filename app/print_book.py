class PrintBook:

    def console_print(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def reverse_print(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def print_book(self, print_type: str) -> None:
        if print_type not in ("console", "reverse"):
            raise ValueError(f"Unknown print type: {print_type}")

        match print_type:
            case "console":
                self.console_print()

            case "reverse":
                self.reverse_print()
