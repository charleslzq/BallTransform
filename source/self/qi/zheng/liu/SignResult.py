class SignResult:
    rows = []

    def append(self, date, name, time, note):
        self.rows.append([date, name, time, note])

    def __str__(self):
        return str(self.rows)
