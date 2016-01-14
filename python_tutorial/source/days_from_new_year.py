from datetime import datetime


def days_since_new_year(mydate):
    # TODO: get Jan 1 of the same year as mydate
    jan_1 = datetime()
    jan_1_delta = mydate - jan_1
    jan_1_seconds =  jan_1_delta.total_seconds()
    ## TODO: convert seconds to days
    days = 0
    return days

days = days_since_new_year(datetime.now())
print ("Days since the begging of the year %d" % days)
