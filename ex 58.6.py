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
    def plus_days(self, days):
        date = datetime(self.year, self.month, self.day)
        new_date = date + timedelta(days=days)
        self.year = new_date.year
        self.month = new_date.month
        self.day = new_date.day
