class DefaultList(list):
    def __init__(self, value):
        self.value = value
        super().__init__()

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)

        except IndexError:
            return self.value
