import calendar

def websiteCalendar(month, year):
    return calendar.HTMLCalendar().formatmonth(year, month).replace("\n", "")
