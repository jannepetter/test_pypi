class TestStuff:

    def __init__(self, some) -> None:
        self.some = some

    def say(self):
        msg = f"main {self.some}"
        print(msg)
