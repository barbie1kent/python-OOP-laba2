from datetime import datetime
import calendar

class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_month_name(self):
        return calendar.month_name[self.month]
