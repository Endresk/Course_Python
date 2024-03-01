class MathClock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, minutes):
        self.minutes += minutes
        self.hours += self.minutes // 60
        self.minutes %= 60

        return self

    def __mul__(self, hours):
        self.hours += hours
        self.hours %= 24
        return self



