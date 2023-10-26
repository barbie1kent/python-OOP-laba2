from datetime import datetime
import calendar

class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_weekday(self):
        return datetime.date(self.year, self.month, self.day).weekday()

    def get_weekday_name(self):
        weekday_num = self.get_weekday()
        return calendar.day_name[weekday_num]

    def get_month_name(self):
        return calendar.month_name[self.month]

class ZateExt(Zate):
    def plus_months(self, months):
        new_year = self.year + (self.month + months) // 12
        new_month = (self.month + months) % 12
        if new_month == 0:
            new_month = 12
            new_year -= 1
        self.year = new_year
        self.month = new_month
