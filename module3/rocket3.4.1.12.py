"""
code for assignment 3.4.1.12 edube.org python institute

"""
from re import M


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    def __str__(self):
        # format to hh:mm:ss
        h = formatTwoDiget(self.__hours)
        m = formatTwoDiget(self.__minutes)
        s = formatTwoDiget(self.__seconds)
        s_time = f"{h}:{m}:{s}"
        return s_time


    def next_second(self):
        # inc by one sec
        add_min, new_sec = self.__inc_to_60(self.__seconds, 1)
        add_h, new_min = self.__inc_to_60(self.__minutes, add_min)
        new_h = self.__inc_hour(self.__hours, add_h)
        self.__seconds = new_sec
        self.__minutes = new_min
        self.__hours = new_h
        #return 0

    def prev_second(self):
        # dec by one sec
        add_min, new_sec = self.__inc_to_60(self.__seconds, -1)
        add_h, new_min = self.__inc_to_60(self.__minutes, add_min)
        new_h = self.__inc_hour(self.__hours, add_h)
        self.__seconds = new_sec
        self.__minutes = new_min
        self.__hours = new_h
        #return 0

    def __inc_to_60(self, val, inc=0):
        new = val + inc
        if new > 59:
            sec = new-60
            return 1, sec
        elif new < 0:
            sec = new+60
            return -1, sec
        else:
            return new

    def __inc_hour(self, hours, inc=0):
        new_hours = hours + inc
        if new_hours > 23:
            return new_hours-24
        elif new_hours < 0:
            return new_hours+24
        else:
            return new_hours


def formatTwoDiget(val):
    if val < 10:
        return "0" + str(val)
    else:
        return str(val)


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
