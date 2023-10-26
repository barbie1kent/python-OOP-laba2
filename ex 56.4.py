from datetime import datetime

class Period:
    def __init__(self, start_time, end_time):
        self.__start_time = start_time
        self.__end_time = end_time

    def get_seconds_difference(self):
        delta = self.__end_time - self.__start_time
        return delta.total_seconds()

    def get_minutes_difference(self):
        seconds = self.get_seconds_difference()
        return seconds / 60

    def get_hours_difference(self):
        minutes = self.get_minutes_difference()
        return minutes / 60


starting = datetime(2022, 2, 2, 10, 0, 20)
end = datetime(2022, 1, 2, 13, 10, 15)
period = Period(starting, end)
print("разницу между моментами в часах:", period.get_hours_difference())