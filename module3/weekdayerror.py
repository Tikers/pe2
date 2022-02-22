class WeekDayError(Exception):
    pass
	

class Weeker:

    __days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError("Wrong day!")
        else:
            self.__day = day
        

    def __str__(self):        
        return self.__day

    def add_days(self, n):
        #
        cur_day = self.__days.index(self.__day)
        new_day = (cur_day + n) % 7
        self.__day = self.__days[new_day]

    def subtract_days(self, n):
        idx_cur_day = self.__days.index(self.__day)
        new_day = ((n // 7) * 7 + 7 + idx_cur_day - n) % 7
        self.__day = self.__days[new_day]
        # todo if statement check if end up below or above 7 days
        # and 



try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
