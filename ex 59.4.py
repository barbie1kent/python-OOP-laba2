import calendar

class Month:
    def __init__(self, month_num):
        self.month_num = month_num

    def get_lastday_num(self):
        days_in_month = calendar.monthrange(2022, self.month_num)[1]
        return days_in_month
