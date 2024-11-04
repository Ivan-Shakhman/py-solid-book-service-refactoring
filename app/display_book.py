class BaseDisplayBook():
    DISPLAYED_TYPES = []

    def use_display(self):
        pass

    def display(self, display_type: str) -> None:
        if display_type not in self.DISPLAYED_TYPES:
            raise ValueError(f"Unknown display type: {display_type}")

        self.use_display()


class ConsoleDisplayBook(BaseDisplayBook):
    DISPLAYED_TYPES = super().DISPLAYED_TYPES + ["console"]

    def use_display(self):
        print(self.content)


class ReverseDisplayBook(BaseDisplayBook):
    DISPLAYED_TYPES = super().DISPLAYED_TYPES + ["reverse"]

    def use_display(self):
        print(self.content[::-1])
