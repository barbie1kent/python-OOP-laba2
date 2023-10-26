import calendar

class Month:
    def __init__(self, month_num):
        self.month_num = month_num

    def get_month_name(self):
        return calendar.month_name[self.month_num]
