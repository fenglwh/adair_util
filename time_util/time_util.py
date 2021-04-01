from _typeshed import StrPath
import datetime

class Period():
    
    def __init__(self,start,stop):
        if (isinstance(start,datetime.datetime) and isinstance(stop,datetime.datetime)) or (isinstance(start,datetime.date) and isinstance(stop,datetime.datet)):
            self.start = start
            self.stop = stop
        else:
            raise Exception("The start and stop parameter is not datetime or date instance")

    def as_datetime(self):
        if isinstance(self.start,datetime.date):
            self.start = datetime.datetime(self.start)
        if isinstance(self.stop,datetime.date):
            self.stop = datetime.datetime(self.stop)+datetime.timedelta(hours=23,minutes=59,seconds=59,milliseconds=59,microseconds=59)
        return self

    def as_date(self):
        if isinstance(self.start,datetime.datetime):
            self.start = datetime.date(self.start)
        if isinstance(self.stop,datetime.datetime):
            self.stop = datetime.date(self.stop)
        return self

def by_year(year):
    first_day = datetime.date(year=year)
    return first_day, first_day+datetime.timedelta(year=1)-datetime.timedelta(days=1)

def by_month(year,month):
    first_day = datetime.date(year=year,month=month)
    return first_day, first_day+datetime.timedelta(month=1)-datetime.timedelta(days=1)

def by_week(year,week):
    first_day =datetime.date(year=year)
    time_start= first_day+datetime.timedelta(weeks=(week-1),days=1)
    time_stop=first_day+datetime.timedelta(6)
    return time_start, time_stop

def yestoday(current=datetime.date.today()):
    return current-datetime.timedelta(days=1)

def last_week(current):
    today=datetime.date.today()

    return today-datetime.timedelta(days=7), today-datetime.timedelta(days=7)

def this_week():
    pass

def next_week():
    pass

def last_month():
    pass

def last_year():
    pass

def tomorrow():
    return datetime.date.today()+datetime.timedelta(days=1)

def the_day_next_tomorrow():
    return datetime.date.today()+datetime.timedelta(days=2)