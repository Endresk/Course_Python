class Multiplier:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, Multiplier):
            return Multiplier(self.value + other.get_value())
        else:
            return Multiplier(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Multiplier):
            return Multiplier(self.value - other.get_value())
        else:
            return Multiplier(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Multiplier):
            return Multiplier(self.value * other.get_value())
        else:
            return Multiplier(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Multiplier):
            return Multiplier(self.value / other.get_value())
        else:
            return Multiplier(self.value / other)


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        super().__init__(value * 100)


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        super().__init__(value * 1000)


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        super().__init__(value * 1000000)


