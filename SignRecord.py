class SignRecord:
    name = ''
    month = ''
    records = []

    def __init__(self, n, m):
        self.name = n
        self.month = m
        self.records = []

    def append(self, date, time):
        self.records.append((date, time))

    def find_times_by_date(self, date):
        times = []
        for record in self.records:
            if record[0] == date:
                times.append(record[1])
        times.sort()
        return times

    def __str__(self):
        return 'name:\t' + self.name + '\n' + 'month:\t' + self.month + '\n' + 'records:\t' + str(self.records)
