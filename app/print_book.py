class BasePrintBook:
    PRINT_TYPES = []

    def action_print(self) -> None:
        pass

    def print_book(self, print_type: str) -> None:
        if print_type not in self.PRINT_TYPES:
            raise ValueError(f"Unknown print type: {print_type}")

        self.action_print()


class ConsolePrintBook(BasePrintBook):
    PRINT_TYPES = super().PRINT_TYPES + ["console",]

    def action_print(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrintBook(BasePrintBook):
    PRINT_TYPES = super().PRINT_TYPES + ["reverse",]

    def action_print(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
