from datetime import datetime
import calendar

class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_weekday_name(self):
        weekday_num = self.get_weekday()
        return calendar.day_name[weekday_num]
