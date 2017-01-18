class SignRecord:
    name = ''
    month = ''
    records = []

    def __init__(self, n, m):
        self.name = n
        self.month = m
        self.records = []

    def append(self, date, time):
        self.records.append((date, self.name, time))

    def __str__(self):
        return 'name:\t' + self.name + '\n' + 'month:\t' + self.month + '\n' + 'records:\t' + str(self.records)
