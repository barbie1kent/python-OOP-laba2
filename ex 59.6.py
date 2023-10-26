import calendar

class Month:
    def __init__(self, month_num):
        self.month_num = month_num

    def get_last_weekday_num(self):
        last_day_weekday = (calendar.monthrange(2022, self.month_num)[0] + self.get_lastday_num() - 1) % 7
        return last_day_weekday