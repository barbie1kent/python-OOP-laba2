import calendar

class Month:
    def __init__(self, month_num):
        self.month_num = month_num

    def get_first_weekday_num(self):
        first_day_weekday = calendar.monthrange(2022, self.month_num)[0]
        return first_day_weekday
